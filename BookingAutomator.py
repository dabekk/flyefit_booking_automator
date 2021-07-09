from selenium import webdriver
import time
import boto3
import json


class BookingAutomator:
    def __init__(self, path):
        self.path = path
        self.driver = webdriver.Chrome(self.path)

    # get login creds for Flyefit from AWS secrets manager
    def _get_creds_from_secrets_manager(self, secret_name, region_name):

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name="secretsmanager",
            region_name=region_name
        )
        secret_value = client.get_secret_value(SecretId=secret_name)
        secret_dict = json.loads(secret_value["SecretString"])
        return (secret_dict["FLYEFIT_LOGIN"], secret_dict["FLYEFIT_PASS"])

    def _login_to_site(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get("https://www.flyefit.ie/")
        login_button = self.driver.find_element_by_id("menu-item-195")
        login_button.click()

        email_input = self.driver.find_element_by_id("email_address")
        password_input = self.driver.find_element_by_id("password")

        flyefit_creds = self._get_creds_from_secrets_manager("flyefit_creds", "eu-west-1")

        email_input.send_keys(flyefit_creds[0])
        password_input.send_keys(flyefit_creds[1])

    # targets elements/buttons on webpages and clicks then to book workout
    def _book_workout(self):
        login_button = self.driver.find_element_by_class_name("link")
        login_button.click()

        book_workout = self.driver.find_element_by_link_text("Book a workout")
        book_workout.click()

        location_button = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/"
                                                            "section[1]/div[2]/div[1]/form[1]/div[1]"
                                                            "/div[2]/div[1]/div[1]/div[2]/span[1]")
        location_button.click()
        location_selection = self.driver.find_element_by_xpath("//li[contains(text(),'Tallaght')]")
        location_selection.click()

        date_button = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/section[1]"
                                                        "/div[2]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]"
                                                        "/div[2]/span[1]")
        date_button.click()
        date_selection = self.driver.find_element_by_xpath("//li[contains(text(),'Tomorrow')]")
        date_selection.click()

        time_button = self.driver.find_element_by_xpath("//p[@id='btn_1869050']")
        time_button.click()

        time.sleep(3)   # allow popup to load
        book_button = self.driver.find_element_by_xpath("//a[@id='book_class']")
        book_button.click()

        # logout does not yet work. Workaround to exit browser
        logout_button = self.driver.find_element_by_xpath("//header/div[1]/div[1]/div[1]/ul[1]/li[6]/a[1]")
        logout_button.click()

    def book_workout(self):
        self._login_to_site()
        self._book_workout()


path = "C:/Users/Kamil/PycharmProjects/pythonProject/chromedriver.exe"  # must give path to webdriver file
booking_automator = BookingAutomator(path)
booking_automator.book_workout()

# flyefit_booking_automator

Python class to automatically book a gym slot in Flyefit gyms.

This tool was used during 2020/2021 when Flyefit gyms in Ireland had restricted access and required members to pre-book their time slots. To ensure consistent bookings, users can use this tool to automate booking in advance so that a slot is always booked for a specified time.

This script would be deployed to an AWS EC2 server (T2.micro - free tier) and executed daily (Monday-Friday) and a desired time via cron jobs.

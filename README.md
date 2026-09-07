# FlyeFit Booking Automator

A Python automation that books gym slots automatically, deployed to AWS and run on a daily schedule via cron.

## What it does

- Authenticates against the FlyeFit booking system
- Books a slot for a specified day and time
- Runs unattended on a schedule (Monday-Friday) via cron
- Designed to fail quietly and log outcomes, so a missed run is visible

## Architecture

- **Language:** Python (single `BookingAutomator` class)
- **Deployment:** AWS EC2 (t2.micro, free tier)
- **Scheduling:** cron jobs triggering the script daily at a set time
- **Model:** trigger-based, unattended automation, no human in the loop once configured

## Usage

1. Set your FlyeFit credentials and desired booking slot in the configuration.
2. Run manually:
```bash
   python BookingAutomator.py
```
3. For scheduled use, add a cron entry on the host, e.g. book every weekday at 07:00:

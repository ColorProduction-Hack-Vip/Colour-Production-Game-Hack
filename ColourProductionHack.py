#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
import smtplib
from datetime import date, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Expiry date set to one year from today
expiry_date = date.today() + timedelta(days=365)
today = date.today()

# RAIHAN color codes for a colorful design
green = "\033[92m"
cyan = "\033[96m"
nc = "\033[0m"
red = "\033[91m"
yellow = "\033[93m"
purple = "\033[95m"
bold = "\033[1m"
underline = "\033[4m"

# Email configuration (update with actual sender details)
sender_email = "your_email@gmail.com"  # Replace with your email
receiver_email = "aburaihantalukder20@gmail.com"
password = "your_password"  # Replace with your email password

def send_email():
    """Send an automatic email notification at script start."""
    subject = "Raihan Script Notification"
    body = "The Raihan script has been started on a new device."
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"{green}Notification email sent successfully.{nc}")
    except Exception as e:
        print(f"{red}Failed to send email. Error: {e}{nc}")

def display_banner():
    """Clear terminal and display the banner."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    system('https://github.com/ColorProduction-Hack-Vip')

def animate_message(message, duration=20):
    """Display an animated loading message."""
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write(f'\r{yellow}{message} {c}{nc}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(duration)
    done = True

def get_sum_of_digits(n):
    """Calculate sum of digits for the given number."""
    return sum(int(digit) for digit in str(n))

def play_game():
    """Main game logic."""
    display_banner()
    print(f"{purple}{bold}{underline}Contact me on Telegram: @T_B_H_20{nc}")
    print(f"{yellow}----------------------------------------{nc}")
    print(f"{bold}{green}Welcome to ColorProduction-Hack-Vip{nc}")
    print(f"{yellow}----------------------------------------{nc}")
    print(f"{yellow}Hi Dear {nc}")

    # Display this message once at the start
    animate_message("Please Wait A Moment....")

    period = 1  # Initial period
    numbers = []
    keep_playing = True

    while keep_playing:
        display_banner()
        print(f"{cyan}Enter Your Last Win 3-Digit Period Number√ Example: If you give 100 number then your hack result will be 10{period}:{nc}")

        try:
            current = int(input(f"{green}Your Input: {nc}"))
        except ValueError:
            print(f"{red}Invalid input! Please enter a valid number.{nc}")
            continue

        print(f"\n{green}--------- Server successfully hacked ----------{nc}")
        animate_message("Hack Processing...")

        print(f"\n{green}--------- Hack successfull-------------{nc}\n")
        
        # Determine color based on the sum of digits
        digit_sum = get_sum_of_digits(current)
        color = "RED" if digit_sum % 2 == 0 else "GREEN"
        color_icon = "" if color == "RED" else ""
        
        print(f"{cyan}Your Hacking Period Result is {period + 1}: {bold}{color_icon} {color}{nc}")

        # Increment period and record the price
        period += 1
        numbers.append(current)

        # Ask user if they want to continue
        try:
            keep_playing = bool(int(input(f"\n{yellow}Do you want to continue? Press 1 to play again, 0 to exit: {nc}")))
        except ValueError:
            print(f"{red}Invalid input! Exiting the game.{nc}")
            break

        # If more than 50 rounds, stop the game and thank the player
        if len(numbers) > 50:
            display_banner()
            system('figlet Thank you!!')
            print(f"{green}Thank you for playing! Please play again at the specified time.{nc}")
            print(f"{purple}----------- Session Time Over ----------{nc}")
            sys.exit(f"\n\n\n{cyan}Contact on Telegram @T_B_H_20{nc}")

if expiry_date > today:
    send_email()  # Send notification email at the start of the script
    play_game()
else:
    print(f"{red}{bold}This script has expired. Please contact support for an updated version.{nc}")
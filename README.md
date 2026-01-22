# Website_blocker
import time
from datetime import datetime as dt

# Path of hosts file
# For Windows:
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# For Linux / Mac (comment Windows path and uncomment below)
# hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

# Websites to block
website_list = [
    "www.facebook.com",
    "facebook.com",
    "www.instagram.com",
    "instagram.com",
    "www.youtube.com",
    "youtube.com"
]

# Working hours (24-hour format)
start_hour = 9
end_hour = 17

while True:
    current_time = dt.now()

    if current_time.hour >= start_hour and current_time.hour < end_hour:
        print("🔒 Working hours... Websites are blocked")

        with open(hosts_path, "r+") as file:
            content = file.read()

            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")

    else:
        print("🔓 Free time... Websites are unblocked")

        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()

    time.sleep(60)

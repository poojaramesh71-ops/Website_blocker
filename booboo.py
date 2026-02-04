import time
from datetime import datetime as dt

# Path to hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# For Linux/Mac:
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

# Working hours (9 AM to 5 PM)
start_hour = 9
end_hour = 17

print("Website Blocker Started...")

while True:
    current_time = dt.now()
    if start_hour <= current_time.hour < end_hour:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
        print("Websites are blocked")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Websites are unblocked")

    time.sleep(5)


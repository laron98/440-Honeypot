import time
import requests
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Replace these variables with your own email and password
API_KEY = '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'

# Define the path of the file you want to monitor
FILE_PATH = '/var/log/audit/audit.log'

# Define the message you want to send in the email
message = 'The file at {} has been modified.'.format(FILE_PATH)

# Define the email function
def send_email():
    url = "https://api.sendinblue.com/v3/smtp/email"

    payload = {
        "sender": {
            "name": "HoneyPotAlerter",
            "email": "auditemail440@gmail.com"
        },
        "to": [
            {
                "email": "auditemail440@gmail.com",
                "name": "HoneyPotAdmin"
            }
        ],
        "htmlContent": "<html><body>{}</body></html>".format(message),
        "subject": "File Modification Alert"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("Email sent successfully.")
    else:
        print("Error sending email. Status code:", response.status_code)

# Define the event handler
class FileModifiedEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == FILE_PATH:
            send_email()

# Start the observer
if __name__ == '__main__':
    event_handler = FileModifiedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, FILE_PATH, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

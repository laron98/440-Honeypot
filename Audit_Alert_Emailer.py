import time
import smtplib
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Replace these variables with your own email and password
EMAIL_ADDRESS = 'Insert_Email_Here'
EMAIL_PASSWORD = 'Insert_Email_Password_Here'

# Define the path of the file you want to monitor
FILE_PATH = '/var/log/audit/audit.log'

# Define the message you want to send in the email
message = 'The file at {} has been modified.'.format(FILE_PATH)

# Define the email function
def send_email():
    msg = MIMEText(message)
    msg['Subject'] = 'File Modification Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

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

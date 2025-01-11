import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send a basic email
def send_email(to_address, subject, message):
    from_address = 'herohighping@gmail.com'  # My Email
    password = 'wmpz pfec znkq vuyf'  # My password in App Password (yung Generated)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
send_email('genjohnbrito@gmail.com', 'Test Subject', 'This is a test email.') #This is the sent messenge to the other email

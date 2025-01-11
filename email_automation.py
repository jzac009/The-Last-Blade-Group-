import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient_email, email_subject, email_body):
    """Sends an email using Gmail's SMTP server."""
    
    # Email credentials
    sender_email = 'jzac0109@gmail.com' 
    app_password = 'wpqz trez ckfu jxoq'  
    
    # Set up the email details
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = email_subject
    email_message.attach(MIMEText(email_body, 'plain'))
    
    # Connect to Gmail and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender_email, app_password)
            smtp_server.send_message(email_message)
            print(f"Email successfully sent to {recipient_email}")
    except smtplib.SMTPException as error:
        print(f"Failed to send email: {error}")

# Example usage
if __name__ == "__main__":
    recipient = 'jzac009@gmail.com'  
    subject = 'Hello from Python'
    body = 'This email was sent using Python. Have a great day!'
    send_email(recipient, subject, body)

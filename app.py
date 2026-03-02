import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email configuration
sender_email = ""
receiver_email = ""
password = ""

#Create the email content
subject = "Test Email"
body = "Hello,this is email sent from Python!"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls() #Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(sender_email, password) #log in to your email account
    server.send_message(message) #Send the email

print("Email sent successfully!")    
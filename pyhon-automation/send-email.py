import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()
conn.starttls()

conn.login("email@gmail.com", "password")

conn.sendmail("email@gmail.com",
                "email@gmail.com",
                "subject: google meeting\nHello World!")

conn.quit()





#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart

# Set up the message
#subject = "Google Meeting"
#body = "Hello,\nDo you want to do a Google Meet"
#message = MIMEMultipart()
#message["From"] = "@gmail.com"
#message["To"] = "@gmail.com"
#message["Subject"] = subject

#message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server
#with smtplib.SMTP("smtp.gmail.com", 587) as server:
 #   server.ehlo()
  #  server.starttls()

    # Login to your Gmail account
    #server.login("email@gmail.com", "password")

    # Send the email
    #server.sendmail("email@gmail.com", "email@gmail.com", message.as_string())

#print("Email sent successfully.")

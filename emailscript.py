# getpass used to make user's password invisible
# smtplib is a a library taht provided by python
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# mimetext because you will only send a text message

sender = str(input("Please input your username: "))
password = getpass.getpass('Please input your password: ')

receiver = []
relist = open ("receiver_list.txt", "r")
for i in relist:
    receiver.append(i.replace("\n", ""))
# this program will make your receiver_list.txt read as a list

message = MIMEMultipart()
message ['From'] = sender
message ['To'] = i
message ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

# we will use gmail, so the host in this script uses smtp.gmail.com
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
for email in receiver:
    server.sendmail(sender, email, message.as_string())
    print("Email has been sent to ", email)
# looping your script so that it can send a message to each recipient
server.quit()
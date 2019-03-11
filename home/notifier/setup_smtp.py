# importing smtplib since it is included in python by default

import smtplib

# setting up the server
MY_ADDRESS = "denispeterson96@gmail.com"
Passwd = "Dennis5050"
server = smtplib.SMTP(host="smtp.gmail.com", port="587")
server.starttls()
server.login(MY_ADDRESS, Passwd)

# importing the necessary modules /Packages
from . import setup_smtp
from . import read_template
from . import read_contacts
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# read contacts
names, emails = read_contacts.get_contacts('mycontacts.txt')

message_template = read_template.read_template('message.txt')


def send_mail(games):
    # for each contact send email
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # adding the actual person name to the message template

        message = message_template.substitute(PERSON_NAME=name, GAMES=games)

        # setting the parameters of the message
        msg['From'] = setup_smtp.MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Error Reporting TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # sending the message via the server set up earlier
        setup_smtp.server.send_message(msg)

        del msg
        # Terminate the SMTP session and close the connection
        print("Message sent successfully")
        setup_smtp.server.quit()

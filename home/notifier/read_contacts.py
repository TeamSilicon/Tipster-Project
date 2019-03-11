# Function to read the contacts from a given contact file and return a
# list of names and email addresses
import os
from django.conf import settings


def get_contacts(filename):
    file_path = os.path.join(settings.STATIC_ROOT, filename)
    names = []
    emails = []
    contact_file = open(file_path, mode='r', encoding='utf-8')
    for each in contact_file:
        names.append(each.split()[0])
        emails.append(each.split()[1])

    return names, emails

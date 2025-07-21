import os


def email_list():
    path = 'data/emails.txt'
    with open(path , 'r') as file:
        email = file.readlines()
        return email
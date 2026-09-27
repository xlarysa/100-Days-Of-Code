import smtplib
import datetime as dt
import random as rd
my_email = "darren.bernhard@ethereal.email"
my_password = "X6RhkhckEvAsHaBpSk"

now = dt.datetime.now()
curr_day = now.weekday()

if curr_day == 3:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = rd.choice(quotes)
    with smtplib.SMTP('smtp.ethereal.email', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"Subject:Motivational Quote of the day!\n\n{quote}" )

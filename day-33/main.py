import requests
from datetime import datetime
import smtplib
from time import sleep

MY_LAT = 0.7634 #50.064651 # Cracow latitude
MY_LONG = 166.8081 #19.944981 # Cracow longitude
MY_EMAIL = "caleigh.goodwin@ethereal.email" #testing credentials from ethereal.email
MY_PASSWORD = "XxG5F5NdGbJtReukXu"

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT > iss_latitude + 5 or MY_LAT < iss_latitude - 5 and MY_LONG > iss_longitude + 5 or MY_LONG < iss_longitude - 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["sunrise"][11:13])
    sunset = int(data["sunset"][11:13])

    time_now = datetime.now()
    curr_hour = time_now.hour
    return curr_hour > sunset or curr_hour < sunrise

while True:
    if is_close() and is_dark():
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Look up!\n\nThe ISS is currently above you in the sky." )
    sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




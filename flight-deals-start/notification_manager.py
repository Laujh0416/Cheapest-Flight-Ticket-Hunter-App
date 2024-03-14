import smtplib

class NotificationManager:
    def __init__(self, sender_email, password, receiver_email, msg):
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=sender_email, password=password)
        emote = "🛩️"
        self.connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=f"Subject: The CHEAPEST price for your flight{emote}\n\n{msg} ".encode("utf-8"))
        self.connection.close()
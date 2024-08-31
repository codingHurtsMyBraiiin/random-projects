from email.message import EmailMessage
import ssl, smtplib

email_sender = ""  #your email address here
email_password = "" #watch this video to learn more: https://www.youtube.com/watch?v=pdy3nh1tn6I
email_reciever = "" #email address of the person you want to send it to
subject = "This text is automated"
body = """
Head over to https://www.youtube.com/watch?v=pdy3nh1tn6I to learn more.

"""

while True:   
    em = EmailMessage()
    em["from"] = email_sender
    em["to"] = email_reciever
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
def email_script(receiver_email,msg):
    import os
    import smtplib
    import imghdr
    from email.message import EmailMessage

    smtp_server = 'smtp.gmail.com'
    port = 465 
    sender_email = os.environ.get("Email_User")
    sender_password = os.environ.get("Email_Pass")

    msg = EmailMessage()
    msg['Subject'] = 'Holiday Reminder'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(msg)

    with smtplib.SMTP_SSL(smtp_server, port) as smtp:   

        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)   #sending Email
    







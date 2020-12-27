def email_script():
    import os
    import smtplib
    import imghdr
    from email.message import EmailMessage

    smtp_server = 'smtp.gmail.com'
    port = 465 
    sender_email = os.environ.get("Email_User")
    sender_password = os.environ.get("Email_Pass")
    receiver_email = 'koushik.dey8790@gmail.com'

    msg = EmailMessage()
    msg['Subject'] = 'Holiday Reminder'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content("For which event you want to get a reminder?")

    #with open("Screenshot 2020-12-26 200042.png", "rb") as f:
    #file_data = f.read()
    #file_type = imghdr.what(f.name)
    #file_name = f.name

    #msg.add_attachment(file_data, maintype= 'image', subtype = file_type, filename = file_name )

    with smtplib.SMTP_SSL(smtp_server, port) as smtp:   
        #smtp.ehlo()     #elho method identified ourselves to the mail server
        #smtp.starttls() #Encrypt our traffic
        #smtp.ehlo()     #reindentified ourseleves as a encrypted connection

        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)   #sending Email

email_script()    







import smtplib
from tkinter import E


## Fill this part, we can use a input instead for add customizable sender / receiver & also subjects and text.
sender =  "you@gmail.com"
receiver = "receiver@gmail.com"
password =  "password"
subject = "Subject"
text =  "Body"



## Form for the message, just like a template pretty much
message = f""""From: Test{sender}
To: Test{receiver}
Subject:{subject}\n
{body}
"""

##This is the important part as well, we choose what server to use and what port, in this case 587 but you can use any other SMTP available port.
server = smtplib.SMTP("smtplib@gmail.com", 587)
## Important, so emails are being send encrypted and nobody can snitch around on what is inside.
server.starttls()

## Pretty much the end of the code, login details and also the final message that we wanna send with our early inputs in the code.
## prints are not necessary at all but are useful to let know the client or whoever is using the code if they logged correctly but also if they sent the email or not

try:
    server.login(sender,password)
    print("Login succesful!")
    server.sendmail(sender,receiver,message)
    print("Email has been sent successfully")

except smtplib.smtplib.SMTPAuthenticationError:
    print("Sign in error, unable to login.")





import os
user=input("What is your email address?\n> ")
password = input("What is your password? (This will be cleared from the terminal.)\n> ")
os.system('cls' if os.name == 'nt' else 'clear')
toSendTo=input("What email address is this for?\n> ")
messageSubject=input("What is the subject?\n> ")
messageText=input("What is the text?\n> ")
finalConstructed=f"Subject:{messageSubject}\n\n{messageText}"
os.system('cls' if os.name == 'nt' else 'clear')
print("Working...")
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = user

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, toSendTo, finalConstructed)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
import smtplib
 
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'plant.nanny.alerts@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'Balk5610,'  #change this to match your gmail password
 
class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
 

if __name__ == '__main__':
    sender = Emailer()
    
    sendTo = 'lgb0020@gmail.com'
    emailSubject = "Testing Email Functionality"
    emailContent = "This is a test of my Emailer Class"
    
    #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
    sender.sendmail(sendTo, emailSubject, emailContent) 
import sendgrid
from elasticsearch import Elasticsearch
import time
mail = sendgrid.SendGridAPIClient('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')

esconnector = Elasticsearch(
  "http://10.97.252.29:31102/")

   
message = sendgrid.Mail(
                from_email='harinath.kavuri@gmail.com',
                to_emails='anandsadhu@perigorddata.com',
                subject='PM Elastic DB Down',
                html_content='<strong>Elastic DB Down</strong>')

#response = client1.send(message)

while True:
    time.sleep(10)
    try:
       esconnector.info()
       print("Connected")
       continue    
    except:
       print("Error an expectional")
       response = mail.send(message)
    break

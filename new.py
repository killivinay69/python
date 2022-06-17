import sendgrid
from elasticsearch import Elasticsearch
import time
mail = sendgrid.SendGridAPIClient('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')

esconnector = Elasticsearch(
  "http://10.97.252.29:31102/")

   
message = sendgrid.Mail(
                from_email='harinath.kavuri@perigorddata.com',
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

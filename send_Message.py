from telesign.messaging import MessagingClient
import os

def send(message, taskNum):
    numbers = ["16786634141", "17707560467"]
    customer_id = os.getenv('CUSTOMER_ID', 'EC06F41C-05C8-4F00-BFD4-C90D972C6A40')
    api_key = os.getenv('API_KEY','762VIC8WBw4mEAapAGuzm+IV0ER7wdqrKTxdATttf4F2dufSsxr61XxjusIflmgOj4Lcl7FtaHBZTKxgm/sMFQ==')


    phone_number = os.getenv('PHONE_NUMBER', numbers[taskNum])

    message_type = "ARN"


    messaging = MessagingClient(customer_id, api_key)

    response = messaging.message(phone_number, message, message_type)

    print(f"\nResponse:\n{response.body}\n")

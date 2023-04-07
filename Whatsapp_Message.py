from twilio.rest import Client

account_sid = 'AC712ec08d3f41135602cb19fdd937f9f9'
auth_token = '25595a768ba7f7cba380b0ef40c046cd'


whatsapp_from = 'whatsapp:+14155238886'
whatsapp_to = 'whatsapp:+919110484895'

# Message body
message_body = 'Hello, this is a forwarded message!'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body=message_body,
    from_=whatsapp_from,
    to=whatsapp_to
)

# Print message SID on successful send
print(f"Message sent successfully. SID: {message.sid}")
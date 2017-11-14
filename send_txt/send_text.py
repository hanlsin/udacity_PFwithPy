from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe1bf2fa0f7489375367fb4d5d540d99b"
# Your Auth Token from twilio.com/console
auth_token  = "9029404a5c60eaf2d78dbcb62719d16c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17706868240", 
    from_="+14049913355",
    body="Hello from Python!")

print(message.sid)
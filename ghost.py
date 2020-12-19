import amino

email = "luxarcadia328@gmail.com"  # Set your own password here!
password = "sagar890@"  # Set your own password here!
cid = "226547416"  # Community ID

client = amino.Client()
client.login(email=email, password=password)
print("Bot logged in")
sub = amino.SubClient(comId=cid, profile=client.profile)
print("Bot logged onto the community, id:", cid, "\nBot Name:", sub.profile.nickname)



name_pr = lambda l: ' '.join(l)
@client.callbacks.event("on_text_message")
def on_text_message(data):
  msg_1 = data.message.content
  command = msg_1.split(' ')
  params = command[1:]
  command = command[0] 
  if command == ".l":
         message = name_pr(params)
         msg = {
        'message': f"{message}",
        'chatId': data.message.chatId,
        'mentionUserIds': [data.message.author.userId],
        'messageType': 100
        }
  sub.send_message(**msg)
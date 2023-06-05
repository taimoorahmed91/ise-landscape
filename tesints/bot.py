from webexteamssdk import WebexTeamsAPI
import requests
import sys

BOT_ACCESS_TOKEN='NmM3ZjliOTMtNjkyYi00ZWI1LTliNjItOGNhNWQ3YmJkYzQ2NWM2YWY5MzItMDA3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
URL = 'https://api.ciscospark.com/v1/messages'
#MESSAGE_TEXT = 'Yo.'
MESSAGE_TEXT = sys.argv[1]



headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}

# Create a Webex Teams API object with your access token
api = WebexTeamsAPI(access_token=BOT_ACCESS_TOKEN)

# Get a list of all rooms in the account
rooms = api.rooms.list()

# Print the name and ID of each room
for room in rooms:
    print(f"Room Name: {room.title}\nRoom ID: {room.id}\n")
    post_data = {'roomId': room.id,'text': MESSAGE_TEXT}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print("New message created")
        #print(message_text)
        print("====================")
        print(response)
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)


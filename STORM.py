from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle
import sys

CLIENTS = []

for i,SESSION in enumerate(SESSIONS):
    if SESSION:
        client = Client(
            name=f"RikXSpam{i}",
            session_string=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="STORM.modules"),
        )
        CLIENTS.append(client)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("Third_DegreeTG")
            print(f"---> {i+1} Clients has been Started...")
            print(f"Started {cli.me.first_name} 🔥")
        except Exception as e:
            print(e)
            print("Exiting the Program.")
            sys.exit(1)

    print("🧑‍💻 Spam Userbots Have Been Deployed Successfully 🧑‍💻")
    idle()

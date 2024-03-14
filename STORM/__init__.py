from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY, SESSIONS
from datetime import datetime
import time
#from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
#aiosession = ClientSession()

if API_ID:
    API_ID = API_ID
else:
    print("WARNING: API ID NOT FOUND ⚡")

if API_HASH:
    API_HASH = API_HASH
else:
    print("WARNING: API HASH NOT FOUND ⚡")   

#app = Client(
#    name="app",
#    api_id=API_ID,
#    api_hash=API_HASH,
#    plugins=dict(root="STORM/modules"),
#    in_memory=True,
#)

# Initialize clients based on provided session strings
for i, session in enumerate(SESSIONS):
    if session:
        print(f"Client{i}: Found.. Starting.. 📳")
        client = Client(name=f"client{i}", api_id=API_ID, api_hash=API_HASH, session_string=str(session.strip()), plugins=dict(root="modules"))
        clients.append(client)

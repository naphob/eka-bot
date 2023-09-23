import os
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv

load_dotenv()
credential = os.getenv("FIREBASE_CREDENTIALS")
DB_URL = os.getenv("DB_URL")
UID = os.getenv("UID")
cred = credentials.Certificate(credential)
firebase_admin.initialize_app(cred, {
    'databaseURL': DB_URL,
    'databaseAuthVariableOverride' : {
        'uid' : UID
    }
})

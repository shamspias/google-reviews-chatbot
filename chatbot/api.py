from google.oauth2 import service_account
from googleapiclient.discovery import build
from config.settings import GOOGLE_API_KEY, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET


def get_mybusiness_service():
    credentials = service_account.Credentials.from_authorized_user_info(
        info={
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "api_key": GOOGLE_API_KEY,
        },
        scopes=["https://www.googleapis.com/auth/business.manage"]
    )

    return build("mybusiness", "v4", credentials=credentials)


def get_account_name(service):
    accounts = service.accounts().list().execute()
    return accounts["accounts"][0]["name"]


def get_reviews(service, account_name):
    locations = service.accounts().locations().list(parent=account_name).execute()
    location_name = locations['locations'][0]['name']

    reviews = service.accounts().locations().reviews().list(parent=location_name).execute()
    return reviews.get('reviews', [])


def generate_response_gpt3(text):
    # Call the GPT-3 API here and return the generated response
    # Use the `gpt3.py` module for GPT-3 functionality
    pass

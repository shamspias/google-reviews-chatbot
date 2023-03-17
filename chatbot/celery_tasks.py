from celery_worker import app
from .api import get_mybusiness_service, get_account_name, get_reviews, generate_response_gpt3


@app.task
def fetch_and_respond_reviews():
    service = get_mybusiness_service()
    account_name = get_account_name(service)
    reviews = get_reviews(service, account_name)

    for review in reviews:
        print(f"Review: {review['comment']}")
        response = generate_response_gpt3(review['comment'])
        print(f"Response: {response}")
        print("\n")

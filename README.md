# Google Reviews Chatbot

The Google Reviews Chatbot is an automated response system that fetches reviews from Google My Business, analyzes
sentiments using OpenAI's GPT-3, and generates appropriate responses. It uses Celery for task scheduling and can be
deployed on AWS using Elastic Beanstalk, EC2, and ElastiCache for Redis.

## Request Access Google My Business
Click [here](https://docs.google.com/forms/d/e/1FAIpQLSfC_FKSWzbSae_5rOpgwFeIUzXUF1JCQnlsZM_gC1I2UHjA3w/viewform) to apply for access to Google My Business API.

## Installation

- Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
- Set up the environment variables in the `.env` file:
    ```
    GOOGLE_API_KEY=your_google_api_key
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    OPENAI_API_KEY=your_openai_api_key
    REDIS_URL=redis://your_redis_server:port/db
    ```

## Usage

- Run the chatbot locally:
    ```
    python google_reviews_chatbot.py
    ```
- Run Celery worker for task scheduling:
    ```
    celery -A celery_worker worker --loglevel=info
    ```
- Run Celery beat for periodic task execution:
  ```
  celery -A celery_worker beat --loglevel=info
  ```

## Dashboard for Google Reviews Chatbot

The dashboard for the Google Reviews Chatbot is [Here](https://github.com/shamspias/google-review-chatbot-dashboard). It
is built using Django Rest.

## Deployment on AWS

Follow the steps in the deployment guide to deploy the Google Reviews Chatbot on AWS using Elastic Beanstalk, EC2, and
ElastiCache for Redis.


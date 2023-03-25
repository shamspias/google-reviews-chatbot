# chatbot/routes.py
from flask import Flask, request, jsonify
from .api import get_mybusiness_service, get_account_name, get_reviews
from .gpt3 import generate_response_gpt3

app = Flask(__name__)

@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    service = get_mybusiness_service()
    account_name = get_account_name(service)
    reviews = get_reviews(service, account_name)
    return jsonify(reviews)

@app.route('/generate-response', methods=['POST'])
def generate_response():
    user_input = request.json.get('user_input', '')
    response = generate_response_gpt3(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

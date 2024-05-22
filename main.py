from flask import Flask, jsonify
from flask import render_template
from flask import request

import logging

from openai_chat import send_message_to_openai

app = Flask(__name__)
chat_history = []


# loading chat client
@app.route('/')
def chat():
    return render_template('chat.html')


@app.route('/message', methods=['POST'])
def message():
    user_input = request.json['message']
    # 実際にはここでOpenAIのAPIにリクエストを送り、応答を得る
    response = send_message_to_openai(user_input)
    return jsonify({'message': response})


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s")
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()

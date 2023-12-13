import os
import logging
from flask import Flask, json, request, jsonify
from flask_cors import CORS
import requests
from collections import namedtuple

app = Flask(__name__)
CORS(app)

app.debug = True
logging.basicConfig(level=logging.INFO)

api_url = os.getenv("HERCAI_API_URL", "https://hercai.onrender.com/v3-beta/hercai")

Response = namedtuple('Response', 'content accuracy error')


def generate_response(user_input: str) -> Response:
    user_input = user_input.lower()
    response = requests.get(f"{api_url}?question={user_input}")

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        return Response(None, 0, f"Request Error: {err}")

    if response.status_code == 200:
        response_data = json.loads(response.text)

        if response_data.get("status") == 404:
            return Response(None, 0, "Pertanyaan tidak boleh kosong")

        error_message = response_data.get("error", None)

        if error_message is not None:
            return Response(None, 0, error_message)
        else:
            return Response(response_data.get("reply", None), 1, None)
    else:
        return Response(None, 0, "Tidak dapat mengambil respons")


@app.route('/')
def index():
    return '<h1>Halaman Utama</h1>'


@app.route('/api', methods=['GET', 'POST'])
def api():
    try:
        if request.method == 'GET':
            user_input = request.args.get('message')
        elif request.method == 'POST':
            user_input = request.json.get('message')
        else:
            return jsonify({'error': f'Method {request.method} not supported'}), 405

        if not user_input:
            return jsonify({'error': 'Parameter "message" tidak valid'}), 400

        response = generate_response(user_input)

        result = {
            'response': f'{response.content}'
        }

        return jsonify(result)

    except Exception as e:
        logging.error(f'Error dalam mengelola permintaan: {str(e)}')
        return jsonify({'error': 'Terjadi kesalahan dalam mengelola permintaan'}), 500


if __name__ == '__main__':
    app.run()

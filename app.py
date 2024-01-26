
                    # import os
# import logging
# from flask import Flask, json, request, jsonify
# from flask_cors import CORS
# import requests
# from collections import namedtuple

# app = Flask(__name__)
# CORS(app)

# app.debug = True
# logging.basicConfig(level=logging.INFO)

# data_json_path = os.getenv("DATA_JSON_PATH", "data.json")  

# Response = namedtuple('Response', 'content accuracy error')


# def load_data_json():
#     with open(data_json_path, "r") as f:
#         data = json.load(f)
#     return data


# def generate_response(user_input: str) -> Response:
#     data = load_data_json()
#     for entry in data["data"]:
#         if entry["words"].lower() in user_input.lower().split():
#             return Response(entry["answer"], 1, None)

#     return Response(None, 0, "Tidak ditemukan jawaban yang sesuai")



# # ... (REST of your code remains the same)



# @app.route('/')
# def index():
#     return '<h1>Halaman Utama</h1>'


# @app.route('/api', methods=['GET', 'POST'])
# def api():
#     try:
#         if request.method == 'GET':
#             user_input = request.args.get('message')
#         elif request.method == 'POST':
#             user_input = request.json.get('message')
#         else:
#             return jsonify({'error': f'Method {request.method} not supported'}), 405

#         if not user_input:
#             return jsonify({'error': 'Parameter "message" tidak valid'}), 400

#         response = generate_response(user_input)

#         result = {
#             'response': f'{response.content}'
#         }

#         return jsonify(result)

#     except Exception as e:
#         logging.error(f'Error dalam mengelola permintaan: {str(e)}')
#         return jsonify({'error': 'Terjadi kesalahan dalam mengelola permintaan'}), 500


# if __name__ == '__main__':
#     app.run()
   
    # kode dengan nlp tapi tidak ada respon
# import os
# import logging
# from flask import Flask, json, request, jsonify
# from flask_cors import CORS
# import requests
# from collections import namedtuple
# import spacy

# app = Flask(__name__)
# CORS(app)

# app.debug = True
# logging.basicConfig(level=logging.INFO)

# data_json_path = os.getenv("DATA_JSON_PATH", "data.json")  

# Response = namedtuple('Response', 'content accuracy error')

# nlp = spacy.load("en_core_web_sm")  # Load the spaCy model

# def load_data_json():
#     with open(data_json_path, "r") as f:
#         data = json.load(f)
#     return data

# def generate_response(user_input: str) -> Response:
#     doc = nlp(user_input)

#     # Analisis NLP dengan spaCy

#     # Temukan kata kunci atau maksud pengguna
#     keywords = [token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
#     intent = "greeting" if "hello" in keywords else "question"

#     # Cari jawaban berdasarkan kata kunci atau maksud pengguna
#     answer = None
#     for entry in data["data"]:
#         if intent == entry["intent"] and any(keyword in entry["keywords"] for keyword in keywords):
#             answer = entry["answer"]
#             break

#     # Jika tidak ditemukan jawaban yang sesuai, gunakan data.json
#     if not answer:
#         data = load_data_json()
#         for entry in data["data"]:
#             if entry["words"].lower() in user_input.lower().split():
#                 answer = entry["answer"]
#                 break

#     return Response(answer, 1 if answer else 0, None)

# @app.route('/')
# def index():
#     return '<h1>Halaman Utama</h1>'

# @app.route('/api', methods=['GET', 'POST'])
# def api():
#     try:
#         if request.method == 'GET':
#             user_input = request.args.get('message')
#         elif request.method == 'POST':
#             user_input = request.json.get('message')
#         else:
#             return jsonify({'error': f'Method {request.method} not supported'}), 405

#         if not user_input:
#             return jsonify({'error': 'Parameter "message" tidak valid'}), 400

#         response = generate_response(user_input)

#         result = {
#             'response': f'{response.content}'
#         }

#         return jsonify(result)

#     except Exception as e:
#         logging.error(f'Error dalam mengelola permintaan: {str(e)}')
#         return jsonify({'error': 'Terjadi kesalahan dalam mengelola permintaan'}), 500

# if __name__ == '__main__':
#     app.run()

# kode ke dua berhasil tapi tidak bisa mendeteksi


# import os
# import logging
# from flask import Flask, json, request, jsonify
# from flask_cors import CORS
# import requests
# from collections import namedtuple
# import spacy
# import json

# app = Flask(__name__)
# CORS(app)

# app.debug = True
# logging.basicConfig(level=logging.INFO)

# data_json_path = os.getenv("DATA_JSON_PATH", "data.json")  

# Response = namedtuple('Response', 'content accuracy error')

# nlp = spacy.load("en_core_web_sm")  # Load the spaCy model

# def load_data_json():
#     with open(data_json_path, "r") as f:
#         data = json.load(f)
#     return data

# def generate_response(user_input: str) -> Response:
#     data = load_data_json()

#     # Analisis NLP dengan spaCy

#     # Temukan kata kunci atau maksud pengguna
#     keywords = [token.text for token in nlp(user_input) if token.pos_ in ["NOUN", "VERB", "ADJ"]]
#     intent = "greeting" if "hello" in keywords else "question"

#     # Cari jawaban berdasarkan kata kunci atau maksud pengguna
#     answer = None
#     for entry in data["data"]:
#         if intent == entry["words"] and any(keyword in entry["keywords"] for keyword in keywords):
#             answer = entry["answer"]
#             break

#     # Jika tidak ditemukan jawaban yang sesuai, gunakan data.json
#     if not answer:
#         for entry in data["data"]:
#             if entry["words"].lower() in user_input.lower():
#                 answer = entry["answer"]
#                 break

#     # Jika tidak ditemukan jawaban yang sesuai, kembalikan pesan default
#     if not answer:
#         answer = "Maaf, saya tidak mengerti pertanyaan Anda."

#     return Response(answer, 1 if answer else 0, None)

# @app.route('/')
# def index():
#     return '<h1>Halaman Utama</h1>'

# @app.route('/api', methods=['GET', 'POST'])
# def api():
#     try:
#         if request.method == 'GET':
#             user_input = request.args.get('message')
#         elif request.method == 'POST':
#             user_input = request.json.get('message')
#         else:
#             return jsonify({'error': f'Method {request.method} not supported'}), 405

#         if not user_input:
#             return jsonify({'error': 'Parameter "message" tidak valid'}), 400

#         response = generate_response(user_input)

#         result = {
#             'response': f'{response.content}'
#         }

#         return jsonify(result)

#     except Exception as e:
#         logging.error(f'Error dalam mengelola permintaan: {str(e)}')
#         return jsonify({'error': 'Terjadi kesalahan dalam mengelola permintaan'}), 500

# if __name__ == '__main__':
#     app.run()
 
# VERSI ERROR


                    # KODE FIX BOT AI



# import os
# import logging
# from flask import Flask, json, request, jsonify
# from flask_cors import CORS
# import requests
# from collections import namedtuple
# import spacy
# import json
# from fuzzywuzzy import fuzz

# app = Flask(__name__)
# CORS(app)

# app.debug = True
# logging.basicConfig(level=logging.INFO)

# data_json_path = os.getenv("DATA_JSON_PATH", "data.json")

# Response = namedtuple('Response', 'content accuracy error')

# nlp = spacy.load("en_core_web_sm") 

# def load_data_json():
#     with open(data_json_path, "r") as f:
#         data = json.load(f)
#     return data

# def generate_response(user_input: str) -> Response:
#     data = load_data_json()

   
#     keywords = [token.text for token in nlp(user_input) if token.pos_ in ["NOUN", "VERB", "ADJ"]]
#     intent = "greeting" if "hello" in keywords else "question"

#     # Cari jawaban berdasarkan kata kunci atau maksud pengguna
#     answer = None
#     best_match = None
#     best_score = 0

#     for entry in data["data"]:
      
#         if intent == entry["words"] and any(keyword in entry["keywords"] for keyword in keywords):
#             answer = entry["answer"]
#             break

       
#         score = fuzz.partial_ratio(user_input.lower(), entry["words"].lower())
#         if score > best_score:
#             best_score = score
#             best_match = entry["answer"]

   
#     if not answer:
#         answer = best_match

   
#     if not answer:
#         answer = "Maaf, saya tidak mengerti pertanyaan Anda."

#     return Response(answer, 1 if answer else 0, None)




# @app.route('/')
# def index():
#     return '<h1>Halaman Utama</h1>'

# @app.route('/api', methods=['GET', 'POST'])
# def api():
#     try:
#         if request.method == 'GET':
#             user_input = request.args.get('message')
#         elif request.method == 'POST':
#             user_input = request.json.get('message')
#         else:
#             return jsonify({'error': f'Method {request.method} not supported'}), 405

#         if not user_input:
#             return jsonify({'error': 'Parameter "message" tidak valid'}), 400

#         response = generate_response(user_input)

#         result = {
#             'response': f'{response.content}'
#         }

#         return jsonify(result)

#     except Exception as e:
#         logging.error(f'Error dalam mengelola permintaan: {str(e)}')
#         return jsonify({'error': 'Terjadi kesalahan dalam mengelola permintaan'}), 500

# if __name__ == '__main__':
#     app.run()
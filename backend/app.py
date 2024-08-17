from flask import Flask, request, jsonify
from main import create_rag_instance
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

rag_model = create_rag_instance()

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = rag_model.ask(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
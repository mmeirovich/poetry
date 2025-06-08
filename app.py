from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

def run_crew(topic):
    """
    Simulates processing the topic and returns a result.
    Replace this with your actual logic.
    """
    # Example processing logic
    result = f"Processed topic: {topic}"
    return result

@app.route('/process-topic', methods=['POST'])
def process_topic():
    """
    Endpoint to process a topic and return the result.
    """
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({'error': 'Missing "topic" in request body'}), 400

    topic = data['topic']
    result = run_crew(topic)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
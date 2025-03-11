import asyncio
from flask import Flask, request, jsonify
from app.agent.manus import Manus
from app.logger import logger

app = Flask(__name__)
manus_agent = Manus()

@app.route('/api/prompt', methods=['POST'])
def handle_prompt_sync():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing prompt in request'}), 400

    prompt_text = data['prompt']
    logger.info("Received prompt: %s", prompt_text)
    
    try:
        # Create a new event loop to run the async method synchronously.
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(manus_agent.run(prompt_text))
        loop.close()
        return jsonify({'response': result})
    except Exception as e:
        logger.error("Error processing prompt: %s", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

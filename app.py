# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from transformers import pipeline
# # import requests

# # app = Flask(__name__)
# # CORS(app)

# # # Load the pre-trained question-answering pipeline
# # model_name = "distilbert-base-cased-distilled-squad"
# # qa_pipeline = pipeline("question-answering", model=model_name)

# # # Set up Gemini API key directly
# # gemini_api_key = "AIzaSyDZkUnZtpZze0IprZiwT8vq-3ibGSSP6kE"  # Replace with your actual Gemini API key

# # def initialize_pipeline():

# #     generator = pipeline('text-generation', model='distilgpt2')
# #     return generator

# # def answer_question(generator, question):
  
# #     response = generator(question, num_return_sequences=1)
# #     answer = response[0]['generated_text']
# #     return answer


# # def handle_file_content(text, question):
# #     result = qa_pipeline(question=question, context=text)
# #     confidence_threshold = 0.001  # Set your confidence threshold here
# #     print(result['score'])
# #     if result['score'] < confidence_threshold:
# #         # Fallback to Gemini API if confidence is low
# #         try:
# #             generator = initialize_pipeline()
# #             result = answer_question(generator, question)
# #             '''headers = {
# #                 "Authorization": f"Bearer {gemini_api_key}",
# #                 "Content-Type": "application/json"
# #             }
# #             data = {
# #                 "model": "gemini-model-name",  # Replace with the actual model name
# #                 "messages": [
# #                     {"role": "system", "content": "You are a helpful assistant."},
# #                     {"role": "user", "content": f"Context: {text}\nQuestion: {question}"}
# #                 ]
# #             }
# #             response = requests.post("https://gemini.googleapis.com/v1/generate", headers=headers, json=data)
# #             response.raise_for_status()
# #             gpt_answer = response.json()['choices'][0]['message']['content'].strip()
# #             return gpt_answer
# #             '''
# #         except Exception as e:
# #             return f"Error in fetching answer : {e}"

# #     return result['answer']

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     data = request.get_json()
# #     text = data.get('text')
# #     question = data.get('additional')
# #     if text and question:
# #         answer = handle_file_content(text, question)
# #         return jsonify({"answer": answer}), 200
# #     return jsonify({"message": "No file content or question received"}), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)
    

# # '''
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from transformers import pipeline

# # app = Flask(__name__)
# # CORS(app)

# # # Load the pre-trained question-answering pipeline with explicit model name and revision
# # model_name = "distilbert-base-cased-distilled-squad"
# # qa_pipeline = pipeline("question-answering", model=model_name)

# # def handle_file_content(text, question):
# #     answer = qa_pipeline(question=question, context=text)
# #     return answer['answer']

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     data = request.get_json()
# #     text = data.get('text')
# #     question = data.get('additional')
# #     if text and question:
# #         answer = handle_file_content(text, question)
# #         return jsonify({"answer": answer}), 200
# #     return jsonify({"message": "No file content or question received"}), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)
# # '''
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from transformers import pipeline

# app = Flask(__name__)
# CORS(app)

# # Load the text generation pipeline with the GPT-2 model
# generator = pipeline('text-generation', model='gpt2')

# def generate_text(prompt):
#     response = generator(prompt, max_length=50, num_return_sequences=1)  # Adjust max_length as needed
#     return response[0]['generated_text']

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     data = request.get_json()
#     text = data.get('text')
#     question = data.get('additional')
    
#     if not text:
#         return jsonify({"message": "No text content received"}), 400
    
#     if not question:
#         return jsonify({"message": "No question received"}), 400

#     try:
#         # Combine the context and question as the prompt for text generation
#         prompt = f"Context: {text}\nQuestion: {question}"
#         answer = generate_text(prompt)
#         return jsonify({"answer": answer}), 200
#     except Exception as e:
#         return jsonify({"message": f"Error processing the request: {e}"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load the text generation pipeline with the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    response = generator(prompt, max_new_tokens=30, num_return_sequences=1, pad_token_id=50256)
    return response[0]['generated_text']

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    text = data.get('text')
    question = data.get('additional')
    
    if not text:
        return jsonify({"message": "No text content received"}), 400
    
    if not question:
        return jsonify({"message": "No question received"}), 400

    try:
        # Combine the context and question as the prompt for text generation
        prompt = f"Context: {text}\nQuestion: {question}"
        answer = generate_text(prompt)
        return jsonify({"answer": answer}), 200
    except Exception as e:
        return jsonify({"message": f"Error processing the request: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

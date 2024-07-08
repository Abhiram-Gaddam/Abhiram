import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

model_name = "distilbert-base-cased-distilled-squad"
qa_pipeline = pipeline("question-answering", model=model_name)

location = "Chowdavaram, Guntur, Andhra Pradesh"
college_name = "R.V.R. & J.C.College of Engineering"
negative_res = ("no", "nope", "nah", "naw", "not interested", "sorry")
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
keywords = {
            'greetings': ['hello', 'hi', 'hey', 'howdy'],
            'farewells': ['goodbye', 'bye', 'see you later','take care'],
            'admission': ['admission', 'apply', 'enroll', 'application', 'entrance exam', 'eligibility'],
            'courses': ['courses', 'programs', 'degree', 'majors', 'curriculum', 'syllabus'],
            'faculty': ['faculty', 'professors', 'teachers', 'instructors', 'lecturers', 'researchers'],
            'events': ['events', 'activities', 'schedule', 'workshops', 'seminars', 'conferences'],
            'address':[location.lower()],
            'location': [location.lower()],
            'college': [college_name.lower()],
            'about': ['about', 'information', 'details', 'know more'],
            'contact': ['contact', 'reach out', 'get in touch'],
            'farewell_terms': ['thank you', 'thanks', 'appreciate', 'grateful'],
            'website_link':['link','url','website','site']
            }
responses = {
            'greetings': f"Hello! Welcome to {college_name}. How can I assist you today?",
            'farewells': f"Goodbye! Thank you for visiting {college_name}. If you have any further questions, feel free to ask!",
            'admission': f"For admission inquiries, please visit our website's admission section. You can also contact our admission office at {location}.",
            'courses': f"Chemical Engineering\n Civil Engineering\nComputer Science & Engineering\nComputer Science & Business  Systems(TCS)\nComputer Science & Engineering (DS)\nComputer Science & Engineering (AI & ML)\nComputer Science & Engineering (IoT)\nElectronics and Communication Engineering\nElectrical and Electronics Engineering\nInformation Technology\nMechanical Engineering\nChemistry\nMathematics\nHumanities\nPhysics\nComputer Applications Management Sciences .",
            'faculty': f"Our faculty comprises experienced professionals. Check the faculty section on our website for more details.",
            'events': f"We regularly organize events and activities. Visit our website for the latest updates on events happening at {college_name}.",
            'location': f"{college_name} is located in {location}.",
            'college_name': f"This is {college_name}.",
            'about': f"{college_name} is committed to providing quality education and fostering a vibrant learning community.",
            'contact': f"You can reach out to us by visiting our website or contacting us directly at {location} or Call Us: 91******",
            'farewell_terms': "You're welcome! If you need further assistance, feel free to ask.",
            'website_link':"https://rvrjcce.ac.in/"
            
        }



def handle_file_content(text, question):
    answer = qa_pipeline(question=question, context=text)
    return answer['answer']

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    text = data.get('text')
    question = data.get('additional')
    
    while True:
            reply = question.lower()
            if make_exit(reply):
                print(responses['farewells'])
                break
            result=generate_response(reply,keywords)
            if result=="I'm sorry, I couldn't understand your query. Please try again." :
                break
            return jsonify({"answer": result }), 200
    if text and question:
        answer = handle_file_content(text, question)
        return jsonify({"answer": answer}), 200
    return jsonify({"message": "No file content or question received"}), 400


def greet():
        print(f"Welcome to {college_name} chatbot! How can I assist you today?")
def make_exit(reply):
        return any(reply.lower() == command for command in exit_commands)

def generate_response(query,keywords):
        for category, keywords in keywords.items():
            for keyword in keywords:
                if re.search(r'\b{}\b'.format(keyword), query, re.IGNORECASE):
                    return responses[category]
        return "I'm sorry, I couldn't understand your query. Please try again."

if __name__ == '__main__':
    app.run(debug=True)



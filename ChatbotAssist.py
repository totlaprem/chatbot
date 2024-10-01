import random
import time
import speech_recognition as sr
import pyttsx3
import setuptools

# Initialize the speech recognition and synthesis engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a dictionary of responses
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! What can I help you with?"],
    "hi": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! What can I help you with?"],
    "hey": ["Hello! How can I assist you today?", "Hi! What's on your mind?", "Hey! What can I help you with?"],
    "how are you": ["I'm doing great, thanks! How about you?", "I'm good, thanks for asking!", "I'm doing well, thanks!"],
    "what is your name": ["My name is Chatty, nice to meet you!", "I'm Chatty, your friendly chatbot!", "My name is Chatty, I'm here to help!"],
    "what can you do": ["I can assist you with a wide range of tasks, from answering questions to providing information on various topics!", "I can help you with anything from simple queries to complex tasks!", "I'm a knowledgeable chatbot, and I can assist you with many things!"],
    "default": ["I didn't quite understand that. Can you please rephrase?", "Sorry, I'm not sure what you mean. Can you explain?", "I'm not sure I understand. Can you please clarify?"],
    "goodbye": ["It was nice chatting with you! Have a great day!", "Goodbye! It was great talking to you!", "See you later! It was nice conversing with you!"],
    "bye": ["It was nice chatting with you! Have a great day!", "Goodbye! It was great talking to you!", "See you later! It was nice conversing with you!"],
    "see you later": ["It was nice chatting with you! Have a great day!", "Goodbye! It was great talking to you!", "See you later! It was nice conversing with you!"],
    "thanks": ["You're welcome! It was my pleasure to assist you!", "No problem! I'm happy to help!", "You're welcome! I'm glad I could assist you!"],
    "thank you": ["You're welcome! It was my pleasure to assist you!", "No problem! I'm happy to help!", "You're welcome! I'm glad I could assist you!"],
}

# Define a function to get a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Start the conversation
engine.say("Hello! I'm Chatty, your friendly chatbot. How can I assist you today?")
engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("You: ")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            print("You: " + user_input)
            response = get_response(user_input)
            engine.say(response)
            engine.runAndWait()
            
            # Check if the user wants to exit the conversation
            if "goodbye" in user_input.lower() or "bye" in user_input.lower() or "see you later" in user_input.lower():
                engine.say(random.choice(responses["goodbye"]))
                engine.runAndWait()
                break

            # Add a delay to make the conversation more natural
            time.sleep(0.5)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that. Can you please rephrase?")
        except sr.RequestError as e:
            print("Sorry, there was an error; {0}".format(e))
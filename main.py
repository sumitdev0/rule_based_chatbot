# Rule Based Chatbot
import datetime
import time

name = input("Enter your name : ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print(f"Good Morning {name}")
elif 11 <= presentHour <= 17:
    print(f"Good Afternoon {name}")
elif 17 <= presentHour <= 20:
    print(f"Good Evening {name}")
else:
    print(f"Good night {name}")


print(f"Hello {name}, I hope you will enjoy our first chatbot")
print("Disclaimer - It is a rule based chatbot")
print("You can ask basic questions, Type 'bye' to exit ..")

# Chatbot Memory Creation [ Dictionary of responses ]
import pyjokes
responses = {
    "hello" : "Hi, whats going on in your mind ?",
    "how are you" : "I am pretty fine, Thank you",
    "who are you" : "I am rule based and smart chatbot",
    "motivate me" : "The best motivation is that You are not a special person, wanted to be special - Compile Yourself...",
    "tell me a joke" : pyjokes.get_joke(),
    "happy" : "Great to hear that, be a happy person and live a happy live"
}

# Creating a method/function to get response of chatbot

def get_response(user_question):
    user_question = user_question.lower()
    for eachkey in responses:
        if eachkey in user_question:
            return responses[eachkey]
        
    return "I don't have the answer of your querries, I am still learning"


# Take user input
while True:
    user_input = input("Please ask your question : ")
    reply = get_response(user_input)
    time.sleep(2)
    print("Bot : ",reply)

    if "bye" in user_input.lower():
        break
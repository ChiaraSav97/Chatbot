#Application Launcher to Interact with the chatbot

__author__ = "Chiara Savoldi 5014502"

import os

from chatterbot import ChatBot
from flask import Flask, render_template, request

from initialize_chatbot import train_chatbot
from initialize_interface import create_chatbot_interface
#Next we create an instance of this class. The first argument is the name of
#the application’s module or package. I should use __name__ because '__main__' versus
# is the actual import name
chatbot = None
app = Flask(__name__, template_folder = 'Templates')

@app.route("/")
def home():
    return render_template("Cb_htmlp_exe.html")

#The request.args is bringing a "dictionary" object that it can store many elements in one single object.
@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    if not user_input:
        print('Error: ', user_input)
    if user_input == "Goodbye":
        print("Nice to meet you. It was a pleasure talking with you.")
        quit()
    return str(chatbot.get_response(user_input))
#Interface
#os.getcwd() which returns the current working directory of a process.
#The os.path.join() method in Python concatenates various path components with one directory separator (‘/’).
file_path = os.path.join(os.getcwd(), 'templates', 'Cb_htmlp_exe.html')
#print(file_path)
#Check if the file already exists.
create_chatbot_interface(file_path)

#Chatbot
chatbot = ChatBot("InfoTour")
#You can decide whether to train the bot and converse in Python or click directly on the link for the web page.
#train_chatbot(chatbot)
#Exec
if __name__ == '__main__':
    app.run()



#This method returns current working directory of a process.


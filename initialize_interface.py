#Initilization of the html code of the chatbot interface.

__author__ = "Chiara Savoldi 5014502"

import os

#I have produced the HTML home page of my Chatbot.
def produce_chatbot_hp(filename):
    with open(filename, "w") as f:
        print("Creating the file...")
        html_text = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="../static/style.css">
            <body>
                <p class="mainText"><span>I present my first ChatBot, whose name is InfoTour:</span></p>
                <p class="mainText">
            <span>It can gives you information about tourist attraction, public trasport and restaurants...</span></p>
            <div id="chatbot">
                <div id="chatbox">
                <p class="botText"><span>I'm in Infotour. Tell me what you need and I'll be happy to answer! To exit write Goodbye.</span>
                </p>
            </div>
            <div id="userInput">
                <input id="textInput" type="text" name="msg" placeholder="Message">
                <input id="buttonInput" type="submit" value="Send">
            </div>
            </div>
            </div>
                <p class="mainText"><span>Where are you? London or Paris?</span></p>
                <p class="mainText"><span><a href="https://en.wikipedia.org/wiki/London">All about London.</a></span></p>
                <p class="mainText"><span><a href="https://en.wikipedia.org/wiki/Paris">All about Paris.</a></span></p>
            </body>
        </html>
            """
        f.write(html_text)
        print("Successfully created!")
        f.close()

#The function has the purpose of check whether at the specified path is an existing regular file or not.
def create_chatbot_interface(file_path):
    if not os.path.isfile(file_path):
        produce_chatbot_hp(file_path)
    else:
        print("The file already exists")

#Main
#It is better to create the file in the folder 'templates', in order to fell the css style.
create_chatbot_interface('cb_starting_htmlp.html')




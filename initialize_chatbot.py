#Initilization of the instance of the chatbot service.

__author__ = "Chiara Savoldi 5014502"

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from conversations import CONVERSATIONS

default_msg = "I'm in Infotour. Tell me what you need and I'll be happy to answer! To exit write Goodbye."
default_msg_gb = "Goodbye, see you next time!"

#ALTERNATIVE 1: I use a while loop, until the person who's talking on my Chatbot write 'Goodbye'
#print("I'm in Infotour. Tell me what you need and I'll be happy to answer! To exit write Goodbye.")
#I want to save every conversation with my Chatbot.
def start_conversation(chatbot):
    with open("SavedConversation.txt", "w") as f:
        print(default_msg)
        f.write(f"Chatbot: {default_msg}")
        chat = True
        while chat:
            user_input = input("You: ")
            response = chatbot.get_response(user_input)
            if user_input.lower() != 'goodbye':
                print("Infotour:", response)
                f.write("\n")
                f.write(f"User: {user_input}")
                f.write("\n")
                f.write(f"Chatbot:{response}")
                f.write("\n")
            else:
                chat = False
        f.write(f"Chatbot: {default_msg_gb}")
    print(default_msg_gb)
    f.close()
#ALTERNATIVE 2: WITH TRY/EXCEPT STATEMENT
    #bool = True
#while bool:
#    try:
#        user_input = input("You: ")
#        response = chatbot.get_response(user_input)
#        print("Infotour:", response)
# Press something on the keyboard to exit (for example CRTL + D)
#    except(KeyboardInterrupt, EOFError, SystemExit):
#        print("Infotour: Goodbye, see you next time!")
#        break #For making sure that the program stops


def train_chatbot(chatbot):
    # Train with general corpus. It will give more conversation to the chatbot.
    # trainer = ChatterBotCorpusTrainer(chatbot)
    # trainer.train("chatterbot.corpus.english")

    # Train with specific corpus:
    trainer = ListTrainer(chatbot)
    for conv in CONVERSATIONS:
        trainer.train(conv)

#MAIN
chatbot = ChatBot("InfoTour")

#I can specify some parameters, that represents the level of personal customization: I don't use them
#for the implementation of my chatbot, but I leave them indicated. I just specify the name!
#chatbot = ChatBot("InfoTour",
     #storage_adapter = "chatterbot.storage.SQLStorageAdapter", #default
     #input_adapter = "chatterbot.input.VariableInputTypeAdapter",
     #output_adapter = "chatterbot.output.OutputAdapter" #creation and use of different databases, it receives input from different sources
     #logic_adapters=[
      #   'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
       #  'chatterbot.logic.BestMatch'
    # ]
    #Logic used to provide answers based on the input. You can use more than one adapters (some of them are already installed).
#)
#I've decided to use the simplest version. The only thing required is the name of my Chatbot.
train_chatbot(chatbot)
start_conversation(chatbot)






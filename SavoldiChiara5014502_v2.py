from nltk.chat.util import Chat, reflections
#Responses is my training list: it's a list of lists which contains possible user input and response.
responses = [
    [
        r"(.*)my name is (.*)",
        ["Hi %2, How are you today?",]
    ],
    [
        r"Hi (.*)",
        ["Hi, How are you today?",]
    ],
    [
        r"Hi (.*)",
        ["Good morning!",]
    ],
    [
        r"I'm in (London|Paris) (.*)",
        ["What a beautiful city %2 %1",]
    ],
    [
        r"(.*)Help(.*) ",
        ["I will help you! Where are you?",]
    ],
     [
        r"(.*) What's your name ?",
        ["My name is Infotour, ask me for Restaurants, tourist attractions and means of public transport",]
    ],
    [
        r"How are you (.*) ?",
        ["Fine, thanks. And you?",]
    ],
    [
        r"How are you?",
        ["Fine, thanks. And you?",]
    ],
    [
        r"What are you able to do?(.*)",
        ["if you like, I can tell you a joke!",]
    ],
    [
        r"(.*)Picadilly circus(.*)",
        ["Piccadilly Circus is a road junction and public space of London's West End in the City of Westminster. It was built in 1819 to connect Regent Street with Piccadilly ",]
    ],

    [
        r"(It's|I am|All) (ok|fine|good|)",
        ["I'm glad you're okay.",]
    ],
    [
        r"I'm in (London|Paris|)",
        ["Be careful, due to the pandemic Covid-19",]
    ],
    [
        r"(We|Ciao|Hey|hola|Guten Morgen|Hi|Hello)(.*)",
        ["I am polyglot. Hi 'You'",]
    ],
    [
        r"I'd like to go to a (.*) for having (.*)",
        ["Let's first tell me where are you",]

    ],
    [
        r"(.*)Tell me a joke (.*)",
        ["Mathematical logic exam:Professor, but am I passed or am I failed? Yes",]
    ],
    [
        r"(.*) near the London Eye",
        ["They London Eye is a cantilevered observation wheel on the South Bank of the River Thames",]
    ],
    [
        r"(.*)wow, Is it accesible? (.*)",
        ["https://www.londoneye.com/, here you can find what you need",]
    ],
    [
        r"thank you",
        ["You're welcome",]
    ],
    [
        r"thank you",
        ["something else?",]
    ],
    [
        r"quit",
        ["Bye Bye. It has been nice talking to you!",]
    ],
    [
        r"(.*)",
        ['Gladly!',]
    ],
    [
        r"I'm hungry in (Paris|Lodon)(.*)",
        ["you are in %2 or %1?",]
    ],
    [
        r"someone tell me that you can help me",
        ["where are you? I can tell you information about tourist attraction, public trasport and restaurants of Paris and London",]
    ],
    [
        r"I'm in London",
        ["London is one of the most beautiful city! You can find information about what you can do here https://visitlondon.com/?ref=header",]

    ]
]

#The first message when 'you open the chat'.
print("I'm in Infotour. Tell me what you need and I'll be happy to answer! To exit write quit.")
#Create my chatbot
chatbot = Chat(responses, reflections)
while reflections != "quit":
    chatbot.converse() #I use this functions in order to talk with the Chatbot
    break

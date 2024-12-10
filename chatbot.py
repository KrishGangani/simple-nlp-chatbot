import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I assist you today?', 'Hi! How can I help you?']),
    (r'How are you?', ['I am good, thank you for asking!', 'I am doing well, how about you?']),
    (r'What is your name?', ['I am a chatbot created by Krish.', 'You can call me your virtual assistant.']),
    (r'What can you do?', ['I can chat with you, answer basic questions, and keep you company!', 
                           'I can assist you with basic tasks and provide helpful information.']),
    (r'Tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 
                         'Why did the computer go to the doctor? Because it caught a virus!']),
    (r'What is Python?', ['Python is a versatile programming language used for web development, data analysis, AI, and more.', 
                          'Python is a popular programming language known for its simplicity and flexibility.']),
    (r'What is AI?', ['AI stands for Artificial Intelligence, the simulation of human intelligence by machines.', 
                      'AI refers to machines that can perform tasks requiring human intelligence, like learning and problem-solving.']),
    (r'What is your purpose?', ['I am here to assist and entertain you!', 
                                'My purpose is to make your day easier and more enjoyable.']),
    (r'Where are you from?', ['I exist in the digital realm, created to chat with you.', 
                              'I am from the virtual world, here to be your friendly assistant.']),
    (r'Who created you?', ['I was created by Krish, using Python and NLP techniques!', 
                           'My creator is Krish, who designed me to assist and entertain.']),
    (r'Quit', ['Goodbye! Have a nice day!', 'Take care! See you soon!']),
    (r'(.*)', ['I am sorry, I did not understand that. Can you try again?', 
               'Hmm, I am not sure about that. Could you rephrase?'])
]

def chatbot():
    print("Hello! I am a simple chatbot. Type 'Quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

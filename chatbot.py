import re
def chatbot(input):
    input = input.lower()
    if "hello" in input or "hi" in input:
        return "Hi there! How can I help you?"
    elif re.match(r"(.*)are you(.*)", input):
        return "Great,thanks!"
    elif re.match(r"(.*)a joke",input):
        return "what is the most shocking city in the world???\nElectricity"
    elif "thanks" in input or "thank you" in input:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that."

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye'or user_input.lower()=='see you':
        print("Bot: Goodbye,Have a nice day")
        break
    else:
        respond = chatbot(user_input)
        print("Bot:", respond)

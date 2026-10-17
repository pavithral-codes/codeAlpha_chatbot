def chatbot():
    print("chatbot:hello! Type bye to exit.")
    while True:
        msg=input("you:").lower()
        if msg=="hello":
            print("bot: Hii!")
        elif msg=="how are you":
            print("bot: I'm fine,thanks!")
        elif msg=="bye":
            print("bot:Goodbye!")
            break
        else:
            print("bot: sorry,i don't understand.")

chatbot()
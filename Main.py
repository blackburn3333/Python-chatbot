

from Bot import Bot

bot =  Bot()

if __name__ == '__main__':
    print("|-------------------------------------------------------|")
    print("|\t\tWelome to XYZ Car sale\t\t\t|")
    #print("|\t\t\t\t\tXYZ Car sale\t\t\t\t\t\t|")
    print("|-------------------------------------------------------|")
    print("|XYZ BOT : Hi, how can i help you?")
    while True:
        question = input("|You : ")
        bot.process_question(question)




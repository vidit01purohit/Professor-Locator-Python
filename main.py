from chatbot import Chat
import ttabstract
from ttabstract import Ttabstract
print("BOT: Welcome to the prof-bot!")
professors = ttabstract.professors
search_is_on = True
while search_is_on:
    text = input("USER: ").lower()
    if text != 'bye':
        chat = Chat()
        # Abstracting Professor code
        if text == 'thanks' or text == 'thank you':
            search_is_on = False
            print("BOT: You are welcome...")
        else:
            if chat.greet(text) is not None:
                print("BOT: ", chat.greet(text))
            else:
                find_prof_name = chat.response(text)
                if find_prof_name not in ttabstract.professors:
                    print("BOT: ", find_prof_name)
                else:
                    tt = Ttabstract(find_prof_name)
                    tt.getdetails()

        print("BOT: Do you want to search more? (Yes/No) ")
        ask_user = input("USER: ").lower()
        if ask_user == 'no':
            search_is_on = False
        else:
            print("BOT: Search is on!")
    else:
        print("BOT: Thank you!")
        search_is_on = False
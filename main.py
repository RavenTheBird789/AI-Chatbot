# Main file for Chatbot

import time
import sys
import os
import new_word
import new_sound
import new_place

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def user_prompt():
    prompt = input(green("Would you like to return to the main menu? (yes/no): "))
    if prompt == "yes":
        os.system('clear')
        options()
    elif prompt == "no":
        os.system('clear')
        print(green("Okay then! thanks for teaching me things!"))
        time.sleep(5)
        os.system('clear')
        return;

art = """
   *%@@@@%%#
 *%@@@%@@@%%*
%@@%=*%@#**=**
%@@@@@@#*+.-*+
%%%@@%%#%*.+*
%@%%+:-: .+* 
#@%-: ..=*#+:  
=#+::.::-+++*#.. 
=%@%#+=+--+*%%=-*
*%%%%+*+--+%+#+#%
*%@@@%#====**##@@
*%%%%%%-+-:=-+#@@
+%%%%%#==-:..:%@@
+%%%%%%==:.:.:*%@
*%%%%%%=-:::.:.*%
*%%%%%%#+::.:.:.:*"""

print(green(art));

text = "\nHi there! my name is Jaleigha. \nI'm an AI chatbot that can be trained with data of your choosing. \nWhat would you like to teach me?\n"
for char in text:
    sys.stdout.write(green(char))
    sys.stdout.flush()
    time.sleep(0.1)

def options():
    space = " "
    print(space)
    space = space * 6
    print(bold(green(space + "Options")))
    print(green("==================="))
    print(bold(red("By: RavenTheBird789")))
    print(green("==================="))
    print(green("1. Teach me a word"))
    print(green("2. Teach me a sound"))
    print(green("3. Teach me a place"))
    print(green("4. Exit"))
    selection = input(green("Please select an option: "))
    if selection == '1':
        new_word.new_word();
        time.sleep(3)
        user_prompt()
        os.system('clear')
    elif selection == '2':
        new_sound.new_sound();
        time.sleep(3)
        user_prompt()
        os.system('clear')
    elif selection == '3':
        new_place.new_place();
        time.sleep(3)
        user_prompt()
        os.system('clear')
    elif selection == '4':
        os.system('clear');
        print(green("Thank you for taking the time to speak to me."));
        time.sleep(5)
        os.system('clear');
        os.close(fd=0);
    else:
        os.system('clear');
        print(red("Invalid Input, please try again."));
        time.sleep(3)
        os.system('clear');
        options();
options();

# New Word (Option 1)

import time
import os

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def word_definitions():
    query = input(green("What word would you like to know the definition of?: "))
    if query in words:
        indx = words.index(query)
        print(bold(green(f"{query}: {definitions[indx]}")))
        time.sleep(3)
        ultimatum();
    else:
        print(red("Word not found in training data"))
        time.sleep(3)
        os.system('clear')
        user_query();

def ultimatum():
    ult = input(green("Would you like to teach me more? (yes/no): "))
    if ult == "yes":
        os.system('clear')
        new_word();
    elif ult == "no":
        os.system('clear')
        print(green("Okay then!"))
        time.sleep(1)
        os.system('clear')
        round2 = input(green("Would you like to know the definition of other words? (yes/no): "))
        if round2 == "yes":
            word_definitions();
        elif round2 == "no":
            os.system('clear')
            print(green("Okay then!"))
            time.sleep(1)
            os.system('clear')
            with open("words.txt", "w") as wf:
                wf.write("\n".join(words))
            with open("word_defs.txt", "w") as df:
                df.write("\n".join(definitions))
            return;
        else:
            print(red("Invalid input, please try again."))
            time.sleep(3)
            os.system('clear')
            ultimatum();
    else:
        print(red("Invalid input, please try again."))
        time.sleep(3)
        os.system('clear')
        ultimatum();

def user_query():
        Uques = input(green("Would you like to teach me another word? (yes/no): "))
        if Uques == "yes":
            os.system('clear')
            new_word();
        elif Uques == "no":
            os.system('clear')
            word_definitions();
        else:
            print(red("Invalid input, please try again."))
            time.sleep(3)
            user_query();

words = []
definitions = []

def load_words():
    if os.path.exists("words.txt"):
        with open("words.txt", "r") as wf:
            values = [line.strip() for line in wf if line.strip()]
            if values:
                words.extend(values)

def load_definitions():
    if os.path.exists("word_defs.txt"):
        with open("word_defs.txt", "r") as df:
            values = [line.strip() for line in df if line.strip()]
            if values:
                definitions.extend(values)

def new_word():
    load_words()
    load_definitions()
    training_word = input(green("What is the word you'd like to teach me?: "))
    training_def = input(green("What is the definition of this word?: "))
    words.append(training_word)
    definitions.append(training_def)
    os.system('clear');
    user_query();

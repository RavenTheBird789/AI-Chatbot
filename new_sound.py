# New Sound (Option 2)

import time
import os

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def sound_descriptions():
    query = input(green("What sound would you like to hear an explanation of?: "))
    if query in sounds:
        indx = sounds.index(query)
        print(bold(green(f"{query}: {descriptions[indx]}")))
        time.sleep(3)
        ultimatum();
    else:
        print(red("Sound not found in training data"))
        time.sleep(3)
        os.system('clear')
        user_query();

def ultimatum():
    ult = input(green("Would you like to teach me more? (yes/no): "))
    if ult == "yes":
        os.system('clear')
        new_sound();
    elif ult == "no":
        os.system('clear')
        print(green("Okay then!"))
        time.sleep(1)
        os.system('clear')
        round2 = input(green("Would you like to know the descriptions of other sounds? (yes/no): "))
        if round2 == "yes":
            sound_descriptions();
        elif round2 == "no":
            os.system('clear')
            print(green("Okay then!"))
            time.sleep(1)
            os.system('clear')
            with open("sounds.txt", "w") as sf:
                sf.write("\n".join(sounds))
            with open("sound_descs.txt", "w") as df:
                df.write("\n".join(descriptions))
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
        Uques = input(green("Would you like to explain another sound to me? (yes/no): "))
        if Uques == "yes":
            os.system('clear')
            new_sound();
        elif Uques == "no":
            os.system('clear')
            sound_descriptions();
        else:
            print(red("Invalid input, please try again."))
            time.sleep(3)
            user_query();

sounds = []
descriptions = []

def load_sounds():
    if os.path.exists("sounds.txt"):
        with open("sounds.txt", "r") as sf:
            values = [line.strip() for line in sf if line.strip()]
            if values:
                sounds.extend(values)

def load_descriptions():
    if os.path.exists("sound_descs.txt"):
        with open("sound_descs.txt", "r") as df:
            values = [line.strip() for line in df if line.strip()]
            if values:
                descriptions.extend(values)

def new_sound():
    load_sounds()
    load_descriptions()
    training_sound = input(green("What is the sound you'd like to teach me?: "))
    training_desc = input(green("What is a good description of this sound?: "))
    sounds.append(training_sound)
    descriptions.append(training_desc)
    os.system('clear');
    user_query();

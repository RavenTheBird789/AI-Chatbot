# New Place (Option 3)

import time
import os

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def location_descriptions():
    query = input(green("What place would you like to hear an explanation of?: "))
    if query in places:
        indx = places.index(query)
        print(bold(green(f"{query}: {descriptions[indx]}")))
        time.sleep(3)
        ultimatum();
    else:
        print(red("Place not found in training data"))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        user_query();

def ultimatum():
    ult = input(green("Would you like to teach me more? (yes/no): "))
    if ult == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        new_place();
    elif ult == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(green("Okay then!"))
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        round2 = input(green("Would you like to know the descriptions of other places? (yes/no): "))
        if round2 == "yes":
            location_descriptions();
        elif round2 == "no":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(green("Okay then!"))
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            with open("places.txt", "w") as pf:
                pf.write("\n".join(places))
            with open("place_descs.txt", "w") as df:
                df.write("\n".join(descriptions))
            return;
        else:
            print(red("Invalid input, please try again."))
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            ultimatum();
    else:
        print(red("Invalid input, please try again."))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        ultimatum();

def user_query():
        Uques = input(green("Would you like to explain another place to me? (yes/no): "))
        if Uques == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            new_place();
        elif Uques == "no":
            os.system('cls' if os.name == 'nt' else 'clear')
            location_descriptions();
        else:
            print(red("Invalid input, please try again."))
            time.sleep(3)
            user_query();

places = []
descriptions = []

def load_places():
    if os.path.exists("places.txt"):
        with open("places.txt", "r") as pf:
            values = [line.strip() for line in pf if line.strip()]
            if values:
                places.extend(values)

def load_descriptions():
    if os.path.exists("place_descs.txt"):
        with open("place_descs.txt", "r") as df:
            values = [line.strip() for line in df if line.strip()]
            if values:
                descriptions.extend(values)

def new_place():
    load_places()
    load_descriptions()
    training_places = input(green("What is the name of the place you'd like to teach me about?: "))
    training_desc = input(green("What is a good description of this place?: "))
    places.append(training_places)
    descriptions.append(training_desc)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_query();

import re, random, colorama
from colorama import Fore, Style

#Initialize colorama for colored output
#init(autoreset=True)
colorama.init(autoreset=True)

#Destination & Joke data
destinations = {
    "beaches": ["Hawaii", "Maldives", "Bora Bora"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Tokyo", "Paris"]
}
jokes=[
    "Why don't programmers like nature? It has too many bugs.",
    "Why do travellers always carry a pencil? In case they need to draw a map!"
    "Why was the computer cold? It left its Windows open."
]

#Helper function to normalise user input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

#Provide Travel Recommendations
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities? ")
    preference = input(Fore.YELLOW + "You: ")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer=input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Great! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + f"TravelBot: No worries! How about trying a different destination?")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that type of destination." )
    
    show_help()

# Offer packaging tips based on user destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where To?")
    location= normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How long will you be there? (days)")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {location} for {days} days:")
    print(Fore.GREEN + "- Pack versatile clothing.")
    print(Fore.GREEN + "- Bring a power bank.")
    print(Fore.GREEN + "- Check the weather forecast.")

#Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

#Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Provide packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "- Exit (say 'exit')")

#Main function
def chat():
    print(Fore.CYAN + "Welcome to TravelBot! How can I assist you today?")
    name=input(Fore.YELLOW +"Your Name: ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe Travel! Goodbye!!")  
            break
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Please try again.")
            
#Run the chatbot
if __name__ == "__main__":
    chat()
                           

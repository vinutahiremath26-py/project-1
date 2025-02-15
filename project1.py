import random
import string

def load_word_lists():
    adjectives = ["mini", "Happy", "Fast", "Brave", "Clever", "Witty", "Fierce", "Bold", "Jolly", "Mighty"]
    nouns = ["Tiger", "Dragon", "Panda", "Warrior", "Eagle", "Shadow", "Storm", "Wizard", "Knight", "Hunter"]
    return adjectives, nouns

def generate_username(include_numbers=True, include_special_chars=True):
    adjectives, nouns = load_word_lists()
    
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username

def save_username(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

def main():
    print("Welcome to the Random Username Generator!")
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    username = generate_username(include_numbers, include_special_chars)
    print(f"Generated Username: {username}")
    
    save_username(username)
    print("Username saved to usernames.txt")

if __name__ == "__main__":
    main()

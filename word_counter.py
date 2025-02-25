def count_words(text):
    """
    Function to count the number of words in a given text.
    Words are considered as sequences separated by whitespace.
    """
    words = text.split()  # Splitting text into words
    return len(words)  # Returning word count


def main():
    """Main function to run the word counter program."""
    print("Welcome to the Word Counter Program!")
    user_input = input("Enter a sentence or paragraph: ").strip()

    # Error Handling: Check if input is empty
    if not user_input:
        print("Error: You entered an empty string. Please provide valid input.")
        return

    # Counting words
    word_count = count_words(user_input)

    # Displaying the result
    print(f"\nWord Count: {word_count} words")


# Run the program
if __name__ == "__main__":
    main()

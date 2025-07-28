from lib import restore_text

def main():
    """
    Main function to test the is_valid_word function.
    """
    print("Welcome to the Text Restorer!")
    text = input("Please enter the text to restore:\n\n")
    result = restore_text(text)

    if result is None:
        return
    print("Restored Text:")
    print(result)

if __name__ == "__main__":
    main()

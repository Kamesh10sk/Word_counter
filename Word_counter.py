def count_words(text: str) -> int:
    return len(text.split())
def main():
    print("Welcome to the Word Counter Program!")
    user_input = input("Please enter a sentence or paragraph: ").strip()
    if not user_input:
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")
if __name__ == "__main__":
    main()

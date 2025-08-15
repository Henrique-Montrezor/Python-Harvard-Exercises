# twttr.py

def main():
    message = input("Input: ")
    shortened_message = shorten(message)
    print(f"Output: {shortened_message}")

def shorten(word):
    shortened_word = ""
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter not in vowels:
            shortened_word += letter
    return shortened_word

if __name__ == "__main__":
    main()

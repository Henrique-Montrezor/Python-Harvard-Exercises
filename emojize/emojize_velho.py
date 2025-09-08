import emoji

def main():
    text = input()
    output = emoji.emojize(text, language='en')
    print(output)

main()

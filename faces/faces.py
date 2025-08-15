def main():

    original_text = input("")

    converted_text = convert(original_text)

    print(converted_text)

def convert(phrase):

    modified_phrase = phrase.replace(":)", "🙂")

    final_phrase = modified_phrase.replace(":(", "🙁")

    return final_phrase

main()

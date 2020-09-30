import spacy

nlp = spacy.load("en_core_web_sm")


def tokenize(text):
    doc = nlp(text)
    print("Result")
    for token in doc:
        print("Text: " + token.text + ", lemma: " + token.lemma_ + ", part of speech: " + token.pos_)


def main():
    text = input("Enter text:")
    print("\nText\n" + text)
    tokenize(text)


if __name__ == "__main__":
    main()

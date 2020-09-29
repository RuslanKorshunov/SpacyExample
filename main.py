import spacy

nlp = spacy.load("en_core_web_sm")


def tokenize(text):
    doc1 = nlp(text.decode('utf8'))
    print("Result")
    for token in doc1:
        print("Text: " + token.text + ", lemma: " + token.lemma_ + ", part of speech: " + token.pos_)


def main():
    text1 = "Apple is looking at buying U.K. startup for $25 billion dollars."
    print("Text1\n" + text1)
    tokenize(text1)

    text2 = "The drawbacks of classical mathematical logic and automated reasoning are discussed. " \
            "The difference between classical logic and human cognition is shown on simple examples. " \
            "Information granulation based on pragmatics is viewed as a principal capacity of cognitive agent."
    print("Text2\n" + text2)
    tokenize(text2)


if __name__ == "__main__":
    main()

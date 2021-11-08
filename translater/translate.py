from translater.alphabet import Cyrillic


def cyrillic_to_latin_doc(doc):
    with open(doc, 'r', encoding='utf-8') as f:
        text = f.read()
        for key in Cyrillic:
            text = text.replace(key, Cyrillic[key])
        with open(doc, 'w', encoding='utf-8') as file:
            file.write(text)


def cyrillic_to_latin_text(text):
    for key in Cyrillic:
        text = text.replace(key, Cyrillic[key])
    return text

# cyrillic_to_latin_doc('../test.txt')

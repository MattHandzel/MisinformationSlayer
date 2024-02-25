import json
def load_words():
    with open("words.json", "r") as f:
        s = f.read();
        j = json.loads(s);
        return j;
def is_misinfo(phrase):
    dictionary = load_words();
    try:
        b = dictionary[phrase.lower()]
        return b
    except KeyError:
        #call chatgpt
        #update dictionary
        dictionary[phrase.lower()] = False
        with open("words.json", "w") as fi:
            d = json.dumps(dictionary);
            fi.write(d);
        return False
#if __name__ == '__main__':
#    print(is_misinfo("hi"));



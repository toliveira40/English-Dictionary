import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        for d in data:
            return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) >0:
        yn = input("Did you min %s instead ? Type y if Yes or n if No > " % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "That word doesn´t exist, please type again > "
        else:
            return "We didn´t understand your query !"
    else:
        return("That word doesn´t exist, please type again > ")

word = input("Choose word > ")
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

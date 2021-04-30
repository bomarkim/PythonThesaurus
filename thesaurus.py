#thesaurus app
#simple thesaurus application using JSON data
#uses SequenceMatcher to compare possible words via ratio
#uses get_close_matches to find nearest word

import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def findWord(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        question = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys())[0])
        if question == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif question == "N":
            return "The word does not exist. Please double check it."
        else:
            return "Query not understood."
        
    else:
        return "The word does not exist. Please double check it."

word = input("Enter a word: ")
print(findWord(word))
import json
from difflib import get_close_matches    #import to check word similarity

data = json.load(open("dictionary.json"))  #load json file

def meaning(word):
    word = word.upper()          #convert word to uper case
    if word in data:
        return data[word]         #if word exists, return meaning
    elif len(get_close_matches(word, data.keys())) > 0:     #if word not found, check for most similar word instead
        check = input("Did you mean %s instead? Enter Y for yes, N for no\n" %get_close_matches(word, data.keys())[0])   #return most similar word
        if check == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Sorry the word doesn't exist!"
    else:
        return "The word doesn't exist"

word = input("Type word ")

print(meaning(word))   #print word meaning

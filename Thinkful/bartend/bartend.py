# Bartender app. Uses dictionaries!
import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}



# Iterate through questions dictionary.. 
# write the boolean response to each question in a new dictionary
# For each true, add a random ingredient to the drinks
# return the drink

def main():
    likes = {}
    drink = []
    add_ins = []
    for key in questions:
        likes[key] = raw_input(questions[key]+ "(type 'y' if true) ")
    for key in likes:
        if likes[key] in ['y','yes']:
            drink.append(random.choice(ingredients[key]))
    if drink != []:
        print "Excellent, I'll make you a drink with: "
        print drink
    else:
        print "Well, you don't like anything. No drink for you."


if __name__ == '__main__':
    drinking = True
    while drinking == True:
        main()
        if raw_input("Would you like another drink? (y/n) ") == 'y':
            print "OK! You'll have another"
        else:
            drinking = False
    


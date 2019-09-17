# Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story, before reading the – often comical or nonsensical – story aloud.
from collections import defaultdict
import random
from colorama import Fore, Back, Style
import re 

my_dict = defaultdict(lambda:[])

# receives inputs and adds to the empty list

def add_to_story(adjective, adjective2, adjective3, noun, verb, company, pronoun):
    my_dict['Adjective'].append(adjective)
    my_dict['Noun'].append(noun)
    my_dict['Verb'].append(verb)
    my_dict['Company'].append(company)
    my_dict['Pronoun'].append(pronoun)
    my_dict['Adjective'].append(adjective2)
    my_dict['Adjective'].append(adjective3)
    my_dict['Noun'].append('Walmart')
    my_dict['Verb'].append('eats')
    my_dict['Company'].append('Google')
    my_dict['Company'].append('IBM')

# If I want to use regex instead of the try catch method then the code is below
'''
while True:
    
    adjective, adjective2, adjective3 = input('Type 3 Adjectives: ').split()
    noun = input('Type a Verb: ')
    verb = input('Type a Noun: ')
    company = input('A Company Name: ')
    pronoun = input('Type a pronoun: ')

    if not re.match("^[A-Za-z]*$", adjective, adjective2, adjective3, noun, verb, company, pronoun):
        print ("Error! Make sure you only use letters in your responses")
    else:
        pass
    break 

    
'''
# If I wanted to use Try Catch method instead of regex then the code is below
while True:

    try:
        adjective, adjective2, adjective3 = input('Type 3 Adjectives: ')
       
        noun = input('Type a noun: ')
        
        verb = input('Type a verb: ')

        company = input('A Company Name: ')

        pronoun = input('Type a pronoun: ')

        add_to_story(adjective, adjective2, adjective3, noun, verb, company, pronoun)
    except ValueError:
        
        continue
        
    else:
        # the inputs were successfully parsed so we're ready to exit the loop
        pass
    break
 
# checks length of inputs to make sure the input is long enough 
if len(adjective) and len(noun) and len(verb) and len(company) < 3:
    print('Sorry one of your words was too short. Please try again.')
else:

    pass


def story(adjective, noun, verb, company, pronoun):
    a = random.randrange(len(my_dict['Adjective'])) # random counter for adjectives
    adjective1 = my_dict['Adjective'][a]
    b = random.randrange(len(my_dict['Noun'])) # random counter for nouns
    noun1 = my_dict['Noun'][b]
    v = random.randrange(len(my_dict['Verb'])) # random counter for verbs
    verb1 = my_dict['Verb'][v]
    c = random.randrange(len(my_dict['Company'])) # counter for Company name
    company1 = my_dict['Company'][c]
    p = random.randrange(len(my_dict['Pronoun'])) # random counter for pronouns
    pronoun1 = my_dict['Pronoun'][p]
    return (Fore.BLUE + "Andy works at " + Fore.RESET + company1 + " while enjoying " + noun1 + Fore.BLUE + " when Andy " + Fore.RESET + verb1 + " during dinner. After Andy's " + adjective1 + " experience, " + pronoun1 +
      " ran back to the " + noun1 + " and went skinny dipping. Don't forget to " + verb1 + " before you go to eat " + adjective2  + noun1 + " at night. Many " + adjective3 + " people forget that they have " + Fore.LIGHTCYAN_EX +" unorthodox brains." +Fore.RESET)


print(story(adjective, noun, verb, company, pronoun))

print(my_dict)

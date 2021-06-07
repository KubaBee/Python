import random, re
from pathlib import Path

# TODO: Load random text with words to be changed

sentences = open(Path.cwd() / 'madLibs.txt')
sentences = sentences.readlines()
sentence = random.choice(sentences)
print(sentence)

# TODO: Find number of ADJ, NOUN, VERB, ADVERB occurrences and save them

adjNum = re.compile(r'ADJECTIVE')
nounNum = re.compile(r'NOUN')
verbNum = re.compile(r'VERB')

adjNum, nounNum, verbNum = (adjNum.findall(sentence), nounNum.findall(sentence), verbNum.findall(sentence))
adjNum = sum(1 for _ in adjNum)
nounNum = sum(1 for _ in nounNum)
verbNum = sum(1 for _ in verbNum)
print(adjNum, nounNum, verbNum)

adjs = []
nouns = []
verbs = []


# TODO: Ask user for them

def adding_words(v_list, quantity, name):
    for i in range(quantity):
        tmp = input(f'Pass a/an {name}: ')
        v_list.append(tmp)


adding_words(adjs, adjNum, 'adjective')
adding_words(nouns, nounNum, 'noun')
adding_words(verbs, verbNum, 'verb')


# TODO: Replace text with given words

def replace_inside(name, quantity, v_list):
    global sentence
    for i in range(quantity):
        sentence = sentence.replace(f'{name}', v_list[i], 1)


replace_inside('ADJECTIVE', adjNum, adjs)
replace_inside('NOUN', nounNum, nouns)
replace_inside('VERB', verbNum, verbs)

print(sentence)

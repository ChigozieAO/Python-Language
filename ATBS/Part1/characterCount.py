import pprint
message = 'It was a bright sunny day in africa then the fire nation attacked, they fucking rampaged'
count = {}

for character in message :
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
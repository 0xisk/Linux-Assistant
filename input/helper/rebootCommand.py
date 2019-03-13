# expectations of what the user may say in the beginning of his/her sentence
desires = ['i want to', 'i need to', 'i wish to', 'i demand to', 'i long to']

#most used of the word synonyms
rebootSynonyms = ['reboot', 'restart', 'reset', 'reestablish', 'reopen']


sentences = ['pc', 'laptop', 'computer', 'my laptop', 'machine', 'my machine', 'system',
            'the system', 'kernel']


# this for loop is for giving a direct command from the user
count = 0
for x in rebootSynonyms:
    for y in sentences:
        print(x + ' ' + y + ', reboot')
        count += 1
print(count)


# this loop is to combine each list together the form of (i want to + <the synonyms> + the rest of the sentence)
count = 0
for z in desires:
    for x in rebootSynonyms:
        for y in sentences:
            print(z + ' ' + x + ' ' + y + ', reboot')
            count += 1
print(count)


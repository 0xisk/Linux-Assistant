# expectations of what the user may say in the beginning of his/her sentence
desires = ['i want to', 'i need to', 'i wish to', 'i demand to', 'i long to']

#most used of the word synonyms
openSynonyms = ['open', 'eject', 'disclose', 'remove', 'unlock', 'uncover']

sentences = ['cd rom', 'cdrom', 'cd-rom', 'rom', 'my cd rom', 'my cdrom', 'the cd-rom', 'the rom']


# this for loop is for giving a direct command from the user
count = 0
for x in openSynonyms:
    for y in sentences:
        print(x + ' ' + y + ' ,eject')
        count += 1
print(count)


# this loop is to combine each list together the form of (i want to + <the synonyms> + the rest of the sentence)
count = 0
for z in desires:
    for x in openSynonyms:
        for y in sentences:
            print(z + ' ' + x + ' ' + y + ' ,eject')
            count += 1
print(count)


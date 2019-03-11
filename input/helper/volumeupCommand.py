# expectations of what the user may say in the beginning of his/her sentence
desires = ['i want to', 'i need to', 'i wish to', 'i demand to', 'i long to']


#most used of the word synonyms
volumeupSynonyms = ['volumeup', 'volume up', 'increase', 'boost', 'inflate', 'escalate',
                    'raise', 'rise', 'double', 'maximize', 'pulse']


sentences = ['volume', 'speaker', 'sound', 'tone']


# this for loop is for giving a direct command from the user
count = 0
for x in volumeupSynonyms:
    for y in sentences:
        print(x + ' ' + y + ', amixer -D pulse sset Master 50%+')
        count += 1
print(count)



# this loop is to combine each list together the form of (i want to + <the synonyms> + the rest of the sentence)
count = 0
for z in desires:
    for x in volumeupSynonyms:
        for y in sentences:
            print(z + ' ' + x + ' ' + y + ', amixer -D pulse sset Master 50%+')
            count += 1
print(count)


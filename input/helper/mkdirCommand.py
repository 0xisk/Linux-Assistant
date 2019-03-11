# expectations of what the user may say in the beginning of his/her sentence
desires = ['i want to', 'i need to', 'i wish to', 'i demand to', 'i long to']

#most used of the word synonyms
createSynonyms = ['create', 'make', 'build', 'generate', 'conceive', 'design', 'establish', 'form', 'initiate', 'set up', 'invent']


sentences = ['folder', 'directory', 'new folder', 'new directory',
             'a folder', 'a directory', 'a new folder', 'a new directory',
             'many folders', 'many directories', 'multiple folders', 'multiple directories',
             'different folders', 'different directories', 'various folders', 'various directories',
             'multi folders', 'multi directories', 'several folders', 'several directories',
             'mixed folders', 'mixed directories', 'collective folders', 'collective directories',
             'brand new folder', 'brand new directory',
             'brand new folders', 'brand new directories'

            ]


# this for loop is for giving a direct command from the user
count = 0
for z in desires:
    for x in createSynonyms:
        for y in sentences:
            print(z + ' ' + x + ' ' + y + ', mkdir')
            count = count + 1
print(count)
        

# this loop is to combine each list together the form of (i want to + <the synonyms> + the rest of the sentence)
count = 0
for x in createSynonyms:
    for y in sentences:
        print(x + ' ' + y + ', mkdir')
        count = count + 1
print(count)


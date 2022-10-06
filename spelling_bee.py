import os
print(os.getcwd())



def spelling_bee(all,required):
    '''
    Solve the spelling bee problem
    '''
    f = open('data/words.txt')
    line = f.readline()
    word = line.strip()
    while True:
        for line in f:
            if required in line:
                if line not in all:
                    if len(word)>3:
                        print(word)

print(spelling_bee('ahditr','b'))

        

def bad_words():
    '''
    A bad word should:
    - contain at least three letters from "covid",
    - and contain at least one letter that occurs twice in a row,
    - and have same first letter and last letter.
    '''
    f = open('data/words.txt')
    count=0
    special=['c','o','v','i','d']
    for line in f:
        word = line.strip()
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                print(word)
            elif word[i] in special:
                count+=1
        if count>=3:
            print(word)
        elif word[0]==word[-1]:
            print(word)

bad_words()
        

            

        
        

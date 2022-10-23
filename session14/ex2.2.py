f = open('data/words.txt')
for line in f:
        word = line.strip()

words = []

def file_to_wordlist():
    """
    Return a list of words from words.txt
    """
    words = []
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        words.append(word)
    return words

def sort_word(word):
    '''
    '''

print(sort_word('deltas'))

def list_to_dict(word_list):
    '''
    '''

list_for_test=[]
result=list_to_dict(list_for_test)

def dict_to_list(anagram_dict):
    '''
    '''
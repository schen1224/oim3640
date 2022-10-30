def create_dict():
    """
    Return a dictionary of words from words.txt
    """
    d = {}
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        d[word] = 1
    return d
'''
tuples as key, list can not be used
'''

def create_list():
    """
    Return a list of words from words.txt
    """
    words = []
    f = open("data/words.txt")
    for line in f:
        word = line.strip()
        words.append(word)
    return words

'''
list(d.key)
'''


def histogram(s):
    """
    Return a dict mapping letter to frequency in s
    """
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def main():
    print(histogram('bookkeeper'))


if __name__ == '__main__':
    main()


def is_reverse(word1, word2):
    """Return True if WORD2 is the reversed WORD1"""
    # if len(word1) != len(word2):
    #     return False

    # i = 0
    # j = len(word2)

    # while j > 0:
    #     if word1[i] != word2[j]:
    #         return False
    #     i = i + 1
    #     j = j - 1
    # return True

    return word1[::-1] == word2


print(is_reverse('pots', 'stop'))

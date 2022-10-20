f = open('data/words.txt')
for line in f:
        word = line.strip()


def make_anagram_dict(word):
    """change the list of words to a dictionary"""
    result = defaultdict(list)
    for letter in word:
        fp = ''.join(sorted(letter))
        result[fp].append(letter)

    result = {fp: result[fp] for fp in result if len(result[fp]) > 1}
    return result

'''
after creating the dictionary, assign key and values to words, enabling us to call a specifc anagram. And then group them together by choosing all values. 
'''


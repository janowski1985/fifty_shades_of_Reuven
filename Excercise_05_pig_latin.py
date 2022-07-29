# one word translation

def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

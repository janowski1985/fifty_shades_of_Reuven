def pig_latin():
    sentence = input("Enter a sentence you would like to translate to pig latin language: ").strip()
    
    translation = []
    
    for one_word in sentence.split():
        if one_word[0] in 'aeiou':
            translation.append(f'{one_word}way')
        else:
            translation.append(f'{one_word[1:]}{one_word[0]}ay')
            
# "space" join will join words from translation list with space as a separator

    return ' '.join(translation)

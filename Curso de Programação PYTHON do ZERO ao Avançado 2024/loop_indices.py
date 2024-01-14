def is_abcedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return
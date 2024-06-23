def choose_words_for_notes(x, y, language_pairs, lecture):
    word_map = {}
    for a, b in language_pairs:
        word_map[a] = b
    
    notes = []
    for word in lecture:
        corresponding_word = word_map[word]
        if len(word) <= len(corresponding_word):
            notes.append(word)
        else:
            notes.append(corresponding_word)
    
    return notes


x, y = map(int, input().split())
language_pairs = [input().split() for i in range(y)]
lecture = input().split()

result = choose_words_for_notes(x, y, language_pairs, lecture)
print(" ".join(result))

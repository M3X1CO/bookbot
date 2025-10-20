def get_word_count(verse):
    word_count = verse.split()
    return len(word_count)

def get_letter_count(verse):
    # create a dic to hold letter 'a': 324 and count
    char_count = {}
    for char in verse.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted(char_count):
    char_list = []

    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key= lambda x: x["num"])
    
    return char_list


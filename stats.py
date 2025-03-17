
def get_num_words(text):
    num_words = text.split()
    return len(num_words)


def count_chars(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] +=1
    return char_dict

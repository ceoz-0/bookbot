
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

def dict_sorter(char_dict):
    sorted_dict = sorted(char_dict.items(),key=lambda x:x[1], reverse=True)
    for char in sorted_dict:
        if char[0].isalpha():       
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_cha = count_cha(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_cha)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    count = 0
    count += len(words)
    return count

def count_cha(text):
    my_dict = {}
    for cha in text:
        lowered_string = cha.lower()
        if lowered_string in my_dict:
            my_dict[lowered_string] += 1
        else:
            my_dict[lowered_string] = 1
    return my_dict


main()

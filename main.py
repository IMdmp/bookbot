def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        char_dictionary = GetCharCount(file_contents)
        list_count = change_to_list_of_count(char_dictionary)
        PrintReport(list_count)

def GetCharCount(file_contents):
    word_count = {}
    
    lower_case_file_contents = file_contents.lower()
    for c in lower_case_file_contents:
        if c in word_count:
            word_count[c] +=1
        elif c.isalpha():
            word_count[c] = 1
    print(word_count)
    return word_count

def change_to_list_of_count(dictionary):
    list = []
    for key in dictionary:
        new_dict = {"char": key, "count": dictionary[key]}
        list.append(new_dict)
    return list


def sort_on(dict):
    return dict["count"]

def PrintReport(list):
    list.sort(key=sort_on, reverse=True)
    for item in list:
        print(f"The '{item["char"]}' was found {item["count"]} times")
main()
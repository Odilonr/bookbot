def main():
    print('---Begin Report of books/frankenstein.txt---')
    file_path = 'books/frankenstein.txt'
    text = get_text_book(file_path=file_path)
    print(f'{count_words(text)} words found in the document\n\n')
    letters_count = count_letter(text)
    to_list =[]
   
    def sort_on(dict):
        return dict['occurence']
    
    for key, val in letters_count.items():
        if key.isalpha():
            to_list.append({'letter':key, 'occurence': val})
    
    to_list.sort(reverse=True, key= sort_on)

    for dic in to_list:
        letter = dic['letter']
        occ = dic['occurence']
        
        print(f"The '{letter}' character was found {occ} times")


    print('---End of Report---')

    


def count_words(text):
    new_text = text.split()
    return(len(new_text))

def count_letter(text):
    text = text.lower()
    char_report = {}

    for char in text:
        if char in char_report:
            char_report[char] += 1
        else:
            char_report[char] = 1
    return char_report


def get_text_book(file_path):
    with open(file_path) as f:
        return f.read()
    

    
    
main()
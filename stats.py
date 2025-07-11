def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def dictionary_of_characters(counts):
    result = []
    for char, count in counts.items():
        if char.isalpha():
            result.append({'char': char, 'num': count})
    result.sort(key=lambda x: x['num'], reverse=True)
    return result        
   
    
    

        
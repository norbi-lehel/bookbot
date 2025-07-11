from stats import word_count ,character_count ,dictionary_of_characters
import sys

def get_book_text(book_path):
        with open(book_path) as file:
           return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
   
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    char_counts = character_count(book_text)
    dick_caracter = dictionary_of_characters(char_counts)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in dick_caracter:
        if not item["char"].isalpha():
            continue
        print (f"{item['char']}: {item['num']}" )
    print(f"============= END ===============")

main()

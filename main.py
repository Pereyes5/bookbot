def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    chars = count_chars(file_contents)
    char_report = [{"alphabet": char, "num": count} for char, count in chars.items()]
    char_report.sort(reverse = True, key = sort_on)
    count = count_words(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print("{} words found in the document\n".format(count))
    for lines in char_report:
        if lines["alphabet"].isalpha():
            print("The '{}' character was found {} times".format(lines["alphabet"], lines["num"]))
    print("--- End report ---")

def count_words(content):
    count = len(content.split())
    return count

def count_chars(content):
    dictionary = {}
    for words in content.split():
        wordL = words.lower()
        for character in wordL:
            dictionary[character] = dictionary.get(character, 0) + 1
    return dictionary

def sort_on(dict):
    return dict["num"]

main()
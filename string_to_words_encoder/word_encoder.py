import os, sys
import argparse
import random
from collections import defaultdict

# Function to load words from a file and organize them by their first letter
def load_words(filename):
    words_by_letter = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if word:  # Ensure the line is not empty
                if len(word) == 1:
                    continue
                first_letter = word[0].lower()  # Use lower() to standardize
                words_by_letter[first_letter].append(word)
    return words_by_letter

# Function to get a random word by its first letter
def get_random_word(letter, words_by_letter):
    letter = letter.lower()
    if letter in words_by_letter and words_by_letter[letter]:
        return random.choice(words_by_letter[letter])
    else:
        print("Not in dictionary")
        return None

def encode_string(to_encode, wordlist):
    output = ""
    for char in to_encode:
        if not char.isalpha():
            output += char + " "
            continue
        chosen_word = get_random_word(char, wordlist)
        if char.isupper():
            chosen_word = chosen_word[0].upper() + chosen_word[1:]
        output += chosen_word + " "
    return output



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process pictures and sort the pixels')
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-s", "--string", help='String to encode')
    g.add_argument("-f", "--file", help = "Filepath of file to encode")
    parser.add_argument("-w", "--wordlist", help = "Override filepath of wordlist to use (Defaults to words.txt)")
    args = parser.parse_args()

    filename = 'words.txt'
    if args.wordlist:
        filename=args.wordlist
    words_by_letter = load_words(filename)

    output = ""
    if args.string:
        output = encode_string(args.string, words_by_letter)

    if args.file:
        with open(args.file, 'r') as file:
            for line in file:
                line = line.strip()
                for char in line:
                    output += encode_string(char, words_by_letter) + " "
                output += "\n"

    print(output)

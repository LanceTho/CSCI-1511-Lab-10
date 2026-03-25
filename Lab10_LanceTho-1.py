"""
Lab10_LanceTho-1.py
Lance Thongsavanh
Create an OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. The program will count the frequency of every word in the selected file and print an alphabetical report.
The first line of code inside of print_report() that sorted the dictionary came from here: https://www.codegenes.net/blog/how-to-sort-dictionary-by-key-python/
Date.
"""
from pathlib import Path
import string
"""
WordAnalyzer Class:
You must create a class named WordAnalyzer.
__init__(self, filepath): The initializer should take the filepath (as a string) and store it as a private pathlibrary
Path object. It should also initialize a private dictionary to hold the word frequencies.
process_file(self): This method will contain the main logic. It must:
Use a try-except block to handle FileNotFoundError gracefully.
Use the pathlib.Path object's .exists() method to check for the file.
Use the pathlib.Path object's .open() method to read the file line by line.
Use string.punctuation to create a translation table to remove all punctuation from each line.
Convert each line to all lowercase.
Split each line into words and update their counts in the internal frequencies dictionary.
The method should return True if processing was successful and False if a FileNotFoundError occurred.
print_report(self): This method should print the results.
Get the keys from the frequencies dictionary and sort them alphabetically.
Print the word and its count in the specified format (see example).
"""
class WordAnalyzer:
    def __init__(self, filepath: str):
        self.__pathlibrary = Path(filepath)
        self.word_frequency = {}

    def process_file(self) -> bool:
        try:
            if not self.__pathlibrary.exists():
                raise FileNotFoundError("File does not exist.")
        except FileNotFoundError as e:
            print(f"Exception Thrown: {e}")
            return False
        else:
            translator = str.maketrans("", "", string.punctuation)
            self.__pathlibrary.open()
            contents = self.__pathlibrary.read_text()
            lines = contents.split()
            for line in lines:
                line = line.translate(translator)
                line = line.lower()
                if(line in self.word_frequency):
                    self.word_frequency[line] += 1
                else:
                    self.word_frequency[line] = 1
            return True

    def print_report(self):
        self.word_frequency = {key: self.word_frequency[key] for key in sorted(self.word_frequency)}
        for word in self.word_frequency:
            print(f"{word:10}:: {self.word_frequency[word]}")

"""
main() Function:
You must also have a main() function (outside of your class) that acts as the "driver" for your program.
It must have the 4 text files path built using the path library that are passed in as values inside a dictionary
File Menu: The main function must define a dictionary of 4 files for the user to choose from (e.g., {"1": "Moby Dick path", "2": "Frankenstein path", ...}).
Main Loop: The function must loop, displaying the menu of 4 files plus an "Exit" option.
User Choice: It should prompt the user for their choice. only displaying the name of the file (e.g., "Tarzan") without the file extension displayed
Validation: If the user's choice is invalid, print an error and re-display the menu.
Execution: If the user picks a valid file, it should:
Get the corresponding filename from the dictionary.
Create an instance of your WordAnalyzer class with that filename.
Call the process_file() method.
If processing was successful, it should then call the print_report() method.
"""

if __name__ == "__main__":
    text = WordAnalyzer("Tarzan.txt")
    print(text.process_file())
    text.print_report()
"""
Lab10_LanceTho-1.py
Lance Thongsavanh
Create an OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. The program will count the frequency of every word in the selected file and print an alphabetical report.
The first line of code inside of print_report() that sorted the dictionary came from here: https://www.codegenes.net/blog/how-to-sort-dictionary-by-key-python/
3/26/2026
"""
from pathlib import Path
import string

class WordAnalyzer:
    """Represents a text file and counts the occurance of words
    """
    def __init__(self, filepath: str) -> None:
        """Creates a private Path object and a dictionary

        Args:
            filepath (str): name of text file
        """
        self.__pathlibrary = Path(filepath)
        self.word_frequency = {}

    def process_file(self) -> bool:
        """Checks if the file exists and if not then handles the FIleNotFoundError. Otherwise, processes the text file by removing the punctuation and converting all the text to lower case. It then counts the occurance of words by adding it to the dictionary's value based on the key.

        Raises:
            FileNotFoundError: If the text file that was given when it was initialized does not exist

        Returns:
            bool: returns False if it couldn't be processed, otherwise returns True
        """
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

    def print_report(self) -> None:
        """Sorts the dictionary in alphabetical order and displays all of the key value pairs
        """
        self.word_frequency = {key: self.word_frequency[key] for key in sorted(self.word_frequency)}
        for word in self.word_frequency:
            print(f"{word:15}:: {self.word_frequency[word]}")

def main() -> None:
    """Drives the program by displaying a menu and based on the user's input, processes the text file and displays the output. It keeps looping unless the user inputs the exit value.
    """
    while True:
        print(f"--- Word Analyzer ---")
        print(f"Please select a file to analyze:")
        print(f"1. Princess Mars (Chapter 1)")
        print(f"2. Bambi (Chapter 1)")
        print(f"3. Pinocchio (Chapter 1)")
        print(f"4. Winnie the Pooh (Chapter 1)")
        print(f"5. Exit")

        user_input: int = int(input("Enter your choice (1-5): "))
        match user_input:
            case 1:
                text: WordAnalyzer = WordAnalyzer("princess_mars.txt")
                print(f"Processing 'princess_mars.txt'...")
                text.process_file()
                text.print_report()
                input("Press Enter to return to the menu...")
            case 2:
                text: WordAnalyzer = WordAnalyzer("bambi.txt")
                print(f"Processing 'bambi.txt'...")
                text.process_file()
                text.print_report()
                input("Press Enter to return to the menu...")
            case 3:
                text: WordAnalyzer = WordAnalyzer("pinocchio.txt")
                print(f"Processing 'pinocchio.txt'...")
                text.process_file()
                text.print_report()
                input("Press Enter to return to the menu...")
            case 4:
                text: WordAnalyzer = WordAnalyzer("winnie_the_pooh.txt")
                print(f"Processing 'winnie_the_pooh.txt'...")
                text.process_file()
                text.print_report()
                input("Press Enter to return to the menu...")
            case 5:
                print(f"Goodbye!")
                break
            case _:
                print(f"Error: Invalid Option")

if __name__ == "__main__":
    main()
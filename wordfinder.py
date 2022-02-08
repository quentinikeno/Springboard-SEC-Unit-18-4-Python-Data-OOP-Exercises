from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> words = WordFinder("simple.txt")
    3 words read

    >>> words.random() in ["cat", "dog", "porcupine"]
    True

    >>> words.random() in ["cat", "dog", "porcupine"]
    True

    >>> words.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, file):
        """Set the file name, adds words from the file to a list, and prints out the number of words."""
        self.file = open(file)
        self.words_list = self.read_file()
        print(f"{len(self.words_list)} words read")

    def __repr__(self):
        return f"<WordFinder file = {self.file}>"

    def read_file(self):
        """For each word in the file add it to a list and return the list of words."""
        lst = list()
        for word in self.file:
            #Strip new line character
            word = word.rstrip('\n')
            lst.append(word)

        self.file.close()
        return lst

    def random(self):
        """Method that returns a random word from the list of words."""
        return choice(self.words_list)

    
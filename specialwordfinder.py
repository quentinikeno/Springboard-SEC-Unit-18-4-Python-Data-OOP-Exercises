from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """WordFinder that ignores comments and empty lines in the file read.
    
    >>> words = SpecialWordFinder("complex.txt")
    3 words read

    >>> words.random() in ["pear", "carrot", "kale"]
    True

    >>> words.random() in ["pear", "carrot", "kale"]
    True

    >>> words.random() in ["pear", "carrot", "kale"]
    True
    """
    def __init__(self, file):
        super().__init__(file)

    def __repr__(self):
        return f"<SpecialWordFinder file = {self.file}>"

    def read_file(self):
        """For each word in the file add it to a list and return the list of words without comments or empty lines."""
        lst = list()
        for word in self.file:
            #Strip new line character
            word = word.rstrip('\n')
            if '#' not in word and word != '':
                lst.append(word)

        self.file.close()
        return lst
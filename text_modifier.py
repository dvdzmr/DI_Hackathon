# This module fetches text from sources and returns arrays of formatted text.


class TextModifier:

    def __init__(self):
        self.text = ""
        self.censor_type = ""
        self.result = []

    def get_text(self, filename):
        pass
        # Check if file exist
        # Load textfile into an array with "." as delimiter

    def censor_text(self, censor_type, banned_words):
        pass
        # Censor text with provided censor_type
        # eg: censor_type = censor (replace banned words with *)
        # censor_type = positive (replace with positive words)
        # Put results in self.result

        # If censor_type is positive, load the alternative_words.json to iterate over later.

    def show_results(self):
        pass
        # Print results
    
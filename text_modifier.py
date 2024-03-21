# This module fetches text from sources and returns arrays of formatted text.
import json

class TextModifier:

    def __init__(self, textfile, censor_type):
        self.text = textfile  # filename of .txt file
        self.censor_type = censor_type
        self.source = ""
        self.result = []
        self.json = ""

    def get_text(self):
        try:
            with open(self.text, 'r') as file:
                text = file.read()  # .split('.')
                self.source = text
        except FileNotFoundError:
            print('File not found.')

        # print(self.source)

    def censor_text(self, banned_words):
        if self.censor_type == "direct":  # replace banned words with *
            for word in banned_words:
                if word in self.source:
                    censor = len(word) * '*'
                    self.source = self.source.replace(word, censor)

        elif self.censor_type == "replace":  # replace banned words with another word
            self.load_json()
            for word in banned_words:
                if word in self.source:
                    try:
                        replacement = self.json[0][word]
                    except KeyError:  # incase key does not exist, we catch the error here
                        censor = len(word) * '*'
                        replacement = censor
                    self.source = self.source.replace(word, replacement)
        else:
            print('Invalid censor type.')


    def load_json(self):
        with open("alternative_words.json", 'r') as file:
            self.json = json.load(file)
            file.close()

    def show_results(self):
        str_result = ''.join(self.source)
        with open(self.text + "_edited", 'w') as file:
            file.write(self.source)

        print("Text modified successfully.")

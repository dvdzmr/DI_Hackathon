import os
from database_handler import DatabaseHandler
from text_modifier import TextModifier


def main():
    # Setting defaults
    textfile_unvalidated, censor_method, textfile, censoring = True, True, "", ""

    # Asking user to provide file
    # print("Welcome to the antisemitism correction facility\n\n To get started please place the file in this folder "
    #       "and enter the name.\n Ex: text.txt")
    # while textfile_unvalidated:
    #     textfile = input("Enter the name of the text file: ")
    #     if os.path.exists(textfile):
    #         textfile_unvalidated = False
    #     else:
    #         print("File not found. Please try again.")

    # Asking user to set the censoring mode
    # print("Do you want to censor the text, or replace the prohibited words with a positive meaning?\n\n Ex: "
    #       "-bannedword- censored is ******** \n Ex: -bannedword- -positiveword-")
    # print("Direct censor with * (A)\n Censor by changing meaning (B)")
    #
    # while censor_method:
    #     censoring = input("Select A or B")
    #     if censoring.upper() == "A":
    #         censoring = "direct"
    #         censor_method = False
    #     elif censoring.upper() == "B":
    #         censoring = "replace"
    #         censor_method = False
    #     else:
    #         print("Select A or B. Please try again.")

    # DEBUG:
    textfile = "mytext.txt"
    censor_method = "replace"
    # Setting up text object
    my_text = TextModifier(textfile, censor_method)

    # Call database_handler and load banned words to a list
    database = DatabaseHandler()
    banned_words = database.load_words()
    # Loading selected source textfile
    my_text.get_text()
    # Call text handler to apply chosen censoring method, and provide list of banned words.
    my_text.censor_text(banned_words)
    my_text.show_results()


if __name__ == '__main__':
    main()

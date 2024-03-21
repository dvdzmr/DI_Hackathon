import os


def main():
    textfile_unvalidated = True
    # create my_text = TextIntake() object
    print("Welcome to the antisemitism correction facility\n\n To get started please place the file in this folder "
          "and enter the name.\n Ex: text.txt")

    while textfile_unvalidated:
        textfile = input("Enter the name of the text file: ")
        if os.path.exists(textfile):
            textfile_unvalidated = False
        else:
            print("File not found. Please try again.")

    # my_text.get_text(textfile)

    print("Do you want to censor the text, or replace the prohibited words with a positive meaning?\n\n Ex: "
          "-bannedword- censored is ******** \n Ex: -bannedword- -positiveword-")

    # Call database_handler and load banned words to a list
    # banned_words = database_handler()
    # my_Text.censor_text(censor_type, banned_words.load_words())

    # print results
    # my_text.show_results()


if __name__ == '__main__':
    main()

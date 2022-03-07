# My first game in Python
# Developed by Wallacy Pasqualini
# Contact me: wallacypasqualini@gmail.com
# LinkedIn: https://www.linkedin.com/in/wallacypasqualini
# See other projects in my GitHub: https://github.com/WallPasq


from random import randint
from os import system


# Creating the main game class
class Hangman:

    # Defining how to instantiate the class
    def __init__(self, word):
        self.word = word
        self.correct = []
        self.wrong = []
        self.board = [
            ('                            +----+\n'
             '                            |    |\n'
             '                            |\n'
             '                            |\n'
             '                            |\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |\n'
             '                            |\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |    |\n'
             '                            |\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |   /|\n'
             '                            |\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |   /|\ \n'
             '                            |\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |   /|\ \n'
             '                            |   /\n'
             '                            |\n'
             '============================================================='),
            ('                            +----+\n'
             '                            |    |\n'
             '                            |    0\n'
             '                            |   /|\ \n'
             '                            |   / \ \n'
             '                            |\n'
             '=============================================================')
        ]

    # Determining whether the letters are right or wrong
    def guess(self, letter):
        letter = letter.lower()
        if len(letter) > 1 or not letter.isalpha():
            return False
        for correct_letter in self.correct:
            if letter == correct_letter:
                return False
        for wrong_letter in self.wrong:
            if letter == wrong_letter:
                return False
        for word_letter in self.word:
            if letter == word_letter:
                self.correct.append(letter)
                return True
        self.wrong.append(letter)
        return True

    # Hiding the letters
    def hide_word(self):
        hidden = []
        if len(self.correct) == 0:
            for _ in self.word:
                hidden.append("_")
        else:
            checker = False
            for word_letter in self.word:
                for correct_letter in self.correct:
                    if word_letter == correct_letter:
                        hidden.append(word_letter)
                        checker = True
                        break
                    else:
                        pass
                if checker:
                    checker = False
                else:
                    hidden.append("_")
        return ''.join(hidden)

    # Checking if the game is over
    def hangman_over(self):
        return len(self.wrong) == 6

    # Checking if the player has won
    def hangman_won(self):
        return self.hide_word() == self.word

    # Printing the board on the screen
    def status(self):
        system('cls')
        print("*************************************************************\n"
              "*****                   HANGMAN GAME                    *****\n"
              "*************************************************************\n")
        print(self.board[len(self.wrong)], "\n")
        print(self.hide_word(), "-> The word has", len(self.word), "letters.\n")
        print("Wrong letters:", ', '.join(self.wrong), "\n")
        print("You have", 6 - len(game.wrong), "more tries, before the man is hanged.\n")


# Function to get a random word from the word bank
def rand_word():
    try:
        with open("words.txt", "rt") as words:
            bank = words.readlines()
    except (FileNotFoundError, ValueError):
        words_lst = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes',
                    'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar',
                    'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb',
                    'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex',
                    'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord',
                    'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby',
                    'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip',
                    'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot',
                    'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey',
                    'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole',
                    'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky',
                    'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub',
                    'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm',
                    'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue',
                    'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps',
                    'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch',
                    'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress',
                    'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen',
                    'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring',
                    'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern',
                    'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch',
                    'zipper', 'zodiac', 'zombie']
        with open('words.txt', 'wt') as words:
            for word in words_lst:
                words.write(word + '\n')
        with open("words.txt", "rt") as words:
            bank = words.readlines()
    return bank[randint(0, len(bank) - 1)].strip()


# Main menu
system('cls')
print("*************************************************************\n"
      "*****            Welcome to the HANGMAN GAME            *****\n"
      "*****          Developed by Wallacy Pasqualini          *****\n"
      "*************************************************************\n\n"
      "*************************************************************\n"
      "*****           It's my first object-oriented           *****\n"
      "*****                programming project                *****\n"
      "*************************************************************\n\n"
      "*************************************************************\n"
      "*****              Hope you like! Enjoy it              *****\n"
      "*************************************************************\n")
print("TIP: If it doesn't exist, the game will create a file called\n"
      "words.txt, in the same folder where it is inserted, with 213\n"
      "words taken from the site:\n\n"
      "https://www.hangmanwords.com/words\n\n"
      "Use this file to take out words, add others, or even change\n"
      "them completely to challenge someone ;)\n")
start = input("Start game?\n"
              "y = Yes\n"
              "n = No\n\n")
start = start.lower()

# Loop to not allow the user to type something invalid
while start != 'y' and start != 'n':
    system('cls')
    print("*************************************************************\n"
          "*****            Welcome to the HANGMAN GAME            *****\n"
          "*****          Developed by Wallacy Pasqualini          *****\n"
          "*************************************************************\n\n"
          "*************************************************************\n"
          "*****           It's my first object-oriented           *****\n"
          "*****                programming project                *****\n"
          "*************************************************************\n\n"
          "*************************************************************\n"
          "*****              Hope you like! Enjoy it              *****\n"
          "*************************************************************\n")
    print("TIP: If it doesn't exist, the game will create a file called\n"
          "words.txt, in the same folder where it is inserted, with 213\n"
          "words taken from the site:\n\n"
          "https://www.hangmanwords.com/words\n\n"
          "Use this file to take out words, add others, or even change\n"
          "them completely to challenge someone ;)\n")
    start = input("Start game?\n"
                  "y = Yes\n"
                  "n = No\n\n"
                  "!!! Please, enter a valid option !!!\n\n")
    start = start.lower()

# Loop to play and replay the game as many times as the user wants
while start == 'y':
    game = Hangman(rand_word())

    # Loop to continue the game until the player wins or loses
    while not game.hangman_won() and not game.hangman_over():
        game.status()
        attempt = input('Try a letter: ')

        # Loop to not allow the user to type something invalid
        while not game.guess(attempt):
            game.status()
            print('You already tried that letter, or typed something invalid.\n')
            attempt = input('Try another letter: ')

    # Actions if the player wins or loses the game
    if game.hangman_won():
        game.status()
        print('Congratulations! You won the hangman game.\n')
    elif game.hangman_over():
        game.status()
        print('Oh no. The man was hanged! The word was %s.\n' % game.word)

    start = input("Play again?\n"
                  "y = Yes\n"
                  "n = No\n\n")
    start = start.lower()

    # Loop to not allow the user to type something invalid
    while start != 'y' and start != 'n':
        if game.hangman_won():
            game.status()
            print('Congratulations! You won the hangman game.\n')
        elif game.hangman_over():
            game.status()
            print('Oh no. The man was hanged! The word was %s.\n' % game.word)

        start = input("Play again?\n"
                      "y = Yes\n"
                      "n = No\n\n"
                      "!!! Please, enter a valid option !!!\n\n")
        start = start.lower()

if start == 'n':
    print("\n"
          "Thanks for visiting my game! See you later.")

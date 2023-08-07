import os 

from random import choice

from time import sleep



#rules of hangman : 

# max wrong guesses  = 6 

# track the guessed letters so they cant double guess

# word bank : random choice 



#words letters guessing



#right or wrong letters



#full letters



# _ _ _ a _ <- something like this at some point

class Hangman():

    MAX_MOVES = 6

    WORD_BANK = ("abruptly", "honest", "cheesecake", "hornet",

                 "hockey", "quarter", "couch", "potato", "infinite", "crinkle", "celebrate")



    GALLOW_STAGES = [

        """

        +---+

        |   |

            |

            |

            |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

            |

            |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

        |   |

            |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

       /|   |

            |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

       /|\  |

            |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

       /|\  |

       /    |

            |

        ============

        """,

        """

        +---+

        |   |

        O   |

       /|\  |

       / \  |

            |

        ============

        """

    ]



    def __init__(self):

        self.word = choice(Hangman.WORD_BANK)

        self.guessed_letters = []

        self.incorrect_guesses = []

        self.num_of_moves = 0

    

    

    def show_word(self):

        os.system("cls" if os.name == "nt" else "clear")

        board = ["_ " if letter not in self.guessed_letters else letter for letter in self.word]

        for letter in board:

            print(letter, end=" ")

        print()

        print("\nGuessed letters : ", end=" ")

        if self.guessed_letters:

            for letter in self.guessed_letters:

                print(letter, end=" ")

        else:

            print("\nYou haven't guessed any letters!")

        print()

        print(f"You have {Hangman.MAX_MOVES - self.num_of_moves} move(s) left!")



        if self.incorrect_guesses:

            stage = min(self.num_of_moves, len(Hangman.GALLOW_STAGES) - 1)

            print(Hangman.GALLOW_STAGES[stage])       



    def guess_letter(self, letter):

        if len(letter) > 1:

            print("You can't do that, one letter at a time")

            return



        if letter in self.word:

            count = self.word.count(letter)

            print(f'You found {count} {letter}{"s" if count > 1 else ""}')

        else:

            print(f'{letter} not in the word')

            self.num_of_moves += 1

            self.incorrect_guesses.append(letter)



        self.guessed_letters.append(letter)



    def check_all_letters_guessed(self):

        for letters in self.word:

            if letters not in self.guessed_letters:

                return False

        return True

    

    def guess_word(self,word):

        if word == self.word:

            return True

        return False

    

    def check_moves_left(self):

        if self.num_of_moves < Hangman.MAX_MOVES:

            return True

        return False

    

    def user_won(self):

        print(f"Congrats! You got the word with {Hangman.MAX_MOVES - self.num_of_moves} move(s) left! You ROCK!")



    def user_lost(self):

        print(f"\nWOW, that hurt to watch.\n\nThe word was {self.word}")



class UI():

    hangman = Hangman()



    @classmethod

    def main(cls):

        # we can tell them the rules of our game if they havent played (mario vibes)

        os.system("cls" if os.name == "nt" else "clear")

        action = input("Have you played hangman before? If not or if its been a while say no/n!\n\nIf you're ready to play, press Enter to get started!").lower()

        if action == "no" or action == 'n':

            os.system("cls" if os.name == "nt" else "clear")

            print("Here's how to play:\n1. You (the guesser) tries to guess the letters of the secret word one letter at a time. \n2. For every wrong guess, a part of the hangman is drawn. \n3. Keep guessing letters until you either guess the whole word correctly or the hangman drawing is completed. \n\nThe game ends when you guess the word correctly or when the hangman is fully drawn (which means you lost). \nTry to guess the word before the hangman gets fully drawn!\n\nThis message will self destruct in...")

            sleep(20)

        else:

            pass

        while True:

            #show them the word like this : _ _ _ _ _

            cls.hangman.show_word()

            # ask them for thier letter to guess!

            letter = input("What letter do you want to guess? ").lower()

            # see if the letter was right

            cls.hangman.guess_letter(letter)

            # we need to let them know if they got any correct

            cls.hangman.show_word()

            # make sure they havent solved the whole word yet

            if cls.hangman.check_all_letters_guessed():

                cls.hangman.user_won()

                break

            # we want to ask if they want to guess the whole word

            action = input("Would you like to guess the whole word? yes/y or no/n ").lower()

            if action == "yes" or action == 'y':

            # if they gave us a word we wanna check it

                word = input("What is your word? ")

                if cls.hangman.guess_word(word):

            # if they guess the word, give em a congrats and go again

                    cls.hangman.user_won()

                    break

            # see how many moves they have made, >= 6 and they are donezo 

            if not cls.hangman.check_moves_left():

                cls.hangman.user_lost()

                break



UI.main()

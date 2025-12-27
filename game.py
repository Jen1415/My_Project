RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
RESET = '\033[0m'

def guess():
        userInput = ''
        count = 1
        while (len(userInput) != 5) or not(userInput.isalpha()):
                if count > 1:
                        if len(userInput) != 5:
                                print(RED + "Error: " + RESET + "Not a five letters word.")
                        if not(userInput.isalpha()):
                                print(RED + "Error: " + RESET + "A word should not contains digit.")
                userInput = input("Guess a five letters word: ")
                count +=1
        return userInput


def compare(ans, ui):
        while True:
                ui_letters = [letter for letter in ui]
                ans_letters = [letter for letter in ans]
                if ui_letters != ans_letters:
                        # when not the true answer
                        for letter in ui_letters:
                                # there are some identical letters
                                if letter in ans_letters:
                                        # first possible: misplaced
                                        if ui_letters.index(letter) != ans_letters.index(letter):
                                                colour = YELLOW

                                        # second possible: correct place        
                                        else:
                                                colour = GREEN
                                # no identical letters at all
                                else:
                                        colour = RED
                                print(colour + letter + RESET, end = '')
                        print()
                else:
                        print(GREEN + ui + RESET)
                        return
                ui = guess()
                        

        

def main():
        import random


        pro_name = 'Word Raider'

        print(f'Welcome to {pro_name}!')

        with open('words.txt','r') as w:
                words = [lines.rstrip() for lines in w ]
                
        ans = random.choice(words)
        userInput = guess()

        compare(ans,userInput)

        print(GREEN + 'Congratulations!' + RESET + 'Your answer is correct!')




main()
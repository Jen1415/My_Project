RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
RESET = '\033[0m'

def guess():
        userInput = ''
        count = 1
        while (len(userInput) != 5) or not(userInput.isalpha()):
                if count > 1:
                        if not(userInput.isalpha()):
                                print(RED + "Error: " + RESET + "A word should only contains letters.")
                        elif len(userInput) != 5:
                                print(RED + "Error: " + RESET + "Not a five letters word.")
                userInput = input("Guess a five letters word: ")
                count +=1
        return userInput


def print_colour(LETTER, COLOUR):
        print(COLOUR + LETTER + RESET, end = '')


def compare(ans, ug):
        from collections import Counter

        ans_counter = Counter(ans)

        for i, letter in enumerate(ug):
                if letter == ans[i]:
                        print_colour(letter,GREEN)
                        ans_counter[letter] -= 1
                elif (letter in ans_counter) and (ans_counter[letter] > 0):
                        print_colour(letter,YELLOW)
                        ans_counter[letter] -= 1
                else:
                        print_colour(letter,RED)


        

def main():
        import random


        pro_name = 'Word Raider'

        print(f'Welcome to {pro_name}!')

        with open('words.txt','r') as w:
                words = [lines.rstrip() for lines in w ]
                
        ans = random.choice(words)
        for attempts in range(1,6):
                print(f'Attempts left: {YELLOW + str(6-attempts) + RESET}')
                userInput = guess()
                compare(ans,userInput)
                print()
                if userInput == ans:
                        print(f'Congratulations! The answer is {GREEN + ans + RESET}.')
                        print(f'Attempts took: {YELLOW + str(attempts) + RESET}')
                        break
        else:
                print(f'Unfortunately! The answer is {GREEN + ans + RESET}.')


main()
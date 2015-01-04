#! /usr/bin/env python3

from random import Random
from string import Template

def play():
        lo = 1
        hi = 100
        found_it = False
        generator = Random()
        while found_it == False:
                guess = generator.randint(lo, hi)
                template = Template('Is it ${g}?')
                question = template.substitute(g=guess)
                answer = ''
                valid_answers = ('y', 'q', 'h', 'l')
                while answer not in valid_answers:
                        print(question)
                        print('(H) Higher')
                        print('(L) Lower')
                        print('(Y) You got it!')
                        print('(Q) Quit')
                        answer = input('> ').lower()
                        if answer not in valid_answers:
                                print('Uh. Try again.')
                if answer == 'y':
                        found_it = True
                        print('Yay! I got it!')
                        answer = input('Play again? (Y/n) ').lower()
                        if answer == 'y':
                                found_it = False
                                lo = 1
                                hi = 100
                        else:
                                print("Okay. :) See you later!")
                elif answer == 'q':
                        print("I'll get it one day. Good bye!")
                        return
                elif answer == 'h':
                        lo = guess + 1
                elif answer == 'l':
                        hi = guess - 1
                else:
                        print("Oops. Something went wrong.")

def start():
        print('HIGH OR LOW')
        print('Pick a number between 1 and 100 and I will try to guess it.')
        user_is_ready = input('Ready? (Y/n) ').lower()
        if user_is_ready == 'y' or user_is_ready == '':
                play()
        else:
                print("Let's play later, then. Good bye.")

if __name__ == '__main__':
        start()

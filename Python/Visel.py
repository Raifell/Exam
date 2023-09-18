# -*- coding: utf-8 -*-
import random


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_attempts = 6

    def play(self):
        print("Welcome to Hangman!")
        print("Guess the word before the hangman is complete.")
        print("The word has", len(self.word), "letters.")

        while True:
            self.display_word()

            if self.is_word_guessed():
                print("Congratulations! You guessed the word correctly.")
                break

            if len(self.guesses) >= self.max_attempts:
                print("Game over! You ran out of attempts.")
                print("The word was:", self.word)
                break

            guess = self.get_guess()
            self.guesses.append(guess)

            if guess not in self.word:
                print("Wrong guess!")

    def display_word(self):
        for letter in self.word:
            if letter in self.guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def is_word_guessed(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def get_guess(self):
        while self.max_attempts != 0:
            guess = input("Enter your guess: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif guess in self.guesses:
                print("You already guessed that letter.")
            elif not guess.isalpha():
                print("Please enter a letter.")
            else:
                return guess


word_list = ["python", "hangman", "programming", "code", "computer"]
words = random.choice(word_list)

game = Hangman(words)
game.play()

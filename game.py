"""A number-guessing game."""

from random import randint

print("Welcome to the Guessing Game!")

name = input("What is your name? ")

randnum = randint(1, 100)

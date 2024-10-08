Number Guessing Game
Overview:

This program is a command-line based number guessing game written in Python. The user has five chances to guess a randomly generated number between 1 and 10. After each guess, the user will receive a hint indicating whether the number they entered is too high or too low. The game ends when the user either guesses the number correctly or exhausts all five attempts.
How to Run:

    Run the program in a Python environment.
    You will be prompted to input a number between 1 and 10.
    After each guess, the program will provide feedback.
    If you guess correctly, the game will announce that you have won.
    If you fail to guess the number in 5 attempts, you will lose.

Requirements:

    Python 3.x

Error Handling:

    The program ensures that only valid integer inputs are accepted. If the user enters invalid input, they are prompted to re-enter a number.

Example Output:

typescript

You have five chances
Please enter a number between 1 and 10: 5
You have guessed 1 times
The number is too high
Please enter a number between 1 and 10: 3
...
You won!
# Note
   1 Importing Modules: The import random statement at the beginning of the code 
    
    demonstrates how to import external modules to use their functionalities in your 
    
    program.


    2 Generating Random Numbers: The random.randint() function generates a random 
    
    number within a specified range. This introduces the concept of using external 
    
    libraries to extend the capabilities of your code.

    3 User Input: The input() function lets the user provide input. Converting the 
    
    input to an integer (int(input())) demonstrates how to handle user input and 
    
    convert it to the desired data type.

    4 Conditional Statements (if, elif, else): Conditional statements are used to 
    
    check whether the user's guess is too high, too low, or correct. They guide the 
    
    flow of the game based on the provided conditions.

    5 Loops (while): The while loop ensures that the game continues until the user 
    
    correctly guesses the number. It demonstrates how to implement iterative 
    
    processes.

    6 String Formatting: The print() statements use string formatting to display 
    
    messages that include variables (e.g., {target_number} and {attempts}) within 
    
    the string.

    7 Type Conversion: The user's input is converted from a string to an integer 
    
    using the int() function to perform comparisons and calculations.

    8 Exiting the Program: The break statement is used to exit the loop and end the 
    
    game once the user correctly guesses the number.

    9 Executable Code in if __name__ == "__main__": Block: The code block under if 
    
    __name__ == "__main__": ensures that the guess_the_number() function is executed 
    
    only when the script is run directly (not when it's imported as a module). This 
    
    is a common best practice to make your code more reusable.

    10 In the given code snippet, the f in front of the string is used to create an f-string, also known as a formatted string 
    
    literal. F-strings are a feature introduced in Python 3.6 that allow you to embed expressions and variables directly into 
    
    string literals for formatting.

    Here's the explanation of how the f-string works in your code:

    python

    print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")

    The f before the opening double-quote indicates that the string is an f-string.
    
    Inside the f-string, you can include expressions enclosed in curly braces {}. These expressions are evaluated and their values 
    
    are inserted into the string.

    In the code snippet:

    {target_number} is an expression that gets replaced with the value of the target_number variable.
    
    {attempts} is an expression that gets replaced with the value of the attempts variable.

    Using f-strings simplifies string formatting and makes it more readable by allowing you to directly embed variables and 
    
    expressions into the string without the need for complex concatenation or formatting methods.


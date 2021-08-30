"""EX01 hello."""
"""
1. Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""
name = input("What  is your name? ")
random_number = int(input(f"Hello, {name}! Enter a random number: "))
second_number = int(input("Great! Now enter a second random number: "))

answer = random_number + second_number

print(f"{random_number} + {second_number} is {answer}")
"""
2. Poem
Example output:

Roses are red,
violets are blue,
I love to code
And so will you!

"""

color = str(input("Roses are ..."))
objects = str(input("... are blue"))
activity = str(input("I love to ..."))

print(f"Roses are {color}, \n"
      f"{objects} are blue, \n"
      f"I love to {activity} \n"
      f"And so will you!")

"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""
greeting_type = str(input("Enter a greeting "))
recipient = str(input("Enter the name of recipient "))
repeat_amount = int(input("How many times "))
greeting = (greeting_type + " " + recipient + " ")
print(greeting * repeat_amount)

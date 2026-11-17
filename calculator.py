import random
import math

def math_explorer():
    lucky = float(input("Enter a number: "))
    print(f"Fabs: {math.fabs(lucky)}, Ceil: {math.ceil(lucky)}, Floor: {math.floor(lucky)}")
    print(f"GCD of 12 and 18: {math.gcd(12, 18)}")

def guessing_game():
    secret = random.randint(1, 10)
    guess = 0
    attempts = 0
    
    while guess != secret:
        guess = int(input("Guess a number (1-10): "))
        attempts += 1
        if guess < secret: print("Too low!")
        elif guess > secret: print("Too high!")
        
    print(f"You won in {attempts} tries!")

# Main Menu
choice = input("Choose: 'math calculator' or 'number guessing game'? ")
if choice == 'math calculator':
    math_explorer()
elif choice == 'number guessing game':
    guessing_game()
import time

def simple_random(max_value):
    seed = int(time.time()) % max_value
    while True:
        seed = (seed * 1103515245 + 12345) % 0x100000000
        yield seed % max_value

def main():
    max_value = 255
    random = simple_random(max_value)
    num_to_guess = next(random)

    print("Please guess a number between 0 and 65535")
    attempts = 0
    while True:
        try:
            guess = int(input("Guess: "))
            attempts += 1
            if guess == num_to_guess:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < num_to_guess:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
main()
        

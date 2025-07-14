PYRAMID = '#'

def _validate_input(prompt):
    
    while True:
    
        user_input = input(prompt)

        try:
            value = int(user_input)
            if value <= 0:
                print("Sorry, number must be greater than 0")
                continue
            return value
        except ValueError:
            print("That is not a valid number. Please try again: ")


def mario():

    start = 1
    end = _validate_input("Please input a number greater than 0: ")

    while start <= end:
        space = " " * (end-start)
        pyaramid = f'{PYRAMID}'*start
        print(f"{space}{pyaramid} {pyaramid}")
        start += 1

mario()
import random as rnd
import string

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()"
CHARACTERS = [LETTERS + DIGITS + SYMBOLS]

def generate_password(length, num_letters, num_digits, num_symbols):
    password = []
    
    """for i in range(length):
            password.append(CHARACTERS[rnd.randint(0, CHARACTERS_SIZE-1)])"""
    
    rnd.shuffle(password)
    
    return "".join(password)

def get_input():
    length = 0
    while length < 1:
        length = int(input("Enter length of password: "))
        
    num_letters = check_num_characters("Enter number of letters: ", length)
    num_digits = check_num_characters("Enter number of digits: ", length, num_letters)
    num_symbols = check_num_characters("Enter number of symbols: ", length, num_letters, num_digits)
    
    return length, num_letters, num_digits, num_symbols

def check_num_characters(message, length, num_letters=0, num_digits=0, num_symbols=0):    
    num = length + 1
    while num > length - num_letters - num_digits - num_symbols:
        num = input(message)
        if num == "":
            num = rnd.randint(0, length - num_letters - num_digits - num_symbols - 1)
        else:
            num = int(num)
        
    
    return num

def main():
    print(get_input())
    
    #print(generate_password(length))

if __name__ == "__main__":
    main()
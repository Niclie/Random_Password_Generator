import random as rnd
import string

LETTERS = list(string.ascii_letters)
UPPERCASE_LETTERS = list(string.ascii_uppercase)
LOWERCASE_LETTERS = list(string.ascii_lowercase)
DIGITS = list(string.digits)
#SYMBOLS = list("!@#$%^&*()")
SYMBOLS = list("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"')
CHARACTERS = [LETTERS, DIGITS, SYMBOLS]
CHARACTERS_SIZE = len(CHARACTERS)

def generate_password(length, num_letters, num_digits, num_symbols):
    password = []
    
    num = [num_letters, num_digits, num_symbols]
    num_of_char_types = []
    for i in range(CHARACTERS_SIZE):
        if num[i] != 0:
            num_of_char_types.append([i, num[i]])
            
    
    for i in range(length):
        random_id = rnd.choice(range(len(num_of_char_types)))
        random_elem = num_of_char_types[random_id]
        char_type = random_elem[0]
        match char_type:
            case 0:
                password.append(rnd.choice(LETTERS))
                random_elem[1] -= 1
            
            case 1:
                password.append(rnd.choice(DIGITS))
                random_elem[1] -= 1
            
            case 2:
                password.append(rnd.choice(SYMBOLS))
                random_elem[1] -= 1
        
        if random_elem[1] == 0:
            del num_of_char_types[random_id]
    
    rnd.shuffle(password)
    
    return "".join(password)


def get_input():
    length = 0
    while length < 6:
        length = int(input("Enter length of password: "))
    
    type = []
    if input("Enter 'c' for customize password \n'a' for include all characters \n:") == "c":
        if input("Include symbols?(y/n): ") == "y":
            type.append("Symbols")
        
        if input("Include numbers?(y/n): ") == "y":
            type.append("Numbers")
            
        if input("Include lower case letters?(y/n): ") == "y":
            type.append("Lower case letters")
            
        if input("Include upper case letters?(y/n): ") == "y":
            type.append("Upper case letters")
    else:
        type = ["Symbols", "Numbers", "Lower case letters", "Upper case letters"]
        
    char_types = constrained_sum_sample_pos(len(type), length)
    rnd.shuffle(type)
    rnd.shuffle(char_types)
    
    return dict(zip(type, char_types))


def check_num_characters(message, length, num_letters=0, num_digits=0, num_symbols=0, equalize=0):    
    num = length + 1
    while num > length - num_letters - num_digits - num_symbols:
        num = input(message)
        if num == "":
            num = rnd.randint(0, length - num_letters - num_digits - num_symbols - 1)
        else:
            num = int(num)
        
    return num

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(rnd.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


def main():
    print(get_input())


if __name__ == "__main__":
    main()
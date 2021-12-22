import random as rnd
import string
""
UPPERCASE_LETTERS = list(string.ascii_uppercase)
LOWERCASE_LETTERS = list(string.ascii_lowercase)
DIGITS = list(string.digits)
SYMBOLS = list("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"')
CHARACTERS = {"UPPERCASE_LETTERS": UPPERCASE_LETTERS, "LOWERCASE_LETTERS": LOWERCASE_LETTERS, "DIGITS": DIGITS, "SYMBOLS": SYMBOLS}


def generate_password(length, char_type):
    """funzione che genera una password basandosi sulla lunghezza e il tipo di elementi da includere descritti in un dizionario

    Args:
        length (Positive Integers): lunghezza della password
        char_type (Dictionary): Dictionary contente la descrizione della password
        
    Returns:
        String: password generata in modo casuale
    """
    password = []
    
    for i in range(length):
        random_key = rnd.choice(list(char_type))
        password.append(rnd.choice(CHARACTERS[random_key]))
        char_type[random_key] -= 1
        
        if char_type[random_key] == 0:
            del char_type[random_key]
        
    rnd.shuffle(password)
    
    return "".join(password)


def get_input():
    """Funzione che si occupa di interagire con l'utente per permettergli di descrivere la password voluta

    Returns:
        Positive Integers: lunghezza della password
        Dictionary: descrizione della password
    """
    length = 0
    while length < 6:
        length = int(input("Enter length of password: "))
    
    type = []
    if input("Enter 'c' for customize password \n'a' for include all characters \n:") == "c":
        if input("Include symbols?(y/n): ") == "y":
            type.append("SYMBOLS")
        
        if input("Include numbers?(y/n): ") == "y":
            type.append("DIGITS")
            
        if input("Include lower case letters?(y/n): ") == "y":
            type.append("LOWERCASE_LETTERS")
            
        if input("Include upper case letters?(y/n): ") == "y":
            type.append("UPPERCASE_LETTERS")
    else:
        type = ["SYMBOLS", "DIGITS", "LOWERCASE_LETTERS", "UPPERCASE_LETTERS"]
        
    char_types = constrained_sum_sample_pos(len(type), length)
    rnd.shuffle(type)
    rnd.shuffle(char_types)
    
    return length, dict(zip(type, char_types))


def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur.

    Args:
        n (Integer): number of integers that sum is equal to total
        total (Integer): total sum of n positive integers

    Returns:
        List of integers: list of integers that sum is equal to total
    """
    dividers = sorted(rnd.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


def main():
    len, dic = get_input()
    passw = generate_password(len, dic)
    
    print(passw)

if __name__ == "__main__":
    main()
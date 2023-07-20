import random
import string

def generate_password(duljina, m_slova, v_slova, brojevi, znakovi):
    m_letters = string.ascii_lowercase
    v_letters = string.ascii_uppercase
    numbers = string.digits
    signs = string.punctuation

    characters = ""
    if m_slova:
        characters += m_letters
    if v_slova:
        characters += v_letters
    if brojevi:
        characters += numbers
    if znakovi:
        characters += signs

    password = ""

    while len(password) != duljina:
        new_char = random.choice(characters)
        password += new_char
        
    return password

duljina = int(input("Unesite duljinu: "))
m_slova = input("Želite li da lozinka sadrži mala slova? (da/ne) ").lower() == "da"
v_slova = input("Želite li da lozinka sadrži slova? (da/ne) ").lower() == "da"
brojevi = input("Želite li da lozinka sadrži brojeve? (da/ne) ").lower() == "da"
znakovi = input("Želite li da lozinka sadrži znakove? (da/ne) ").lower() == "da"

password = generate_password(duljina, m_slova, v_slova, brojevi, znakovi)

print("Lozinka: ", password)
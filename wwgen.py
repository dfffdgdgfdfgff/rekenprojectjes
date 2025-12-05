import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

len_ww = int(input("Hoe characters lang moet het wachtwoord zijn? "))

wachtwoord = ''.join(random.choice(characters) for _ in range(len_ww))

print(f"Uw wachtwoord is: {wachtwoord}")
import secrets
import string
import random

length = random.randint(12,22)
alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    if length - (sum(c.isalnum() for c in password) >=3 and sum(c.isupper() for c in password) >=3):
            break

password = ''.join(random.sample(password, length)) #password reshuffle
print(password)

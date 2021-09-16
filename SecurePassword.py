import secrets
import string

chars = string.digits + string.ascii_lowercase + string.ascii_uppercase+string.punctuation
print("".join(secrets.choice(chars) for _ in range(16)))



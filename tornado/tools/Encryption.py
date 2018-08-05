from passlib.hash import pbkdf2_sha256

PASSWORD_HASHER = pbkdf2_sha256.using(rounds=30000, salt_size=32)

def getPasswordHash(password):
    return PASSWORD_HASHER.hash(password)

def verifyPassword(password, passwordHash):
    return PASSWORD_HASHER.verify(password, passwordHash)

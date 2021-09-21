import hashlib

def sha1_convert(original_password):
    # sha1 function requires encoded text (original_password) UTF8
    digest = hashlib.sha1(original_password.encode()).hexdigest()
    return digest

def crack_sha1_hash(hash,use_salts = False):
    match = False
    with open('top-10000-passwords.txt') as p:
        for line in p:
            password = line.strip()
            # convert password to hash
            hashed_pass = sha1_convert(password)
            # check if hash matches
            if hash == hashed_pass:
                match == True
                return password
    if match == False:
        return "PASSWORD NOT IN DATABASE"
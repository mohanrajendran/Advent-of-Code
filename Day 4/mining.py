import md5

def valid_hash(hash):
    return hash[0:5] == '00000'

key = 'yzbqklnj'

found = False
salt = 0
while not found:
    salted = key + str(salt)
    if valid_hash(md5.new(salted).hexdigest()):
        found = True
    else:
        salt += 1

print salt

#check if a string belongs to an file
def isinside(username, blacklist):
    v = []
    with open(blacklist, 'r') as f:
        v = f.readlines()
    if username in v:
        return True
    return False


global APIKeys

def setup(key):
    global APIKeys
    APIKeys = key
    
    return True if(key == APIKeys) else False
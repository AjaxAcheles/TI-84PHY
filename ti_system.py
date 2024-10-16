
def disp_clr():
    import os
    os.system('cls')

def wait_key():
    key = input("")
    if key == "":
        return 140
    try: 
        return int(key) + 142
    except:
        pass
    raise KeyError("Not a valid input")
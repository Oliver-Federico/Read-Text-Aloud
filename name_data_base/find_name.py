def findName(string):
    return lookForName(string.lower())

def lookForName(string):
    f = open("name_data_base/" + str(string[0].upper()) + "names.txt", "rt")
    names = f.readlines()
    f.close()
    for x in range(len(names)):
        if names[x].lower().replace(" ","").replace("\n","") == string:
            return True
    return False


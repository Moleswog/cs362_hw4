def cubeVolume(l):
    # return sideLength^3
    if type(l) is int or type(l) is float:
        return l * l * l
    
    return TypeError
    

def avgList(li):
    # num of items
    j = 0
    # total of items
    t = 0
    for i in li:
        if(type(i) is not int):
            return TypeError
        j += 1
        t += i
    if j == 0:
        return None
    else:
        return t/j

def nameGen(f, l):
    if(type(f) is not str or type(l) is not str):
        return TypeError
    return f + " " + l

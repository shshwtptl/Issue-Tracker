# Here will be funcitons like getBool() or getStr().
# So it would make it easier for me to get specific inputs when required.

def getStr():
    _inp:  str
    _inp = input(">> ")
    return _inp

def t_getStr(t: str):
    _inp: str
    _inp = input(t + " >> ")
    return _inp

def t_getInt(t: str):
    _inp: int
    _inp = int(input(t + ">> "))

    return _inp
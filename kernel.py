import random
def returnMethods(base, code):
    method = ""
    n = 0
    while( n < len(code)):
        varA = code[n]
        var = 0
        if code[n] !="\n" and len(base[int(code[n])]) > 0:
            method += base[int(code[n])].replace("\n","")
        if code[n] == "\n":
            method += "\n"
        n += 1
    return method + ""
def returnRandomMethods(base, code):
    method = "try:\n\t"
    n = 0
    while(n < 100):
        var = random.randint(0,len(base))
        if var == len(base):
            method += "\n"
        if var != len(base) and 29 != var and 30 != var:
            method += base[var].strip() + " "
        n += 1
    return method + "\nexcept:\n\tprint(\"details...\")"
with open("carrier.conf", encoding='ISO-8859-1') as f:
    carrier = f.read()
with open("base.conf", encoding='ISO-8859-1') as f:
    base = f.readlines()
with open("manifest.conf", encoding='ISO-8859-1') as f:
    code = f.readlines()
    f = open("respondent.py", "w", encoding="utf8")
    proc = returnMethods(base,code)
    proc = returnRandomMethods(base,code)
    f.write(carrier)
    f.write(proc.strip())
    f.flush
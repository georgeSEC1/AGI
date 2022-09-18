def returnmethods(base, code):
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
with open("carrier.conf", encoding='ISO-8859-1') as f:
    carrier = f.read()
with open("base.conf", encoding='ISO-8859-1') as f:
    base = f.readlines()
with open("manifest.conf", encoding='ISO-8859-1') as f:
    code = f.readlines()
    f = open("respondent.py", "w", encoding="utf8")
    proc = returnmethods(base,code)
    f.write(carrier)
    f.write(proc.strip())
    f.flush
def returnmethods(base, code):
    method = ""
    n = 0
    #while( n < len(code)-1):
        #var = base[int(code[n].strip())].strip()
        #print(var)
        #if len(var) > 0 :
            #method += var
        #if len(var) == 0:
            #method += "\n"
        #n += 1
    return method
with open("base.conf", encoding='ISO-8859-1') as f:
    base = f.readlines()
with open("code.conf", encoding='ISO-8859-1') as f:
    code = f.readlines()
    f = open("AGI.py", "w", encoding="utf8")
    proc = returnmethods(base,code)
    f.write(proc)
    f.flush
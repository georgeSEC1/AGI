def convert(lst):
    return (lst.split())
def returnmethod(arr, operator):
    ngram = ""
    n = 0
    for seg in arr:
        method += operator[seg] 
    return method
with open("instructor.conf", encoding='ISO-8859-1') as f:
    text = f.readlines()
with open("operations.conf", encoding='ISO-8859-1') as f:
    operator = f.readlines()
    f = open("AGI.py", "w", encoding="utf8")
    for line in text:
        proc = returnmethod(convert(text),operator)
        f.write(proc)
        f.flush
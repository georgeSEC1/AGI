def convert(lst):
    return (lst.split())
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    sentences = text.split(".")
    output = ""
    i = 0
    words = convert(user)
    while(i < len(sentences)-1):
        if len(sentences[i]) > 0:
            for word in words:
                if sentences[i].find(" " + word + " ") > -1:
                    output += sentences[i] +"."
        i+=1
    return output
def UVG(inferences):
    with open("fileList.conf", encoding='ISO-8859-1') as f:
        places = f.readlines()
        place = random.shuffle(places)    
    return convert(gather(inferences,place.strip()))
try:
	if 1 < UVG():
		print(True)
except:
	print(False)
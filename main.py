with open("C:\\Users\\User\\Documents\\yesterday.txt", "r") as text:
    d1 = {}
    for line in text:
        line = line.strip()
        line = line.lower()
        seps = ['?', '!', ',', '.', ':', ';']
        for sep in seps:
            line = line.replace(sep, ' ')
        words = line.split()
        for word in words:
            if word in d1:
                d1[word] = d1[word] + 1
            else:
                d1[word] = 1
    for key in list(d1.keys()):
        print(key, ':', d1[key])
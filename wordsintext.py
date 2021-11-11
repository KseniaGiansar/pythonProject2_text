import re
#delimiters = ['\n', ' ', ',', '.', '?', '!', ':']
text = open("C:\\Users\User\Documents\text.txt", "r")
#text = "yyy aa, aa yyy v: aa! v! v aa v v"
splitted = re.split(r'[\b\W\b]+', text)
split_set = set(splitted)      #set is for defining unique items
print(split_set)
print(splitted)
l1 =[]
count = 0
for i in split_set:
    if i in l1:
        count += 1
        l1.append(i)
    print('Word {} occurs {} times'.format(i, splitted.count(i)))


text = ("C:\\Users\\User\\Documents\\text.txt", "r")
d1 = {}
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(' ')
    print(line)

    for word in words:
        if word in d1:
            d1[word] = d1[word]+ 1
        else:
            d1[word] = 1
for key in list(d1.keys()):
    print(key, ':', d1[key])
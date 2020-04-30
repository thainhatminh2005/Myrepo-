import json
file = open('filenhap.json', 'a+')
list = ['hello','Hi']
json.dump(list, file)
file = open('filenhap.json')
print(json.loads(file.readline().strip('\n'))[1])
print(file.readline())
print(type(file.readline()))
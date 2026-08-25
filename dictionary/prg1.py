d={
    'name':'aasma',
    'age':22,
    'course':'ENTC'
}

#get()
c=d.get('name') #access keys using get fun
c1=d['name']# access key manualyy
print(c)
print(c1)

#keys():target key
for a in d.keys():
    print(a)

#values():target value
for a in d.values:
    print(a)

#items():target both key and value

for a,b in d.items():
    print(a,b)


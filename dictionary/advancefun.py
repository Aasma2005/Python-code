d={
    'name':'aasma',
    'age':22,
    'course':'ENTC'
}

#insert
d['year']=2026
print(d)

#update
d.update({'fees': 90})
print(d)

# you can also update like this
d['fees']=60000
print(d)
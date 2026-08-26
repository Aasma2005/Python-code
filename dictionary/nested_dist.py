course={
    'php':{'duration':'2 month', 'fees':5000},
    'python':{'duration':'5 month', 'fees':10000},
    'java':{'duration':'8 month', 'fees':15000}
    }    
print(course) 
print(course['python']) #only iterate python data
print(course['python']['fees']) #specific value iterate

for k,v in course.items():
    print(k,v)
    print(k,v['duration'],v['fees'])
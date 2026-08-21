#   0  1  2  3    4       5    index
l=[10,20,30,40,"hello",[1,2,3]]
# -6 -5 -4 -3    -2      -1 
print(type(l))

print(l[5][2])#[1,2,3] print 3 inside the list
print(l[2],l[3])# print 2 valse at a time
print(l[0:1])
print(l[0::2])
print(l[-1: :-1])
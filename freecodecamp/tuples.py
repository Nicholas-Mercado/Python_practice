d = {'b':1,'a':2260,'c':555,'d':2,'e':1}

# print(sorted(d.items()))

# for k,v in sorted(d.items()):
#   print(k,v)
  
x = sorted([(k,v) for v,k in d.items()])


print(x)
print (max(x))

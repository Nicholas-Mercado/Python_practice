

try:
  fhand = open('freecodecamp/mbox_s.txt', 'r')
except:
  print('File cannot be opened: ', fhand)
  quit()
    
# this just give you Io wrapper
# print(fhand)

# \n is for new lines
# x = 'x \ny'
# print(x)
# 

# count = 0
# for each line 'x' in file 'fhand'
# for x in fhand:
#   count += 1
# print('line count: ', count)

# inp = fhand.read()
# print(len(inp))

# print(inp[:20])

# for line in fhand:
#   if line.startswith('From:') :
#     line = line.rstrip()
#     if not 'uct.ac.za' in line:
#       continue
#     print(line)
    
# line_stripped = (x.rstrip() for x in fhand)
    
# lines = [line.rstrip() for line in fhand if line.startswith('From:')]

# email_from = [line for line in fhand if line.startswith('From:')]
# email_filter = [line for line in email_from  if not 'uct.ac.za' in line ]
# lines = '\n'.join([line.strip().lstrip('From:') for line in email_filter ])
# count = 0
# line_count = len([i for i in lines if i == '\n'])
# print('Email count: ', line_count)
# print(lines)

count = 0
for line in fhand:
  count+=1
  
count = [line for line in fhand]
print(count)


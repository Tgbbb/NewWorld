import re
str = r'1219abc'
p1=r'^[0-9]+abc$'
patt1 = re.compile(p1)
matc1 = re.search(patt1,str)
print(matc1.group(0))
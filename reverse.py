//by reverseing
a="hello"
print("".join(reversed(a)))

//by slicing
a="hell"
print(a[::-1])

//without reverse function
a="meghana"
str=""
for i in a:
    str=i+str
print(str)

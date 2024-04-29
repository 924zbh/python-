ls = ["a","b","c"]
for i in range(len(ls)):
    print(i,end="")
    print(ls[i])

for s in ls:
    print(ls.index(s),end="")
    print(s)

for i,s in enumerate(ls):
    print(i,end="")
    print(s)



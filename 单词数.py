Number = 0
word = False
countSpace = 0
strs=input("请输入字符串: ")
for i in range(len(strs)):
    ch=strs[i]
    if(ch ==""):word = False
    elif(not word):
        word = True
        Number+=1
print("单词有: ",Number)

    

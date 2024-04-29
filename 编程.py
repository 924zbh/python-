strs =input("请输入字符串：")
countLetter = 0;countNumber = 0;conutSpace = 0;countAll = 0;countOther = 0
for i in range(len(strs)):
    ch=strs[i]
    countAll+=1
    if(str.isalpha(ch)):countLetter+=1
    elif(str.isdigit(ch)):countNumber+=1
    elif(str.isspace(ch)):countSpace+=1
    else:countOther+=1
print("所有字母总数为: ",countAll)
print("英文字母出现的次数: ",countLetter)
print("数字出现的次数为: ",countNumber)
print("空格出现的次数为: ",conutSpace)
print("其他字符出现的次数为: ",countOther)

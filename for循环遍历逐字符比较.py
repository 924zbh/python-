def isPalindromic(str):
    for i in range(len(str)//2):
        if str[i]!=str[-i-1]:
            return False
    return True
str = input('请输入字符串:' )
if isPalindromic(str):
    print('{}是回文字符串'.format(str))
else:
    print('{}不是回文字符串'.format(str))

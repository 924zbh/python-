def isPalindromic(str):
    return str == str[::-1]
str = input('请输入字符串:' )
if isPalindromic(str):
    print('{}是回文字符串'.format(str))
else:
    print('{}不是回文字符串'.format(str))

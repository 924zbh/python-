def isPalindromic(str):
    if len(str) < 2:
        return True
    if str[0]!=str[-1]:
        return False
    return isPalindromic(str[1:-1])
str = input('请输入字符串:' )
if isPalindromic(str):
    print('{}是回文字符串'.format(str))
else:
    print('{}不是回文字符串'.format(str))

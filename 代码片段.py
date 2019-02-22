"""读取文件input并写入output"""
file1 = open('input.txt')
file2 = open('output.txt', 'w')

while True:
    line = file1.readline()
    file2.write(line)
    if not line:
        break

file1.close()
file2.close()


""""""
str1 = 'abcdef'
print(str1.lower())         #小写
print(str1.upper())         #大写
print(str1.capitalize())    #首字母大写



s = 'ni hao a'
res = ''
for i in s:
    if i == ' ':
        res += "%20"
    else:
        res += i
print(res)


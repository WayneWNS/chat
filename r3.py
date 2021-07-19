# 清單分割法
# 字串可以當作清單

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] # 取清單內第一筆資料的前五個字(不包含5)
    name = s[0][5:] # 取清單內第五筆以後所有字(包含5)
    print(name)
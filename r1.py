
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # 第一行pirnt 出會多出 '\ufeff' 的奇怪編碼，需要新增'-sig'
        chats = []
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None # 如果今天運行至append還未定義person,就會crash。所以要預設person。 
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue

        if person: # 如果person有值，才會加入清單
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f: # 重新寫入後可以不用再呼叫編碼
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()
import json, re


with open("./龙王：世界的重启.txt", 'r', encoding='utf-8') as f:
    data = f.read().split('\n')

ret = [["简介", []]]

for i, elem in enumerate(data):
    match = re.match(r"第\d+章", elem)
    elem = elem.strip()
    if match:
        ret.append([elem, []])
    else:
        if not elem: continue
        ret[-1][1].append(elem)

with open("龙王：世界的重启.json", "w", encoding="utf-8") as f:
    json.dump(ret, f, ensure_ascii=False, indent=4)
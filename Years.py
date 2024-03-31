import json

file = open("使用过的垃圾程序/hhh.txt", "r")
file1 = open("BoneSong.json", "w+")
info = file.read().split("\n")
info_dict = {}
for i in info:
    info_dict[i[:i.find(":")]] = str(i[i.find(":")+1:])

file1.seek(0)
json.dump(info_dict, file1, indent=4, ensure_ascii=False)
file1.truncate()
file1.close()
file.close()

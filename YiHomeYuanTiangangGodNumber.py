import json

import time


def CallTheBoneGodNumber(year_dict: dict, month_dict: dict, day_dict: dict, when_age: dict, info: list) -> str:
    try:
        file = open("YearsOfBirth.json", "r")
        s = json.load(file)
        file1 = open("BirthMonth.json", "r")
        s1 = json.load(file1)
        file2 = open("DaysOfBirth.json", "r")
        s2 = json.load(file2)
        file3 = open("TimeOfBirth.json", "r")
        s3 = json.load(file3)
        file4 = open("BoneSong.json", "r")
        s4 = json.load(file4)
        p = s[year_dict[int(info[0])][0]] + s1[month_dict[int(info[1])]] + s2[day_dict[int(info[2])]] + s3[
            when_age[int(info[3].find(":"))]]
        return s4[str(p)]
    except KeyError:
        assert "输入的时间不对"
        # print("输入的时间不对")
    except NameErro:
        print("格式错误！")


def CreateNnInformationDictionary():
    # 创建年号,年龄,属性
    TIMES = time.ctime(time.time())
    CELESTIAL_STEM = "甲乙丙丁戊己庚辛壬癸" * 60
    TERRESTRIAL_BRANCH = "子丑寅卯辰巳午未申酉戌亥" * 20
    infoODIAC = '鼠牛虎兔龙蛇马羊猴鸡狗猪' * 20
    SHU = 1924
    year_dict = {}
    # 创建年
    for i in range(len(TERRESTRIAL_BRANCH)):
        year_dict[SHU + i] = CELESTIAL_STEM[i] + TERRESTRIAL_BRANCH[i], int(TIMES[20:]) - (SHU + i), infoODIAC[i]
    # 创建月，日
    MONTH = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    DAY = ['初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十',
           '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
           '廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十']
    WHEN = ['丑时', '寅时', '卯时', '辰时', '巳时', '午时', '未时', '申时', '酉时', '戌时', '亥时', '子时']
    month_dict = {}
    day_dict = {}
    for i in range(len(DAY)):
        if i <= 11:
            month_dict[i + 1] = MONTH[i]
        day_dict[i + 1] = DAY[i]
    # 创建时
    when_age = {}
    shu_0 = 0
    shu_1 = 0
    for i in range(1, 25):
        if i % 2 == 0:
            when_age[i] = WHEN[shu_0]
            shu_0 += 1
        if i % 2 == 1:
            when_age[i] = WHEN[shu_1]
            shu_1 += 1
    return year_dict, month_dict, day_dict, when_age


def mina():
    while True:
        year_dict, month_dict, day_dict, when_age = CreateNnInformationDictionary()
        try:
            info = input('\n输入年月日时\n\033[1m\033[31m注意格式为2000/5/14/1:00: \033[0m').split('/')
            info_b = CallTheBoneGodNumber(year_dict, month_dict, day_dict, when_age, info)
            print(f"\n\033[1m\033[34m{'='*(len(info_b)+len(info_b))}\n|{info_b}|\n{'='*(len(info_b)+len(info_b))}\033[0m")

        except TypeError:
            print("输入有误！")


if __name__ == "__main__":
    mina()

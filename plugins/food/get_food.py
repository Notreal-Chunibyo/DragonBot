import random


async def get_pos(pos):
    print(pos)
    p = {'津南':['理科1楼', '理科2楼', '711', '文科1楼', '文科2楼', '原汁味', '外卖'],
         '八里台':['老陶包子','老王豆皮','武汉热干面','汉堡王','麻辣拌','麦当劳','肯德基','麻辣烫', '外卖'],
         '其他':['外卖']}
    i = random.randint(0, len(p[pos]) - 1)
    res = p[pos][i]
    return res
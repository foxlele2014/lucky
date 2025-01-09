import random
from datetime import datetime
import json
import os

def giveMeRichNums(normalNum, specialNum, normalCount, specialCount, isPrint = False):
  # nums = [random.randint(1, normalNum) for i in range(0, normalCount)]
  # specials = [random.randint(1, specialNum) for j in range(0, specialCount)]
  nums = random.sample(range(1, normalNum), normalCount)
  specials = random.sample(range(1, specialNum), specialCount)
  if isPrint:
    print(nums,specials)
  # nums.extend(specials)
  # 为了分区比较，所以分成两块数据返回
  return nums,specials

# giveMeFourNums(6)
# giveMeFourNums(8)
# giveMeFourNums(12)
# giveMeFourNums(20)
# giveMeFourNums(35)

# 一组数字。10，9，6， 11 
# richList = [10, 9, 6, 11]
# richList = [31, 6, 34, 22, 1, 35]

# choise 是可以从一个序列里随机选一个元素
# randint 是从一个数字区间范围里随机选一个元素
def guessRichCount(normalNum, specialNum, normalCount, specialCount, startList = None, endList = None):
  if startList is None:
    richList, specialRichList = giveMeRichNums(normalNum, specialNum, normalCount, specialCount, True)
  else:
    richList, specialRichList = startList, endList
  # flag = True
  # count = 0
  # while flag:
  #   startArr, endArr = giveMeRichNums(normalNum, specialNum, normalCount, specialCount)
  #   isSame = set(startArr) == set(richList)
  #   isSpecialSame = set(endArr) == set(specialRichList)
  #   count+=1
  #   if isSame and isSpecialSame:
  #     flag = False
  # print(count)
  # return count
  return f"{richList}" + f"{specialRichList}"

# 列表可以通过 == 来判断是否相等，但是这个只适合比较一维，且顺序一致的
# 集合可以比较无序的，一维的，但是假如有重复数字，就不太适合
# 可以借助numpy的array_equal 来比较，这个就适合多维，无序，重复
# print(set([1,2,3]) == set([3, 2,1]))

# random.randint(1, 12)

def giveNumByWeekDay():
  now = datetime.now()
  weekDay = now.weekday()
  today = now.strftime("%Y-%m-%d")
  month = now.strftime("%Y-%m")
  num = ''
  if weekDay == 0 or weekDay == 2 or weekDay == 5:
    num = guessRichCount(35, 12, 5, 2)
  elif weekDay == 1 or weekDay == 3 or weekDay == 6:
    num = guessRichCount(33, 16, 6, 1)
  else:
    print("今天不开奖")

  filePath = './files/' + month + '.json';
  # 确保目录存在
  os.makedirs(os.path.dirname(filePath), exist_ok=True)
  # 检查文件是否存在
  if os.path.exists(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
      data = json.load(f)
      data[today] = num
      with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
  else:
    with open(filePath, 'w', encoding='utf-8') as f:
      data = {today: num}
      json.dump(data, f, ensure_ascii=False)

  # 大乐透 5+2 (1-35, 1-12) （每周一、三、六晚上开奖）  
  # guessRichCount(35, 12, 5, 2)
  # 双色球 6+1 （1-33， 1-16） （每周二、四、日晚上开奖）
  # guessRichCount(33, 16, 6, 1)


giveNumByWeekDay()

# 还需要再改善一下，不能全部数字一起比较，得分区比较
# 然后分区比较的时候忽略顺序
# 生成的随机数需要判断是否有重复，不能出现重复的
# 怎么传一个可选参数，现在我加了这个参数，但是不传会报错

# [5, 20, 21, 22, 32, 3, 4]

# 使用cursor优化代码

#1. 使用 `random.sample()` 替代 `random.randint()` 已经很好，因为它可以确保不会生成重复数字
# 添加输入验证
# 优化打印输出格式
# 添加注释说明

# 添加了输入参数验证，确保选择的数字个数不超过范围
# 优化了打印格式，使用 f-string 使输出更清晰
# 3. 对数字进行排序显示，便于阅读
# 4. 添加了函数文档字符串(docstring)说明参数含义
# 使用 while True 替代 flag 变量，代码更简洁
# 6. 使用千位分隔符格式化大数字输出
# 改进了测试用例的输出格式
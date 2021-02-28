import datetime
import random


with open('todo.txt','a',encoding='utf8') as file:
    random_num = random.randint(1,10000)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.writelines("当前时间：{} 随机数值：{}\n".format(current_time, random_num))

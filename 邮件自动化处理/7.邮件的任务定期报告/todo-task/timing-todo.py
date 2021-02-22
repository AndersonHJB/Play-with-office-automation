import datetime
import random
from send_qq_mail import send_mail

with open('todo.txt','a',encoding='utf8') as file:
    random_num = random.randint(1,10000)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.writelines("当前时间：{} 随机数值：{}\n".format(current_time, random_num))
    subject = "定期任务执行完成"
    contents = "当前时间：{} 随机数值：{}\n".format(current_time, random_num)
    send_mail(subject,contents)

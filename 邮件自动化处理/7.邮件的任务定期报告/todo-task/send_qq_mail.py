import yagmail


def send_mail(subject,contents):
    yag = yagmail.SMTP(user='givemefive94@qq.com', password='***********************', host='smtp.qq.com')
    yag.send(to='givemefive94@qq.com', subject=subject, contents=contents)
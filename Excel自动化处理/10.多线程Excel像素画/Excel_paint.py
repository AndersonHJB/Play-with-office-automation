# coding: utf-8

import xlsxwriter
from PIL import Image
import os
from concurrent import futures


def paint_excel(filename):
    print("开始处理{}".format(filename))
    wb = xlsxwriter.Workbook(filename+'.xlsx')
    ws = wb.add_worksheet('sheet1')

    img = Image.open(filename)
    imgL = img.convert("P").convert("RGB")
    pix = imgL.load()
    w, h = imgL.size

    def RGB_to_Hex(tmp):
        rgb = list(tmp)
        strs = '#'
        for i in rgb:
            num = int(i)
            strs += str(hex(num))[-2:].replace('x','0').upper()
        return strs

    for i in range(w):
        for j in range(h):
            rgb = pix[i,j]
            color = RGB_to_Hex(rgb)
            style = wb.add_format({'bg_color': '{}'.format(color)})
            ws.write(j,i,'',style)
            ws.set_row(j,1)
    ws.set_column(0,w-1,0.5)

    wb.close()
    print("处理完成，文件名{}".format(filename),'\n')


if __name__ == "__main__":
    path = os.getcwd()+'\course'

    # 单线程
    # for filename in os.listdir('./course'):
    #     full_path_filename = os.path.join(path,filename)
    #     print(full_path_filename)
    #     paint_excel(full_path_filename)

    # 多线程
    tasklist = [os.path.join(path,filename) for filename in os.listdir('./course')]
    with futures.ThreadPoolExecutor(len(tasklist)) as executor:
        executor.map(paint_excel, tasklist)
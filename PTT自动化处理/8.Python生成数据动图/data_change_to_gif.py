import matplotlib.pyplot as plt
import pandas as pd
import imageio

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

images = []

df = pd.read_excel('近20年中国省市县个数数据.xls')

for i in range(len(df.columns)-1,-1,-1):
    tmp_df = df.iloc[:, i]
    title = tmp_df.name
    print("读取{}数据".format(title))
    tmp_df.plot.barh(xlim=(0,3000),title="{}中国省市县的个数".format(title))
    plt.savefig("tmp.png")
    plt.close('all')
    im = imageio.imread("tmp.png")
    images.append(im)

imageio.mimsave('近20年中国省市县个数数据.gif', images, 'GIF', duration=round(0.5, 2))


# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:16:26 2017
@author: gaofeng

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl 
f= pd.read_csv(r"C:\Users\gaofeng\Desktop\data\datacut.csv",encoding = 'utf-8')

#性别分布
def Gender_distribution():
    plt.bar(range(2),f.性别.value_counts())
    plt.title('11、12级学生性别分布情况')
    plt.ylabel('学生数量')
    plt.xlabel('性别')
    plt.xticks(range(2),['男','女'])
    for x,y in zip(range(2),f.性别.value_counts()):
        plt.text(x,y+10,y,ha='center')
    plt.show()


#11、12级学生延期分布情况
def Extension():
    plt.bar(range(2),f.是否延期.value_counts())
    plt.title('11、12级学生延期分布情况')
    plt.ylabel('学生数量')
    plt.xlabel('是否延期')
    plt.xticks(range(2),['否','是'])
    length = len(f)
    for x,y in zip(range(2),f.是否延期.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/length) * 100)),ha='center')
    plt.show()
        

#11、12级城乡生源分布情况    
def Life_status():
    plt.bar(range(5),f.城乡生源.value_counts())
    plt.title('11、12级城乡生源分布情况')
    plt.ylabel('学生人数')
    plt.xlabel('城乡等级分布')
    plt.xticks(range(5),['乡镇','县（县级市）','地级市','省会城市','缺失数据'])
    length = len(f)
    for x,y in zip(range(5),f.城乡生源.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/length) * 100)),ha='center')
    plt.show()


#11、12级所在院系分布情况
def School_system():
    plt.bar(range(7),f.所在院系.value_counts())
    plt.title('11、12级所在院系分布情况')
    plt.ylabel('学生人数')
    plt.xlabel('所在院系')
    plt.xticks(range(7),['经管系','地科系','工程系','信息系 ','仪器系','人文系','外语系'])
    length = len(f)
    for x,y in zip(range(7),f.所在院系.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/length) * 100)),ha='center')
    plt.show()

#11、12级学生毕业后是否重点单位
def Keyunits():
    plt.bar(range(2),f.是否重点单位.value_counts())
    plt.title('11、12级学生毕业是否重点单位')
    plt.ylabel('学生数量')
    plt.xlabel('是否重点单位')
    plt.xticks(range(2),['否','是'])
    length = len(f)
    for x,y in zip(range(2),f.是否延期.value_counts()):
        plt.text(x,y+160,str('%.2f%%'%((y/length)*100)),ha = 'center')
    plt.show()


#11、12级学生毕业去向
def Graduation_destination():
    plt.figure(figsize = (15,6))
    plt.bar(range(11),f.毕业去向代码.value_counts())
    plt.title('11、12级毕业去向分布情况')
    plt.ylabel('学生人数')
    plt.xlabel('毕业去向')
    plt.xticks(range(11),['其他录用','签就业协议','升学','签劳动合同 ','待就业','出国','义务兵','创业','地方基层项目','国家基层项目','缺失'])
    length = len(f)
    for x,y in zip(range(11),f.毕业去向代码.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/length) * 100)),ha='center')
    plt.show()
    

#延期情况与性别分布
def Gender_extension_distribution():
    frame1 = f[f.性别=='男']
    frame2 = f[f.性别=='女']
    rect1 = plt.bar(np.arange(2),frame1.是否延期.value_counts(),width = 0.3)
    rect2 = plt.bar(np.arange(2)+0.3,frame2.是否延期.value_counts(),width = 0.3)
    plt.title('11、12级延期情况与性别分布')
    plt.ylabel('学生数量')
    plt.xlabel('是否延期')
    plt.xticks(range(2),['否','是'])
    for x,y in zip(range(2),frame1.是否延期.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/len(frame1)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame2.是否延期.value_counts()):
        plt.text(x+0.3,y+10,str('%.2f%%' % (( y/len(frame2)) * 100)),ha = 'center')
    plt.legend([rect1, rect2], ['男', '女'], loc='upper right', scatterpoints=1)
    plt.show()


#城乡背景与延期分布
def Background_extension():
    frame1 = f[f.城乡生源==4.0]
    frame2 = f[f.城乡生源==3.0]
    frame3 = f[f.城乡生源==2.0]
    frame4 = f[f.城乡生源==1.0]
    rect1 = plt.bar(np.arange(2),frame1.是否延期.value_counts(),width = 0.15)
    rect2 = plt.bar(np.arange(2)+0.15,frame2.是否延期.value_counts(),width = 0.15)
    rect3 = plt.bar(np.arange(2)+0.3,frame3.是否延期.value_counts(),width = 0.15)
    rect4 = plt.bar(np.arange(2)+0.45,frame4.是否延期.value_counts(),width = 0.15)
    plt.title('11、12级城乡生源与延期分布')
    plt.ylabel('学生数量')
    plt.xlabel('是否延期')
    plt.xticks(range(2),['否','是'])
    for x,y in zip(range(2),frame1.是否延期.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/len(frame1)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame2.是否延期.value_counts()):
        plt.text(x+0.15,y+10,str('%.2f%%' % (( y/len(frame2)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame3.是否延期.value_counts()):
        plt.text(x+0.3,y+10,str('%.2f%%' % (( y/len(frame3)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame4.是否延期.value_counts()):
        plt.text(x+0.45,y+10,str('%.2f%%' % (( y/len(frame4)) * 100)),ha = 'center')
    plt.legend([rect1, rect2, rect3, rect4], ['省会城市', '地级市','县（县级市）','乡镇'], loc='upper right', scatterpoints=1)
    plt.show()
        
#系部与延期分布
def Department_extension():
    plt.figure(figsize =(9,5))
    frame1 = f[f.所在院系=='1地科系']
    frame2 = f[f.所在院系=='2工程系']
    frame3 = f[f.所在院系=='3仪器系']
    frame4 = f[f.所在院系=='4信息系']
    frame5 = f[f.所在院系=='5经管系']
    frame6 = f[f.所在院系=='6人文系']
    frame7 = f[f.所在院系=='7外语系']
    plt.xticks(range(2),['否','是'])
    plt.ylabel('学生数量')
    plt.xlabel('是否延期')
    rect1 = plt.bar(np.arange(2),frame1.是否延期.value_counts(),width = 0.1)
    rect2 = plt.bar(np.arange(2)+0.1,frame2.是否延期.value_counts(),width = 0.1)
    rect3 = plt.bar(np.arange(2)+0.2,frame3.是否延期.value_counts(),width = 0.1)
    rect4 = plt.bar(np.arange(2)+0.3,frame4.是否延期.value_counts(),width = 0.1)
    rect5 = plt.bar(np.arange(2)+0.4,frame5.是否延期.value_counts(),width = 0.1)
    rect6 = plt.bar(np.arange(2)+0.5,frame6.是否延期.value_counts(),width = 0.1)
    rect7 = plt.bar(np.arange(2)+0.6,frame7.是否延期.value_counts(),width = 0.1)
    for x,y in zip(range(2),frame1.是否延期.value_counts()):
        plt.text(x,y+10,str('%.2f%%' % (( y/len(frame1)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame2.是否延期.value_counts()):
        plt.text(x+0.1,y+10,str('%.2f%%' % (( y/len(frame2)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame3.是否延期.value_counts()):
        plt.text(x+0.2,y+10,str('%.2f%%' % (( y/len(frame3)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame4.是否延期.value_counts()):
        plt.text(x+0.3,y+10,str('%.2f%%' % (( y/len(frame4)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame5.是否延期.value_counts()):
        plt.text(x+0.4,y+10,str('%.2f%%' % (( y/len(frame5)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame6.是否延期.value_counts()):
        plt.text(x+0.5,y+10,str('%.2f%%' % (( y/len(frame6)) * 100)),ha = 'center')
    for x,y in zip(range(2),frame7.是否延期.value_counts()):
        plt.text(x+0.6,y+10,str('%.2f%%' % (( y/len(frame7)) * 100)),ha = 'center')
        plt.legend([rect1, rect2, rect3, rect4, rect5, rect6, rect7], ['1地科系','2工程系','3仪器系','4信息系','5经管系','6人文系','7外语系'], loc='upper right', scatterpoints=1)
    plt.show()
    
def Data_standardization():   #数据标准化
    data = f[['大一上','大一下','大二上','大二下','大三上','大三下','大四上','大四下','大五上','大五下',
   '平均成绩','2011年11月午','2011年12月午','2012年1月午','2012年3月午','2012年4月午','2012年5月午',
   '2012年6月午','2012年9月午','2012年10月午','2012年11月午','2012年12月午','2013年1月午','2013年3月午',
   '2013年4月午','2013年5月午','2013年6月午','2013年9月午','2013年10月午','2013年11月午','2013年12月午',
   '2014年1月午','2014年3月午','2014年4月午','2014年5月午','2014年6月午','2014年9月午','2014年10月午',
   '2014年11月午','2014年12月午','2015年1月午','2015年3月午','2015年4月午','2015年5月午','2015年6月午',
   '2015年9月午','2015年10月午','2015年11月午','2015年12月午','第一学期','第七学期','第三学期','第九学期',
   '第二学期','第五学期','第八学期','第六学期','第十学期','第四学期']]
    for i in data:
        mean = f[i].mean()
        std = f[i].std()
        f[i] = (f[i]-mean)/std
        f.to_csv(r"C:\Users\gaofeng\Desktop\data\datacut_finally.csv",encoding = 'utf-8')

def normfun(x,mu,sigma):#正态分布
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
def Gaosi_extension(n):   #正态分布直方图
    data = f[n]
    plt.hist(data.dropna(),bins =10,rwidth = 0.9,normed = True)
    plt.title(n+'学生成绩正态分布直方图')
    plt.xlabel("学生分数")
    plt.show()
    
#d3=f['大二下'].corr(f['第二学期'])   计算的相关系数
        
    
def Corr_gender_internet_grade():  #每个学期性别与网费和成绩的相关性
    df= pd.read_csv(r"C:\Users\gaofeng\Desktop\data\datacut_finally.csv",encoding = 'utf-8')
    data1 = df[df['性别']=='男']
    data2 = df[df['性别']=='女']
    print("男生每个学期网费和成绩的相关性：")
    d1 = data1['大一上'].corr(data1['第一学期'])
    print("大一上",d1)
    d2 = data1['大一下'].corr(data1['第二学期'])
    print("大一下",d2)
    d3 = data1['大二上'].corr(data1['第三学期'])
    print("大二上",d3)
    d4 = data1['大二下'].corr(data1['第四学期'])
    print("大二下",d4)
    d5 = data1['大三上'].corr(data1['第五学期'])
    print("大三上",d5)
    d6 = data1['大三下'].corr(data1['第六学期'])
    print("大三下",d6)
    d7 = data1['大四上'].corr(data1['第七学期'])
    print("大四上",d7)
    d8 = data1['大四下'].corr(data1['第八学期'])
    print("大四下",d8)
    print("女生每个学期网费和成绩的相关性：")
    d1 = data2['大一上'].corr(data2['第一学期'])
    print("大一上",d1)
    d2 = data2['大一下'].corr(data2['第二学期'])
    print("大一下",d2)
    d3 = data2['大二上'].corr(data2['第三学期'])
    print("大二上",d3)
    d4 = data2['大二下'].corr(data2['第四学期'])
    print("大二下",d4)
    d5 = data2['大三上'].corr(data2['第五学期'])
    print("大三上",d5)
    d6 = data2['大三下'].corr(data2['第六学期'])
    print("大三下",d6)
    d7 = data2['大四上'].corr(data2['第七学期'])
    print("大四上",d7)
    d8 = data2['大四下'].corr(data2['第八学期'])
    print("大四下",d8)
    
    
    
    
    
#    print(data1['大一上'].corr(data1['第一学期'])
    
f= pd.read_csv(r"C:\Users\gaofeng\Desktop\data\data_final.csv",encoding = 'utf-8')   
mpl.rcParams['font.sans-serif'] = ['SimHei']
#Gender_distribution()  #性别分布
#Extension()#11、12级学生性别分布情况
#Life_status()#11、12级城乡生源分布情况    
#School_system()#11、12级所在院系分布情况
#Keyunits()#11、12级学生毕业后是否重点单位
#Graduation_destination()#11、12级学生毕业去向
#
#Gender_extension_distribution()#延期情况与性别分布
#Background_extension()#城乡背景与延期分布
#Department_extension()#系部与延期分布
Gaosi_extension('大四下')
Corr_gender_internet_grade()













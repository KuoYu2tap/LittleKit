# -*- coding: UTF-8 -*-
#py 3.X
import re
import string
from tkinter.filedialog import askopenfilename
from tkinter import *

#建立元组，其中套用数组
NameClass= {
    '1':(['周一'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '2':(['周二'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '3':(['周三'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '4':(['周四'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '5':(['周五'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '6':(['周六'],[],[],[],[],[],[],[],[],[],[],[],[]),
    '7':(['周日'],[],[],[],[],[],[],[],[],[],[],[],[])
}

 

#打开文件，传递课程数据;source
def OpenFile(in_filename):                       
    File = open(in_filename)
    source =  File.read()
    File.close()
    
    source = source.replace('周一第','周1第')                                          #进行数据替换，方便正则匹配
    source = source.replace('周二第','周2第')
    source = source.replace('周三第','周3第')
    source = source.replace('周四第','周4第')
    source = source.replace('周五第','周5第')
    source = source.replace('周六第','周6第')                    #希望没人名为 周[一到五]第XD
    stu_name = re.findall('(?<=姓名：)[\w]*', source)
    Name = stu_name[0]                                                                     #Name为正则处理后的 姓名
    Stu_Class_Lesson =re.findall("周(\d)?第(\d,[\d{1,2}]*)?节({.{0,9}})?",source)           #Stu_Class_Lesson为正则处理后的课程list

    def Add_Name(in_x, in_name):
        if Class_2_Lesson == '':
            in_x_1 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_1_Lesson)]
            if in_name not in in_x_1:
                in_x_1.append(in_name)
        elif Class_3_Lesson ==  '':
            in_x_1 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_1_Lesson)]
            in_x_2 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_2_Lesson)]
            if in_name not in in_x_1:
                in_x_1.append(in_name)
            if in_name not in in_x_2:
                in_x_2.append(in_name)
        elif Class_2_Lesson != '' and  Class_3_Lesson !=  '':
            in_x_1 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_1_Lesson)]
            in_x_2 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_2_Lesson)]
            in_x_3 = NameClass[Stu_Class_Lesson[in_x][0]][int(Class_3_Lesson)]
            if in_name not in in_x_1:
                in_x_1.append(in_name)
            if in_name not in in_x_2:
                in_x_2.append(in_name)
            if in_name not in in_x_3:
                in_x_3.append(in_name)

    for x in range(0,len(Stu_Class_Lesson)):            #对1,2节课 or 1,2,3节课 or 9,10,11节课.... 多种情况进行处理。虽然冗杂但不可少？
        if len(Stu_Class_Lesson[x][1]) == 1:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson =  ''
            Class_3_Lesson =  ''
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 3:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson =Stu_Class_Lesson[x][1][2]
            Class_3_Lesson =  ''
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 4:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson =Stu_Class_Lesson[x][1][2] + Stu_Class_Lesson[x][1][3]
            Class_3_Lesson =  ''
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 5 and Stu_Class_Lesson[x][1][2]== ',':
            Class_1_Lesson = Stu_Class_Lesson[x][1][0] +  Stu_Class_Lesson[x][1][1]
            Class_2_Lesson = Stu_Class_Lesson[x][1][3] + Stu_Class_Lesson[x][1][4]
            Class_3_Lesson =  ''
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 5 and Stu_Class_Lesson[x][1][1]== ',':
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson = Stu_Class_Lesson[x][1][2]
            Class_3_Lesson = Stu_Class_Lesson[x][1][4]
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 6:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson = Stu_Class_Lesson[x][1][2]
            Class_3_Lesson = Stu_Class_Lesson[x][1][4] + Stu_Class_Lesson[x][1][5]
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 7:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0]
            Class_2_Lesson = Stu_Class_Lesson[x][1][2] + Stu_Class_Lesson[x][1][3]
            Class_3_Lesson = Stu_Class_Lesson[x][1][5] + Stu_Class_Lesson[x][1][6]
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        elif len(Stu_Class_Lesson[x][1]) == 8:
            Class_1_Lesson = Stu_Class_Lesson[x][1][0] + Stu_Class_Lesson[x][1][1]
            Class_2_Lesson = Stu_Class_Lesson[x][1][3] + Stu_Class_Lesson[x][1][4]
            Class_3_Lesson = Stu_Class_Lesson[x][1][6] + Stu_Class_Lesson[x][1][7]
            Add_Name(x, Name+' '+Stu_Class_Lesson[x][2])
        else:
            print('error, 联系管理员吧\n'+Stu_Class_Lesson[x][1])


##print("Please input your command:(input 'quit' let u out)(input 'go' continue)")
##temp = input()
##while temp == "go":
##    filename = askopenfilename(filetypes=[("text file", "*.txt"),("htm file","*.htm"),("html file","*.html")])
##    OpenFile(filename)
##    print("已加载" + filename)
##    print("Please input your command again. ('quit' to quit)('go' to go)")
##    temp = input()

def OF():
    filename = askopenfilename(filetypes=[("text file", "*.txt"),("htm file","*.htm"),("html file","*.html")])
    OpenFile(filename)
    print("已加载" + filename)

    ##IDLE直接输出
    for week_flag in range(1,8):
        for lesson_flag in range(0,12):
            print(str(NameClass[str(week_flag)][lesson_flag])+"\n")
        print("\n\n\n")

    ##写入版本
    f = open(r'NameClass.txt','w')
    for week_flag in range(1,8):
        for lesson_flag in range(0,12):
            f.write(str(NameClass[str(week_flag)][lesson_flag])+"\n")
        f.write("\n\n\n")
    f.close()

root = Tk()
root.title("课表处理")
Button(root , text = "加载",width=4,bd=2,fg='blue',command=OF).pack()
root.mainloop()    

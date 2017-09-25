#coding:utf-8
#Author:KuoYu

def caclulate_hex(OctNum):
    #对十进制处理，返回check二进制,并有前四位num
    HexNum_str= hex(OctNum)[2:]
    while(len(HexNum_str)!=4):
        HexNum_str = '0' + HexNum_str
    HexNum_num = HexNum_str[-2:]+HexNum_str[-4:-2]
    HexNum_checkout = bin(int(HexNum_num,16))[2:]
    while(len(HexNum_checkout)!=16):
        HexNum_checkout ='0'+HexNum_checkout
        
    #对前四位num的二进制数计算Xor,得second
    HexNum_sec = ''
    for i in range(len(HexNum_checkout)):
        if HexNum_checkout[i] == '1':
            HexNum_sec = HexNum_sec + '0'
        else:
            HexNum_sec = HexNum_sec + '1'
            
    HexNum_sec = hex(int(HexNum_sec,2))[2:]
    
    #处理sec16进制时仅有3位
    if len(HexNum_sec)==3:
        HexNum_sec = '0'+HexNum_sec
        
    #返回第一扇区的值
    putHexNum = HexNum_num + '0000' + HexNum_sec
    return putHexNum

while(True):
    OctNum_in = input(u"请输入你的数据(例如100.00输入10000)")
    while(len(str(OctNum_in))<3 & OctNum_in <= 65500):
        OctNum_in= input(u"请输入你的数据(例如100.00输入10000)")
    print u"你需要的数字为:"+caclulate_hex(OctNum_in) 

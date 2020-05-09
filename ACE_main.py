import os
import Head
import Input as i
import Production as pro
import Output as o

info = Head.Info()
#调用Input()函数，和用户交互，获取输入信息
i.Input(info)

num = info.num_t
for j in range(0,num):
    #如果有多个温度，先确定温度点和对应的ACE文件后缀名
    temp = str(info.temperature[j])
    acename=str(info.ACEname[j])

    # message_total文件负责记录一次加工的所有信息，先清空
    message_total_file = info.note_path +'meassage_total_'+ temp+'K'
    message_total = open(message_total_file, 'w')
    # 清空xsdir之前的信息
    xsdir_file=info.output_path+'xsdir_'+temp+'K'
    xsdir = open(xsdir_file, 'w')

    # 将输入文件中的所有核素名建一个列表
    inputfiles = os.listdir(info.input_path)

    # 开始循环
    for file in inputfiles:
        #加工对应核素的对应温度的ACE文件
        pro.produce(info,file,acename,temp,message_total)
        nuclide=pro.nuclide
        #output()函数用于输出ace文件和xsdir
        o.output(info,nuclide,temp,acename)
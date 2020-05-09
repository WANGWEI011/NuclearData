import os,subprocess
import Note
import function as f
import Card_neutron as n
def writebat(productionpath,p_true):
    bat = open(productionpath + 'run.bat', 'w')  # 覆盖原有内容
    bat.write("NJOY2016.exe < Card.njoy")
    bat.close()

def produce(info,file,acename,temp,message_total):
    ENDFname = info.ENDFname
    input_path = info.input_path
    production_path = info.production_path
    note_path = info.note_path
    # 分离文件名,filename[0]就是分离后的文件名
    filename = os.path.splitext(file)
    global nuclide
    nuclide = filename[0]
    # 判断核素是否在裂变核素集合、true核素集合，是返回1，否返回0
    p_true = f.f_true(ENDFname, nuclide)
    p_fission = f.f_fission(ENDFname, nuclide)
    # 复制ENDF文件file_1到tape21
    file_i = input_path + file
    tape21 = production_path + 'tape21'
    f.copyfile(file_i, tape21)
    # 提取核素的MAT编号
    MAT = f.getMAT(tape21, ENDFname)
    # 写NJOY2016的输入卡
    n.Card_neutron(info,nuclide, acename, MAT, temp, p_fission)
    # note_card()函数的功能是建立存档文件card，备份NJOY输入卡
    Note.note_card(production_path, note_path, nuclide, temp)
    # note_message()函数的功能是建立存档文件message，备份输入卡和加工过程中的报错信息
    Note.note_message(production_path, note_path, nuclide, temp)

    message = Note.message

    # 写bat命令行
    writebat(production_path, p_true)
    # 调用cmd，运行run.bat，从而运行NJOY
    os.chdir(production_path)
    p = subprocess.Popen("cmd.exe /c" + production_path + "run.bat abc", stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    # 输出NJOY程序窗口返回的信息
    curline = p.stdout.readline()
    while (curline != b''):
        print(curline)
        message_total.write(str(curline) + '\n')
        message.write(str(curline) + '\n')
        curline = p.stdout.readline()
    p.wait()
    print(p.returncode)
    return 0;
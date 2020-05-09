class Info():
    # 变量default控制脚本的工作模式，默认值0，即工作在默认模式
    default = 0
    # 变量mode，控制加工模式，默认值0，加工中子数据
    mode = 0
    # 变量neutron，控制中子数据的加工要求，默认值0，对应加工中子数据+概率表+释热率
    neutron = 0
    # 变量muti，控制多线程开启的开关，默认值0，即默认不开启多线程
    muti = 0
    # 如果开启多线程，num_thread为线程数量，默认值为1
    num_thread = 1
    # 变量ENDFname决定使用哪个评价数据库，默认使用ENDF8.0评价数据库
    ENDFname = 'ENDF8.0'
    # 变量num_t是温度点数量，默认值是1个温度点
    num_t = 1
    # 数组temperature[]用于储存所有温度点
    temperature = []
    # 数组ACEname[]用于存储所有的ACE文件后缀
    ACEname = []
    # 变量path为ACEProduce文件夹的路径
    path = 'D:/ACEProduce/'

    input_path = path + 'input/' + ENDFname + '/'
    production_path = path + 'production/'
    output_path = path + 'output/' + ENDFname + '/'
    note_path = path + 'note/' + ENDFname + '/'

class Nuclide_Info():
    def __init__(self,nuclide='-1',MAT=-1,p_fission=-1,temp=-1,acename='-1'):
        self.nuclide = nuclide
        self.MAT = MAT
        self.p_fission = p_fission
        self.temp = temp
        self.acename = acename
    def print_all(self):
        print("加工核素为："+self.nuclide)
        print("MAT编号为：" + self.MAT)
        print("是否为裂变核素：" + self.p_fission)
        print("加工温度为" + self.temp+"K")
        print("ACE文件后缀名为：" + self.acename)
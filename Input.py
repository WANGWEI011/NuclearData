import os
# Input()函数用于和用户交互，获取输入信息
def Input(info):
    #确认加工文件的路径，检查必要的文件
    print("脚本加工文件默认存放在D:/ACEProduce/目录下面，\n"
          "如果要修改文件路径，请输入1.\n"
          "输入值          工作模式\n"
          "默认值          默认目录\n"
          "1               手动输入目录\n"
          "默认值:输入回车键或任意值。")
    path_check = input("是否修改目录：")
    if path_check == '1':
        info.path=input("如果新的文件目录为E：/wangwei/.../ACEProduce/,则输入\n"
                              "E：/wangwei/.../ACEProduce/,请输入新的文件目录：")

    #确认脚本的工作模式
    print("*****************************************************************************")
    print("脚本有两种工作模式，为了简化输入，最常用的操作被设置为默认模式。\n"
          "默认模式加工中子数据(概率表、释热率、气体)，单线程，只有一个温度。\n"
          "对应关系如下：\n"
          "输入值          工作模式\n"
          "默认值          默认模式\n"
          "1               开发模式\n"
          "默认值:输入回车键或任意值。")
    info.default = input("请选择工作模式：")
    if info.default !='1':
        info.mode = 0
        info.neutron = 0
        info.muti = 0
        info.num_thread = 1
        num_t = 1
    elif info.default=='1':
        print("使用开发模式，请按照提示依次设置参数！")

        # 确认要加工的数据类型
        print("*****************************************************************************")
        print("使用输入值控制使用的不同的加工功能，对应关系如下：\n"
              "输入值          功能名称\n"
              "默认值          加工中子数据(概率表、释热率)\n"
              "1               加工热化数据\n"
              "2               加工光核数据\n"
              "3               编辑模式\n"
              "默认值:输入回车键或任意值。")
        info.mode = input("请选择加工功能：")
        if info.mode != '1' and info.mode != '2' and info.mode != '3':
            info.mode = 0;
        else:
            info.mode = int(info.mode)

        # 如果是加工中子数据，确认加工中子数据的详细要求
        if info.mode == 0:
            print("*****************************************************************************")
            print("加工中子数据时，默认加工中子数据+概率表+释热率。\n"
                  "对应关系如下：\n"
                  "输入值          加工的中子数据\n"
                  "默认值          中子数据(概率表、释热率)\n"
                  "1               中子数据\n"
                  "2               中子数据(概率表)\n"
                  "3               中子数据(释热率)\n"
                  "默认值:输入回车键或任意值。")
            info.neutron = input("请选择加工的中子数据类型：")
            if info.neutron != '1' and info.neutron != '2' and info.neutron != '3':
                info.neutron = 0;
            else:
                info.neutron = int(info.neutron)

        # 加工大量中子数据时，可开启多线程计算功能，以节约计算时间
        if info.mode == 0:
            print("*****************************************************************************")
            print("加工中子数据时，可以选择使用并行功能。\n"
                  "对应关系如下：\n"
                  "输入值          是否使用多线程\n"
                  "默认值          单线程\n"
                  "1               多线程\n"
                  "默认值:输入回车键或任意值。")
            info.muti = input("请选择是否使用多线程：")
            if info.muti != '1':
                info.muti = 0;
            else:
                info.muti = int(info.muti)
        if info.muti == 1:
            info.num_thread = input("请输入线程数量：")
            info.num_thread = int(info.num_thread)
            if info.num_thread < 1:
                print("线程数量错误！")

        # 确认温度点数量
        info.num_t = input("请输入温度点数量：")
        info.num_t = int(info.num_t)
        if info.num_t < 1:
            print("温度点数量错误！")


    #选择使用的评价数据库
    print("*****************************************************************************")
    print("使用输入值控制使用的数据库，对应关系如下：\n"
          "输入值          评价数据库名称\n"
          "默认值          ENDF8.0\n"
          "1               ENDF7.0\n"
          "2               JEFF3.3\n"
          "默认值:输入回车键或任意值。")
    num_ENDF = input("请选择数据库：")
    if num_ENDF == '1':
        info.ENDFname = 'ENDF7.0'
    elif num_ENDF == '2':
        info.ENDFname = 'JEFF3.3'
    else:
        info.ENDFname = 'ENDF8.0'

    #输入温度点和后缀名
    if info.num_t == 1:
        temp = input("例如温度为300K，则输入300。\n"
                     "请输入温度：")
        info.temperature = [temp]
        ace = input("例如ACE文件名后缀为.70c，则输入70。\n"
                        "请输入ACE文件名后缀：")
        ace = int(ace)
        info.ACEname = [ace]
    else:
        print("*****************************************************************************")
        print("多温度点情况可以采用两种输入方法，例如温度为300K,310,......,390K的情况：\n"
              "等间距输入：初始温度输入300，间距输入10\n"
              "例如温度为0.1K,300K,......,10000K\n"
              "枚举输入：依次输入0.1,300,......,10000\n"
              "输入值          输入方式\n"
              "默认值          枚举输入\n"
              "1               等间距输入\n"
              "默认值:输入回车键或任意值。")
        input_method = input("请确定输入方式：")
        if input_method!='1':
            for k in range(0,num_t):
                num = input("请输入第"+str(k+1)+"个温度点，如300或1E4：")
                info.temperature.append(num)
            print(str(num_t)+"个温度点输入完成！")
        else:
            first_temp = input("请输入初始温度：")
            first_temp = float(first_temp)
            step = input("请输入温度间距：")
            step = float(step)
            for k in range(0,num_t):
                num = first_temp+k*step
                if num%1 == 0.0:
                    num = int(num)
                info.temperature.append(num)
        print("例如温度为300K,310,......,390K的情况，对应的ACE文件\n"
              "后缀名应该为：.80c,.81c,......,.89c。\n"
              "输入首个温度点ACE文件的后缀名80，其余后缀自动加1生成。")
        first_ace = input("请输入首个温度点后缀名：")
        first_ace = int(first_ace)
        for k in range(0, num_t):
            ace= first_ace + k
            info.ACEname.append(ace)

    path = info.path
    ENDFname = info.ENDFname
    # 确认输入文件地址
    input_path = path + 'input/' + ENDFname + '/'
    if not os.path.exists(input_path):
        os.makedirs(input_path)
    # 确认加工文件地址
    production_path = path + 'production/'
    if not os.path.exists(production_path):
        os.makedirs(production_path)
    # 确认输出文件地址
    output_path = path + 'output/' + ENDFname + '/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # 确认存档文件地址
    note_path = path + 'note/' + ENDFname + '/'
    if not os.path.exists(note_path):
        os.makedirs(note_path)
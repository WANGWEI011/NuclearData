import os,shutil,subprocess

#首先封装好一个复制函数，其功能是将srcfile复制到dstfile
def copyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))
        #message_total.write("copy %s -> %s" % (srcfile, dstfile) + "\n")

#由于NJOY2016源代码RECONR的BW,RM参数开关设置不同，可以编译出“NJOY2016BWfalseRMfalse.exe”和
#“NJOY2016BWtrueRMtrue.exe”两个版本，部分核素使用false版本的NJOY2016无法加工，需要使用true版
#本的NJOY2016程序。因此存储了不同版本ENDF评价数据库中，使用true版本的核素名单。
true_ENDF7=['n-013_Al_027','n-014_Si_028','n-014_Si_029','n-014_Si_030','n-024_Cr_050',
            'n-024_Cr_052','n-024_Cr_053','n-024_Cr_054','n-026_Fe_054','n-026_Fe_056',
            'n-026_Fe_058','n-028_Ni_058','n-028_Ni_060','n-029_Cu_063','n-029_Cu_065',
            'n-064_Gd_152','n-064_Gd_153','n-064_Gd_154','n-064_Gd_155','n-064_Gd_156',
            'n-064_Gd_157','n-064_Gd_158','n-064_Gd_160','n-082_Pb_206','n-082_Pb_207',
            'n-082_Pb_208','n-090_Th_232','n-091_Pa_231','n-091_Pa_233']

#关于裂变核素的处理，在HEATR部分有所不同，所以存储了31种裂变核素名单
fission=['n-090_Th_227','n-090_Th_229','n-090_Th_232','n-091_Pa_231','n-092_U_232',
         'n-092_U_233','n-092_U_234','n-092_U_235','n-092_U_236','n-092_U_237',
         'n-092_U_238','n-093_Np_237','n-093_Np_238','n-094_Pu_238','n-094_Pu_239',
         'n-094_Pu_240','n-094_Pu_241','n-094_Pu_242','n-095_Am_241','n-095_Am_242m1',
         'n-095_Am_243','n-096_Cm_242','n-096_Cm_243','n-096_Cm_244','n-096_Cm_245',
         'n-096_Cm_246','n-096_Cm_248','n-098_Cf_249','n-098_Cf_251','n-099_Es_254',
         'n-100_Fm_255']

fission_JEFF33=['90-Th-227g','90-Th-229g','90-Th-232g','91-Pa-231g','92-U-232g',
                '92-U-233g','92-U-234g','92-U-235g','92-U-236g','92-U-237g',
                '92-U-238g','93-Np-237g','93-Np-238g','94-Pu_238g','94-Pu-239g',
                '94-Pu-240g','94-Pu-241g','94-Pu-242g','95-Am-241g','95-Am-242m',
                '95-Am-243g','96-Cm-242g','96-Cm-243g','96-Cm-244g','96-Cm-245g',
                '96-Cm-246g','96-Cm-248g','98-Cf-249g','98-Cf-251g','99-Es-254g',
                '100-Fm-255g']

#封装一个函数，判断核素是否为true集合里面的核素，是就返回1，不是就返回0
def f_true(ENDFName,filename_i):
    if ENDFName=='ENDF7.0':
        length=len(true_ENDF7)
        for i in range(0,length):
            if filename_i==true_ENDF7[i]:
                return 1
        return 0
    elif ENDFName=='ENDF8.0':
        return 0
    elif ENDFName=='JEFF3,3':
        return 0

#封装一个函数，判断核素是否为裂变核素，是就返回1，不是就返回0
def f_fission(ENDFName, filename_i):
    length = len(fission)
    for i in range(0, length):
        if filename_i ==fission[i]:
            return 1
    return 0

#封装一个函数，功能是获取文件中的MAT编号
def getMAT(file,ENDFName):
    p=open(file)
    # 读取第10行
    i = 1
    while i <= 9:
        p.readline()
        i += 1
    line = p.readline()
    list = line.split(' ')
    #ENDF7.0的第10行的倒数第6个数字一般是MAT编号
    if ENDFName=='ENDF7.0':
        return str(list[-6])
    # ENDF8.0的第10行的倒数第2个数字一般是MAT编号
    elif ENDFName=='ENDF8.0':
        return str(list[-2])
    elif ENDFName=='JEFF3.3':
        return str(list[-6])
def Card_neutron(info,nuclide, acename, MAT, temp, p_fission):
    neutron=info.neutron
    ENDFname=info.ENDFname
    production_path=info.production_path

    Card=open(production_path+'Card.njoy','w')#覆盖原有内容

    #输入卡RECONR模块
    Card.write("reconr\n")
    Card.write("21 22/\n")
    Card.write("'pendf tape for " + nuclide + " from "+ENDFname+"'/\n")
    Card.write(MAT+" 2 0/\n")
    Card.write("0.001 0. 0.005/\n")
    Card.write("'"+nuclide+" from "+ENDFname+"'/\n")
    Card.write("'Processed with NJOY2016'/\n")
    Card.write("0/\n")

    #输入卡BROADR模块
    Card.write("broadr\n")
    Card.write("21 22 23/\n")
    Card.write(MAT+" 1 0 0 0/\n")
    Card.write("0.001/\n")
    Card.write(temp+"/\n")
    Card.write("0/\n")

    #输入卡HEATR模块
    Card.write("heatr\n")
    Card.write("21 23 24/\n")
    if p_fission==1:
        Card.write(MAT+" 11/\n")
        Card.write("302 303 304 318 401 442 443 444 445 446 447/\n")
    elif p_fission==0:
        Card.write(MAT + " 10/\n")
        Card.write("302 303 304 401 442 443 444 445 446 447/\n")

    #输入卡PURR模块
    Card.write("purr\n")
    Card.write("21 24 25/\n")
    Card.write(MAT+" 1 7 20 32/\n")
    Card.write(temp+"/\n")
    Card.write("1e10 1e4 1e3 300 100 30 10/\n")
    Card.write("0/\n")

    #输入卡GASPR模块
    Card.write("gaspr\n")
    Card.write("21 25 26/\n")

    #输入卡ACER模块
    Card.write("acer\n")
    Card.write("21 26 0 27 28/\n")
    acename='.'+acename
    Card.write("1 1 1 "+acename+" 0/\n")
    Card.write("'"+ENDFname+" "+nuclide+" "+temp+"K'/\n")
    Card.write(MAT+" "+temp+"\n")
    Card.write("1 1/\n")
    Card.write("/\n")

    #结束
    Card.write("stop")
    Card.close()
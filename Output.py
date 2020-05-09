import function as f

#output()用于将NJOY程序加工好的数据拷贝出来，编写xsdir，存档信息等
def output(info,nuclide,temp,acename):
    ENDFname=info.ENDFname
    production_path=info.production_path
    output_path=info.output_path
    # 将tape27复制出来，这个是生成的ACE格式数据库
    tape27 = production_path + 'tape27'
    acefile_name = ENDFname + '_' + nuclide+ '_' + temp + 'K.' + acename + 'c'
    acefile = output_path + 'ACElibrary/' + acefile_name
    f.copyfile(tape27, acefile)
    # tape28为xsdir文件使用的信息
    tape28 = open(production_path + 'tape28')
    xsdir = open(output_path + 'xsdir_' + temp + 'K', 'a')
    line = tape28.readline()
    line = line.replace('filename', acefile_name)
    line = line.replace('route', '0')
    xsdir.write(line)
    tape28.close()
    xsdir.close()
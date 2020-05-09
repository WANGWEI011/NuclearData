# NuclearData
目前可支持用NJOY2016，默认加工中子数据（概率表、释热率、气体），可加工多个温度，单线程运行。加工前需要手动将ENDF数据文件拷贝至ACEProduce目录下的input
文件夹中，并且将NJOY2016.exe程序放在production文件夹中，然后即可运行脚本，按照提示输入参数，完成加工。

第一步是检查文件路径，评价数据库文件和NJOY2016程序，需要使用者自己复制到指定文件夹中。比如你只想加工U235和U238两种核素，则只需要复制这两种核素的对应的
endf格式的文件到input文件夹中；加工脚本默认的NJOY程序的名称为“NJOY2016.exe”.

![image](https://github.com/WANGWEI011/NuclearData/blob/master/image/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200509181635.png)

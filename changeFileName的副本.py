import sys, string, os, shutil

def RenameFiles(prefix,srcdir,postfix):
    # os.listdir(path)历遍所有文件路径,返回为列表
    srcfiles = os.listdir(srcdir)
    index = 1
    for srcfile in srcfiles:
        # os.path.splitext将文件名和后缀名字分开,返回元组
        # srcfilename表示只获取元组首个元素,即文件名
        srcfilename = os.path.splitext(srcfile)[0]

        # sufix表示获取元组第二个元素,即获取后缀名
        sufix = os.path.splitext(srcfile)[1]

        #根据目录下具体的文件数修改%号后的值，"%04d"最多支持9999
        targfile = srcdir + "//" + "%4d"%(index) + prefix+ postfix
        srcfile = os.path.join(srcdir, srcfile)

        # os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError
        os.rename(srcfile, targfile)
        index += 1
        print(targfile)


srcdir = "/Users/pengwanlong/Desktop/test文件夹/test1"
prefix = "_a"
postfix = ".jpg"
RenameFiles(prefix,srcdir,postfix)
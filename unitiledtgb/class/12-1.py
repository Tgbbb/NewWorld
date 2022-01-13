try:
    fh=open('testfile.txt','w')
    fh.write('123456')
except IOError:
    print('没有找到文件或写入文件失败')
else:
    print('文件写入成功')
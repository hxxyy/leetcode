import os
rootdir = 'Training data'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       if os.path.isfile(path):
           file = open(path)
           line = file.readline()
           a = file.read()
           b = a.split(' ')
           dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, ']': 0, '7': 0, '8': 0, '9': 0,'\n':0}
           for i in b:
               if i == '':
                   continue
               pos = i.find('.')
               if pos != -1:
                   if i[pos-1] == '0':#e-01 at least
                        if i[pos+1]=='0':#e-02 at least
                            if i[pos+2] == '0':#e-03 at least
                                if i[pos+3] == '0':#e-04 at least
                                    if i[pos+4] == '0':
                                        dict['5'] += 1
                                    else:
                                        dict['4'] += 1
                                else:
                                    dict['3'] += 1
                            else:
                                dict['2'] += 1
                        else:
                            dict['1'] += 1
                   else:
                       dict['0'] += 1

           print(path)
           print(dict)


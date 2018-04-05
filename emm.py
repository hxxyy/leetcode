import os
import re
rootdir = 'Training data'
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       if os.path.isfile(path):
           file = open(path)
           line = file.readline()
           a = file.read()
           b = a.split(' ')
           #re.sub('[\r\n\t]', '', b)
           #b.replace('[', '')
           #b.replace(']', '')
           dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, ']': 0, '7': 0, '8': 0, '9': 0,'\n':0}
           for i in b:
               if i == '':
                   continue
               pos = i.find('e')
               if pos != -1:
                   if i[-1] == '\n':
                       num = i[-2]
                   else:
                       num = i[-1]
                   dict[num] += 1
               else:
                   dict['0'] += 1

           print(path)
           print(dict)

'''
           try:
               while True:
                   b.remove('[')
                   b.remove(']')
           except:
           '''

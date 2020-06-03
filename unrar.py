from unrar import rarfile
import sys

rar = rarfile.RarFile('unrar.rar')
rar.namelist()
rar.printdir()
opened = False
with open('dictionary.txt') as my_file:
    lines = my_file.readlines()

for line in lines:
    pwd = str(line.strip('\n'))
    try:
        rar.extractall(pwd=pwd)
        print("real password is : %s" %(pwd))
        #add break if want to extract file
        opened = True
        break
    except:
        print("test password : %s, err:%s%s" % (pwd, sys.exc_info()[0], sys.exc_info()[1]))

if opened:
    print('Successfully extracted file!')
else:
    print('--Unccessful in extracting file--')

x = input('Press enter to exit...')
sys.exit()
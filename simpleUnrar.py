from unrar import rarfile
import sys

in_path = input('Enter the input file path:')
try:
	rar = rarfile.RarFile(in_path)
except:
	print('input file not found!', sys.exc_info()[0])
	sys.exit()
rar.namelist()
rar.printdir()

dic_path = input('Enter the dictionary file path:')
try:
	with open(dic_path) as my_file:
		lines = my_file.readlines()
except:
	print('dictionary file not found!', sys.exc_info()[0])
	sys.exit()

out_path = input('Enter the output file path (Current directory if none):')
opened = False
for line in lines:
    pwd = str(line.strip('\n'))
    try:
        rar.extractall(path=out_path, pwd=pwd)
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

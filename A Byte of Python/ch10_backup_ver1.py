# Filename: backup_ver1.py

import os
import time
import sys   
sys.path.append('C:\\Program Files\\WinRAR')

# 1. The files and directories to be backed up are specified in a list.
# If you are using Unix/Linux OS, use source = ['/home/swaroop/byte', '/home/swaroop/bin']
# If you are using Windows, use form lilke: source = [r'C:\Documents', r'D:\Work'] or source = ['C:\\Documents', 'D:\\Work']
source = 'E:\\Programspace\\Python\\backup_ver1.txt'

# 2. The backup must be stored in a main backup directory
# Remember to change this to what you will be using
# target_dir = '/mnt/e/backup/' 
target_dir = 'E:\\Programspace\\Python\\'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar' # .zip .rar

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
# zip_command = "zip -qr '%s' %s" % (target, ''.join(source))
zip_command = "winrar a %s %s %s" % (target, source, target_dir)

# Windows Winrar
print 'Zip_command is:', zip_command   
print os.system('dir echo. & pause')

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'

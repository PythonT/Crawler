#!/usr/bin/python
#coding:utf-8
# Filename: backup_ver2.py

import os

import time

# 1. 需要备份的文件和目录由一个列表指定

source = ['"C://My Documents"', 'C://Code']

# 注意我们必须在字符串内部使用双引号将带有空格的名字括起来。

# 2. 备份必须存在一个主备份目录中

target_dir = 'E://' # 记住改变这里即可改变你想要使用的主目录

# 3. 文件会被备份为一个zip文件。

# 4. 主目录中的子目录将以当前日期命名

today = target_dir + os.sep + time.strftime('%Y%m%d')

# zip归档文件将以当前时间命名

now = time.strftime('%H%M%S')

# 如果子目录不存在则创建之

if not os.path.exists(today):

    os.mkdir(today) # make directory

    print('Successfully created directory', today)

# 组成zip文件名

target = today + os.sep + now + '.zip'

print(target)

# 5. 我们使用zip命令将文件归档成一个zip

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print(zip_command)

# 执行备份

if os.system(zip_command) == 0:

    print('Successful backup to', target)
    print('sss')

else:

    print('Backup FAILED')
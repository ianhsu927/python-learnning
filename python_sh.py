# 使用 Python 运行 shell 命令

# python 运行 shell 命令获得命令的结果
import subprocess

ret = subprocess.check_output('ls -l', shell=True)
print(str(ret, encoding='utf-8').split('\n'))
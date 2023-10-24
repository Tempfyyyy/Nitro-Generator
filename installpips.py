import subprocess

modules_to_install = ['requests', 'random', 'string', 'time', 'sys', "colorama"]

for module in modules_to_install:
    subprocess.check_call(['pip', 'install', module])

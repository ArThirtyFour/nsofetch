import platform
import subprocess

import cpuinfo
import psutil
import distro

def get_distro():
    return distro.name()

def get_kernel():
    return platform.platform()

def get_cpu():
    return cpuinfo.get_cpu_info()['brand_raw']

def get_shell():
    return subprocess.check_output("echo $SHELL", shell=True).decode().strip().split('/')[-1]

def get_resolution():
    return subprocess.check_output("xrandr | grep '*' ", shell=True).decode().strip()[:10]

def get_memory():
    memory = psutil.virtual_memory()
    return f'{round(memory.used/(1024**2),0)}MB/{round(memory.total/(1024 ** 2),0)}MB'

def get_de():
   return subprocess.check_output("echo $XDG_CURRENT_DESKTOP", shell=True).decode().strip()

def get_gtk_theme():
    return subprocess.check_output('gsettings get org.gnome.desktop.interface gtk-theme' , shell=True).decode().strip()

def get_info_name_pc():
    name_user = subprocess.check_output('whoami' , shell=True).decode().strip()
    name_pc = platform.node()
    return f'Пользователь : {name_user} | Имя ПК : {name_pc}'
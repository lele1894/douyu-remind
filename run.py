import os
import subprocess

CRD_SSH_Code = input("Google CRD SSH Code :")
username = "user"  # @param {type:"string"}
password = "root"  # @param {type:"string"}
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 123456  # @param {type: "integer"}

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChrome()
        self.finish(user)

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Chrome Remote Desktop 已安装 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")
        print("已安装 XFCE4 桌面环境 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome 已安装 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def finish(user):
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        
        print("..........................................................") 
        print(".....由 The Disala 提供................................") 
        print("..........................................................") 
        print("......#####...######...####....####...##.......####.......") 
        print("......##..##....##....##......##..##..##......##..##......")  
        print("......##..##....##.....####...######..##......######......") 
        print("......##..##....##........##..##..##..##......##..##......") 
        print("......#####...######...####...##..##..######..##..##......") 
        print("..........................................................") 
        print("登录 PIN : 123456") 
        print("用户名 : user") 
        print("用户密码 : root") 
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("请输入从链接获取的授权码")
    elif len(str(Pin)) < 6:
        print("请输入6位或以上的PIN码")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' 变量未找到，请先创建用户")

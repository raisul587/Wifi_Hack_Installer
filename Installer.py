import os
print('''\033[1;36;40mWifi_Hack Installer Raisul
Your Device Must Be Rooted
If Any Question,
Contact Me Facebook
FB:@https://www.facebook.com/Raisul.Anonymous \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/raisul587/Wifi_Hack")

os.system("cd ..;chmod +x Wifi_Hack/birihack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Wifi_Hack/birihack.py -i wlan0 -K")

import time
import sys

def print_like_typing(text):
    for char in text:
        sys.stdout.write("\033[91m" + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)  # يمكنك تغيير هذا الرقم لتعديل سرعة الكتابة


a32 = '\x1b[38;5;180m' ; a14 = '\x1b[38;5;153m'
V1 = '\033[2;32m' ; V2 = '\033[1;33m' ; V3='\x1b[38;5;209m' ; V4= '\x1b[1;97m' ; V5 = '\x1b[38;5;8m' ; X= '\033[1;33m' ; F = '\033[2;32m'
a32 = '\x1b[38;5;180m'  # بني فاتح
a14 = '\x1b[38;5;153m'  # أزرق فاتح
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
R1 = '\033[1;31;40m'
X1 = '\033[1;33;40m' 
F1= '\033[1;32;40m' 
C1 = "\033[1;97;40m" 
B1 = '\033[1;36;40m'
K1 = '\033[1;35;40m'
V1 = '\033[1;36;40m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m'
G = '\033[1;34m' 
HH='\033[1;34m' 
M = '\x1b[1;37m'
ge,be,gi,bi,hit=0,0,0,0,0
G = '\033[1;32m'  
Y = '\033[1;33m'  
C = '\033[1;36m' 
E = '\033[0m'    
E = '\033[1;31m' #احمر
X= '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
Ca = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
Ca = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
uk= [X,F,f,Y,B,Ca,y]

def clear():
 print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

''') 
hits=0
bad=0
clear()
print(f""" 
----------------------
 CH : @Y_1_I_1
----------------------
""")
import requests
import random
import threading
import time
import webbrowser
webbrowser.open("https://t.me/Y_1_I_1")
from uuid import uuid4
from colorama import Fore, init

init(autoreset=True)

############################
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
C = '\033[2;35m' 
S = '\033[2;36m'
G = '\033[1;34m' 
HH='\033[1;34m' 
M = '\x1b[1;37m'
ge,be,gi,bi,hit=0,0,0,0,0
G = '\033[1;32m'  
Y = '\033[1;33m'  
C = '\033[1;36m' 
E = '\033[0m'    
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
############################
token = input(Z+'Tokn  :  '+F)
ID = input(Z+'ID  :  '+F)


print("""
اختار نوع الصيد ♡
1 - HH_HH
2 - _g_jak
3 - hskg_

""")
pattern_choice = int(input(" 🦅اختار: "))


a = 0
s = 0
om = 'qwertyuioplkjhgfdsazxcvbnm'
ooo = 'qwertyuiopalkjhgfdsazxcvbnm0987654321'

url = 'https://i.instagram.com/api/v1/accounts/create/'
headers = {
    'Content-Length': '437',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
    'Accept-Language': 'en-IQ, en-US',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': 'AQ==',
    'Accept-Encoding': 'gzip',
}

def af():
    if pattern_choice == 1:
        return random.choice(om) + random.choice(ooo) + "_" + random.choice(ooo) + random.choice(om)
    elif pattern_choice == 2:
        first_char = "_"
        second_char = random.choice(om)
        return first_char + second_char + "_" + random.choice(ooo) + random.choice(om)

    elif pattern_choice == 3:
        return "_" + random.choice(om) + random.choice(ooo) + random.choice(ooo) + random.choice(om)
    elif pattern_choice == 4:
        return "#" + random.choice(om) + "_" + random.choice(ooo) + "#"

    elif pattern_choice == 5:
        return "_#" + random.choice(ooo) + "_" + random.choice(ooo) + "#"

    else:
        print(Fore.RED + " اختيار غير صحيح! يرجى تشغيل البرنامج مرة أخرى واختيار رقم بين 1-3.")
        exit()


def a1():
    global a, s
    while True:
        user = af()
        data = {
            "email": "abdo1@gmail.com",
            "username": user,
            "password": "Aa123456" + user,
            "device_id": "android-" + str(uuid4()),
            "guid": str(uuid4()),
        }

        try:
            response = requests.post(url, headers=headers, data=data).text

            if '"email_is_taken"' in response:
                print(Fore.GREEN + f'Good User: {user}')
                a += 1

                message = f'''

------------------------------------------
-> User :🔥 {user}
------------------------------------------
-> by 🥷: Y_1_I_1
------------------------------------------
هاك
https://t.me/@Y_1_I_1
'''
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': ID, 'text': message})
            else:
                s += 1

            print(f"\r{Fore.GREEN}Good صح {F} | {Fore.RED}Ban خط {C}", end='', flush=True)

        except requests.exceptions.RequestException:
            time.sleep(0.5)

print(f"{Fore.GREEN}Good ✅ 0 | {Fore.RED}Ban ❌ 0\n")
threads = []
for _ in range(20):
    t = threading.Thread(target=a1)
    threads.append(t)
    t.start()

for t in threads:
    t.join() ('__name__'
    	 '__main__')
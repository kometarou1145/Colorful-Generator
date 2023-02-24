import string
import random
import time

Color = '\033[36m','\033[35m','\033[34m','\033[33m','\033[32m','\033[31m'
Bold = '\033[1m'
Underline = '\033[4m'
Reset = '\033[0m'

email2 = [
'@yahoo.co.jp',
'@gmail.com',
'@ezweb.ne.jp',
'@au.com',
'@docomo.ne.jp',
'@i.softbank.jp',
'@softbank.ne.jp',
'@excite.co.jp',
'@googlemail.com',
'@hotmail.co.jp',
'@hotmail.com',
'@icloud.com',
'@live.jp',
'@me.com',
'@mineo.jp',
'@nifty.com',
'@outlook.com',
'@outlook.jp',
'@yahoo.ne.jp',
'@ybb.ne.jp',
'@ymobile.ne.jp',
]

index1 = random.randint(0, len(Color) - 1)
ColorRandom1 = Color[index1]
print(ColorRandom1 + "███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗ ███████╗███╗   ██╗")
time.sleep(0.3)
index2 = random.randint(0, len(Color) - 1)
ColorRandom2 = Color[index2]
print(ColorRandom2 + "██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝ ██╔════╝████╗  ██║")
time.sleep(0.3)
index3 = random.randint(0, len(Color) - 1)
ColorRandom3 = Color[index3]
print(ColorRandom3 + "█████╗  ██╔████╔██║███████║██║██║     ██║  ███╗█████╗  ██╔██╗ ██║")
time.sleep(0.3)
index4 = random.randint(0, len(Color) - 1)
ColorRandom4 = Color[index4]
print(ColorRandom4 + "██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║   ██║██╔══╝  ██║╚██╗██║")
time.sleep(0.3)
index5 = random.randint(0, len(Color) - 1)
ColorRandom5 = Color[index5]
print(ColorRandom5 + "███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╔╝███████╗██║ ╚████║")
time.sleep(0.3)
index6 = random.randint(0, len(Color) - 1)
ColorRandom6 = Color[index6]
print(ColorRandom6 + "╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
time.sleep(0.3)
index7 = random.randint(0, len(Color) - 1)
ColorRandom7 = Color[index7]
print(ColorRandom7 + Bold + Underline + "Developer : こめたろう#0681")
time.sleep(2)

cnt = 0
while cnt < 100:
 code1 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
 index8 = random.randint(0, len(email2) - 1)
 code2 = email2[index8]
 index9 = random.randint(0, len(Color) - 1)
 ColorRandom8 = Color[index9]
 emailpass = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
 with open('emails.txt', 'a') as emails:
  print(f"{code1}{code2}:{emailpass}", file=emails)
  print(Underline + Bold + ColorRandom8 + f"Generated : {code1}{code2}:{emailpass}" + Reset)
cnt += 1
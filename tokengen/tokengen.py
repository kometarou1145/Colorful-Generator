import random
import string
import time
from playsound import playsound

tokenhead = ['MTA3','ODK','OTE']
Color = '\033[36m','\033[35m','\033[34m','\033[33m','\033[32m','\033[31m'
Bold = '\033[1m'
Underline = '\033[4m'
Reset = '\033[0m'

index1 = random.randint(0, len(Color) - 1)
ColorRandom1 = Color[index1]
print(ColorRandom1 + "████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗███╗   ██╗")
time.sleep(0.3)
index2 = random.randint(0, len(Color) - 1)
ColorRandom2 = Color[index2]
print(ColorRandom2 + "╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝ ██╔════╝████╗  ██║")
time.sleep(0.3)
index3 = random.randint(0, len(Color) - 1)
ColorRandom3 = Color[index3]
print(ColorRandom3 + "   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██║  ███╗█████╗  ██╔██╗ ██║")
time.sleep(0.3)
index4 = random.randint(0, len(Color) - 1)
ColorRandom4 = Color[index4]
print(ColorRandom4 + "   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ██║╚██╗██║")
time.sleep(0.3)
index5 = random.randint(0, len(Color) - 1)
ColorRandom5 = Color[index5]
print(ColorRandom5 + "   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║╚██████╔╝███████╗██║ ╚████║")
time.sleep(0.3)
index6 = random.randint(0, len(Color) - 1)
ColorRandom6 = Color[index6]
print(ColorRandom6 + "   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
time.sleep(0.3)
index7 = random.randint(0, len(Color) - 1)
ColorRandom7 = Color[index7]
print(ColorRandom7 + Bold + Underline + "Developer : こめたろう#0681")
time.sleep(2)

cnt = 0
while cnt < 100:
 index8 = random.randint(0, len(tokenhead) - 1)
 code1 = tokenhead[index8]
 code2 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(2)])
 code3 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(20)])
 code4 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
 code5 = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(38)])
 index9 = random.randint(0, len(Color) - 1)
 ColorRandom8 = Color[index9]
 with open('tokens.txt', 'a') as tokens:
  print(f"{code1}{code2}{code3}.{code4}.{code5}", file=tokens)
  print(Underline + Bold + ColorRandom8 + f"Generated : {code1}{code2}{code3}.{code4}.{code5}" + Reset)
cnt += 1
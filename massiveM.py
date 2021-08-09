#massiveM.py Bitcoin Legacy compressed/uncompresses address. 04/07/2021
# Search for mnemonics 128 addresses from one 12 word mnemonics and balance checked
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from time import sleep
import itertools
import requests
import bitcoinlib
import random,os,hashlib
import atexit
from time import time
from datetime import timedelta, datetime
import csv
from itertools import zip_longest

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

const = "m/44'/00'/0'/0/"



def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("Start Program")

print("massiveM.py. List loading Good Luck...")

filename ='wordlist.txt'
with open(filename) as file:
    wordlist = file.read().split()


def create_valid_mnemonics(strength=128):
    rbytes = os.urandom(strength // 8)
    h = hashlib.sha256(rbytes).hexdigest()
    b = ( bin(int.from_bytes(rbytes, byteorder="big"))[2:].zfill(len(rbytes) * 8) \
         + bin(int(h, 16))[2:].zfill(256)[: len(rbytes) * 8 // 32] )
    result = []
    for i in range(len(b) // 11):
        idx = int(b[i * 11 : (i + 1) * 11], 2)
        result.append(wordlist[idx])
    return " ".join(result)

def mnem_to_seed(words):
 salt = 'mnemonic'
 seed = hashlib.pbkdf2_hmac("sha512",words.encode("utf-8"), salt.encode("utf-8"), 2048)
 return seed
 
def seed_to_privatekey(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b0=b.subkey_for_path(const + "0")
    return b0.address()
def seed_to_privatekey1(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b1=b.subkey_for_path(const + "1")
    return b1.address()
def seed_to_privatekey2(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b2=b.subkey_for_path(const + "2")
    return b2.address()
def seed_to_privatekey3(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b3=b.subkey_for_path(const + "3")
    return b3.address()
def seed_to_privatekey4(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b4=b.subkey_for_path(const + "4")
    return b4.address()
def seed_to_privatekey5(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b5=b.subkey_for_path(const + "5")
    return b5.address()
def seed_to_privatekey6(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b6=b.subkey_for_path(const + "6")
    return b6.address()
def seed_to_privatekey7(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b7=b.subkey_for_path(const + "7")
    return b7.address()
def seed_to_privatekey8(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b8=b.subkey_for_path(const + "8")
    return b8.address()
def seed_to_privatekey9(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b9=b.subkey_for_path(const + "9")
    return b9.address()
def seed_to_privatekey10(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b10=b.subkey_for_path(const + "10")
    return b10.address()
def seed_to_privatekey11(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b11=b.subkey_for_path(const + "11")
    return b11.address()
def seed_to_privatekey12(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b12=b.subkey_for_path(const + "12")
    return b12.address()
def seed_to_privatekey13(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b13=b.subkey_for_path(const + "13")
    return b13.address()
def seed_to_privatekey14(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b14=b.subkey_for_path(const + "14")
    return b14.address()
def seed_to_privatekey15(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b15=b.subkey_for_path(const + "15")
    return b15.address()
def seed_to_privatekey16(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b16=b.subkey_for_path(const + "16")
    return b16.address()
def seed_to_privatekey17(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b17=b.subkey_for_path(const + "17")
    return b17.address()
def seed_to_privatekey18(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b18=b.subkey_for_path(const + "18")
    return b18.address()
def seed_to_privatekey19(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b19=b.subkey_for_path(const + "19")
    return b19.address()
def seed_to_privatekey20(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b20=b.subkey_for_path(const + "20")
    return b20.address()
def seed_to_privatekey21(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b21=b.subkey_for_path(const + "21")
    return b21.address()
def seed_to_privatekey22(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b22=b.subkey_for_path(const + "22")
    return b22.address()
def seed_to_privatekey23(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b23=b.subkey_for_path(const + "23")
    return b23.address()
def seed_to_privatekey24(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b24=b.subkey_for_path(const + "24")
    return b24.address()
def seed_to_privatekey25(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b25=b.subkey_for_path(const + "25")
    return b25.address()
def seed_to_privatekey26(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b26=b.subkey_for_path(const + "26")
    return b26.address()
def seed_to_privatekey27(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b27=b.subkey_for_path(const + "27")
    return b27.address()
def seed_to_privatekey28(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b28=b.subkey_for_path(const + "28")
    return b28.address()
def seed_to_privatekey29(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b29=b.subkey_for_path(const + "29")
    return b29.address()
def seed_to_privatekey30(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b30=b.subkey_for_path(const + "30")
    return b30.address()
def seed_to_privatekey31(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b31=b.subkey_for_path(const + "31")
    return b31.address()
def seed_to_privatekey32(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b32=b.subkey_for_path(const + "32")
    return b32.address()
def seed_to_privatekey33(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b33=b.subkey_for_path(const + "33")
    return b33.address()
def seed_to_privatekey34(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b34=b.subkey_for_path(const + "34")
    return b34.address()
def seed_to_privatekey35(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b35=b.subkey_for_path(const + "35")
    return b35.address()
def seed_to_privatekey36(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b36=b.subkey_for_path(const + "36")
    return b36.address()
def seed_to_privatekey37(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b37=b.subkey_for_path(const + "37")
    return b37.address()
def seed_to_privatekey38(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b38=b.subkey_for_path(const + "38")
    return b38.address()
def seed_to_privatekey39(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b39=b.subkey_for_path(const + "39")
    return b39.address()
def seed_to_privatekey40(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b40=b.subkey_for_path(const + "40")
    return b40.address()
def seed_to_privatekey41(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b41=b.subkey_for_path(const + "41")
    return b41.address()
def seed_to_privatekey42(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b42=b.subkey_for_path(const + "42")
    return b42.address()
def seed_to_privatekey43(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b43=b.subkey_for_path(const + "43")
    return b43.address()
def seed_to_privatekey44(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b44=b.subkey_for_path(const + "44")
    return b44.address()
def seed_to_privatekey45(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b45=b.subkey_for_path(const + "45")
    return b45.address()
def seed_to_privatekey46(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b46=b.subkey_for_path(const + "46")
    return b46.address()
def seed_to_privatekey47(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b47=b.subkey_for_path(const + "47")
    return b47.address()
def seed_to_privatekey48(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b48=b.subkey_for_path(const + "48")
    return b48.address()
def seed_to_privatekey49(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b49=b.subkey_for_path(const + "49")
    return b49.address()
def seed_to_privatekey50(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b50=b.subkey_for_path(const + "50")
    return b50.address()
def seed_to_privatekey51(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b51=b.subkey_for_path(const + "51")
    return b51.address()
def seed_to_privatekey52(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b52=b.subkey_for_path(const + "52")
    return b52.address()
def seed_to_privatekey53(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b53=b.subkey_for_path(const + "53")
    return b53.address()
def seed_to_privatekey54(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b54=b.subkey_for_path(const + "54")
    return b54.address()
def seed_to_privatekey55(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b55=b.subkey_for_path(const + "55")
    return b55.address()
def seed_to_privatekey56(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b56=b.subkey_for_path(const + "56")
    return b56.address()
def seed_to_privatekey57(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b57=b.subkey_for_path(const + "57")
    return b57.address()
def seed_to_privatekey58(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b58=b.subkey_for_path(const + "58")
    return b58.address()
def seed_to_privatekey59(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b59=b.subkey_for_path(const + "59")
    return b59.address()
def seed_to_privatekey60(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b60=b.subkey_for_path(const + "60")
    return b60.address()
def seed_to_privatekey61(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b61=b.subkey_for_path(const + "61")
    return b61.address()
def seed_to_privatekey62(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b62=b.subkey_for_path(const + "62")
    return b62.address()
def seed_to_privatekey63(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b63=b.subkey_for_path(const + "63")
    return b63.address()
def seed_to_privatekey64(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b64=b.subkey_for_path(const + "64")
    return b64.address()
def seed_to_privatekey65(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b65=b.subkey_for_path(const + "65")
    return b65.address()
def seed_to_privatekey66(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b66=b.subkey_for_path(const + "66")
    return b66.address()
def seed_to_privatekey67(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b67=b.subkey_for_path(const + "67")
    return b67.address()
def seed_to_privatekey68(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b68=b.subkey_for_path(const + "68")
    return b68.address()
def seed_to_privatekey69(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b69=b.subkey_for_path(const + "69")
    return b69.address()
def seed_to_privatekey70(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b70=b.subkey_for_path(const + "70")
    return b70.address()
def seed_to_privatekey71(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b71=b.subkey_for_path(const + "71")
    return b71.address()
def seed_to_privatekey72(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b72=b.subkey_for_path(const + "72")
    return b72.address()
def seed_to_privatekey73(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b73=b.subkey_for_path(const + "73")
    return b73.address()
def seed_to_privatekey74(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b74=b.subkey_for_path(const + "74")
    return b74.address()
def seed_to_privatekey75(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b75=b.subkey_for_path(const + "75")
    return b75.address()
def seed_to_privatekey76(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b76=b.subkey_for_path(const + "76")
    return b76.address()
def seed_to_privatekey77(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b77=b.subkey_for_path(const + "77")
    return b77.address()
def seed_to_privatekey78(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b78=b.subkey_for_path(const + "78")
    return b78.address()
def seed_to_privatekey79(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b79=b.subkey_for_path(const + "79")
    return b79.address()
def seed_to_privatekey80(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b80=b.subkey_for_path(const + "80")
    return b80.address()
def seed_to_privatekey81(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b81=b.subkey_for_path(const + "81")
    return b81.address()
def seed_to_privatekey82(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b82=b.subkey_for_path(const + "82")
    return b82.address()
def seed_to_privatekey83(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b83=b.subkey_for_path(const + "83")
    return b83.address()
def seed_to_privatekey84(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b84=b.subkey_for_path(const + "84")
    return b84.address()
def seed_to_privatekey85(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b85=b.subkey_for_path(const + "85")
    return b85.address()
def seed_to_privatekey86(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b86=b.subkey_for_path(const + "86")
    return b86.address()
def seed_to_privatekey87(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b87=b.subkey_for_path(const + "87")
    return b87.address()
def seed_to_privatekey88(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b88=b.subkey_for_path(const + "88")
    return b88.address()
def seed_to_privatekey89(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b89=b.subkey_for_path(const + "89")
    return b89.address()
def seed_to_privatekey90(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b90=b.subkey_for_path(const + "90")
    return b90.address()
def seed_to_privatekey91(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b91=b.subkey_for_path(const + "91")
    return b91.address()
def seed_to_privatekey92(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b92=b.subkey_for_path(const + "92")
    return b92.address()
def seed_to_privatekey93(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b93=b.subkey_for_path(const + "93")
    return b93.address()
def seed_to_privatekey94(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b94=b.subkey_for_path(const + "94")
    return b94.address()
def seed_to_privatekey95(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b95=b.subkey_for_path(const + "95")
    return b95.address()
def seed_to_privatekey96(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b96=b.subkey_for_path(const + "96")
    return b96.address()
def seed_to_privatekey97(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b97=b.subkey_for_path(const + "97")
    return b97.address()
def seed_to_privatekey98(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b98=b.subkey_for_path(const + "98")
    return b98.address()
def seed_to_privatekey99(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b99=b.subkey_for_path(const + "99")
    return b99.address()
def seed_to_privatekey100(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b100=b.subkey_for_path(const + "100")
    return b100.address()
def seed_to_privatekey101(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b101=b.subkey_for_path(const + "101")
    return b101.address()
def seed_to_privatekey102(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b102=b.subkey_for_path(const + "102")
    return b102.address()
def seed_to_privatekey103(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b103=b.subkey_for_path(const + "103")
    return b103.address()
def seed_to_privatekey104(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b104=b.subkey_for_path(const + "104")
    return b104.address()
def seed_to_privatekey105(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b105=b.subkey_for_path(const + "105")
    return b105.address()
def seed_to_privatekey106(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b106=b.subkey_for_path(const + "106")
    return b106.address()
def seed_to_privatekey107(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b107=b.subkey_for_path(const + "107")
    return b107.address()
def seed_to_privatekey108(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b108=b.subkey_for_path(const + "108")
    return b108.address()
def seed_to_privatekey109(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b109=b.subkey_for_path(const + "109")
    return b109.address()
def seed_to_privatekey110(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b110=b.subkey_for_path(const + "110")
    return b110.address()
def seed_to_privatekey111(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b111=b.subkey_for_path(const + "111")
    return b111.address()
def seed_to_privatekey112(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b112=b.subkey_for_path(const + "112")
    return b112.address()
def seed_to_privatekey113(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b113=b.subkey_for_path(const + "113")
    return b113.address()
def seed_to_privatekey114(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b114=b.subkey_for_path(const + "114")
    return b114.address()
def seed_to_privatekey115(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b115=b.subkey_for_path(const + "115")
    return b115.address()
def seed_to_privatekey116(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b116=b.subkey_for_path(const + "116")
    return b116.address()
def seed_to_privatekey117(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b117=b.subkey_for_path(const + "117")
    return b117.address()
def seed_to_privatekey118(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b118=b.subkey_for_path(const + "118")
    return b118.address()
def seed_to_privatekey119(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b119=b.subkey_for_path(const + "119")
    return b119.address()
def seed_to_privatekey120(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b120=b.subkey_for_path(const + "120")
    return b120.address()
def seed_to_privatekey121(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b121=b.subkey_for_path(const + "121")
    return b121.address()
def seed_to_privatekey122(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b122=b.subkey_for_path(const + "122")
    return b122.address()
def seed_to_privatekey123(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b123=b.subkey_for_path(const + "123")
    return b123.address()
def seed_to_privatekey124(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b124=b.subkey_for_path(const + "124")
    return b124.address()
def seed_to_privatekey125(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b125=b.subkey_for_path(const + "125")
    return b125.address()
def seed_to_privatekey126(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b126=b.subkey_for_path(const + "126")
    return b126.address()
def seed_to_privatekey127(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b127=b.subkey_for_path(const + "127")
    return b127.address()


query = []
count=0
total=0
while True:
    line = create_valid_mnemonics()
    seed = mnem_to_seed(line)
    addr = seed_to_privatekey(seed)
    addr1 = seed_to_privatekey1(seed)
    addr2 = seed_to_privatekey2(seed)
    addr3 = seed_to_privatekey3(seed)
    addr4 = seed_to_privatekey4(seed)
    addr5 = seed_to_privatekey5(seed)
    addr6 = seed_to_privatekey6(seed)
    addr7 = seed_to_privatekey7(seed)
    addr8 = seed_to_privatekey8(seed)
    addr9 = seed_to_privatekey9(seed)
    addr10 = seed_to_privatekey10(seed)
    addr11 = seed_to_privatekey11(seed)
    addr12 = seed_to_privatekey12(seed)
    addr13 = seed_to_privatekey13(seed)
    addr14 = seed_to_privatekey14(seed)
    addr15 = seed_to_privatekey15(seed)
    addr16 = seed_to_privatekey16(seed)
    addr17 = seed_to_privatekey17(seed)
    addr18 = seed_to_privatekey18(seed)
    addr19 = seed_to_privatekey19(seed)
    addr20 = seed_to_privatekey20(seed)
    addr21 = seed_to_privatekey21(seed)
    addr22 = seed_to_privatekey22(seed)
    addr23 = seed_to_privatekey23(seed)
    addr24 = seed_to_privatekey24(seed)
    addr25 = seed_to_privatekey25(seed)
    addr26 = seed_to_privatekey26(seed)
    addr27 = seed_to_privatekey27(seed)
    addr28 = seed_to_privatekey28(seed)
    addr29 = seed_to_privatekey29(seed)
    addr30 = seed_to_privatekey30(seed)
    addr31 = seed_to_privatekey31(seed)
    addr32 = seed_to_privatekey32(seed)
    addr33 = seed_to_privatekey33(seed)
    addr34 = seed_to_privatekey34(seed)
    addr35 = seed_to_privatekey35(seed)
    addr36 = seed_to_privatekey36(seed)
    addr37 = seed_to_privatekey37(seed)
    addr38 = seed_to_privatekey38(seed)
    addr39 = seed_to_privatekey39(seed)
    addr40 = seed_to_privatekey40(seed)
    addr41 = seed_to_privatekey41(seed)
    addr42 = seed_to_privatekey42(seed)
    addr43 = seed_to_privatekey43(seed)
    addr44 = seed_to_privatekey44(seed)
    addr45 = seed_to_privatekey45(seed)
    addr46 = seed_to_privatekey46(seed)
    addr47 = seed_to_privatekey47(seed)
    addr48 = seed_to_privatekey48(seed)
    addr49 = seed_to_privatekey49(seed)
    addr50 = seed_to_privatekey50(seed)
    addr51 = seed_to_privatekey51(seed)
    addr52 = seed_to_privatekey52(seed)
    addr53 = seed_to_privatekey53(seed)
    addr54 = seed_to_privatekey54(seed)
    addr55 = seed_to_privatekey55(seed)
    addr56 = seed_to_privatekey56(seed)
    addr57 = seed_to_privatekey57(seed)
    addr58 = seed_to_privatekey58(seed)
    addr59 = seed_to_privatekey59(seed)
    addr60 = seed_to_privatekey60(seed)
    addr61 = seed_to_privatekey61(seed)
    addr62 = seed_to_privatekey62(seed)
    addr63 = seed_to_privatekey63(seed)
    addr64 = seed_to_privatekey64(seed)
    addr65 = seed_to_privatekey65(seed)
    addr66 = seed_to_privatekey66(seed)
    addr67 = seed_to_privatekey67(seed)
    addr68 = seed_to_privatekey68(seed)
    addr69 = seed_to_privatekey69(seed)
    addr70 = seed_to_privatekey70(seed)
    addr71 = seed_to_privatekey71(seed)
    addr72 = seed_to_privatekey72(seed)
    addr73 = seed_to_privatekey73(seed)
    addr74 = seed_to_privatekey74(seed)
    addr75 = seed_to_privatekey75(seed)
    addr76 = seed_to_privatekey76(seed)
    addr77 = seed_to_privatekey77(seed)
    addr78 = seed_to_privatekey78(seed)
    addr79 = seed_to_privatekey79(seed)
    addr80 = seed_to_privatekey80(seed)
    addr81 = seed_to_privatekey81(seed)
    addr82 = seed_to_privatekey82(seed)
    addr83 = seed_to_privatekey83(seed)
    addr84 = seed_to_privatekey84(seed)
    addr85 = seed_to_privatekey85(seed)
    addr86 = seed_to_privatekey86(seed)
    addr87 = seed_to_privatekey87(seed)
    addr88 = seed_to_privatekey88(seed)
    addr89 = seed_to_privatekey89(seed)
    addr90 = seed_to_privatekey90(seed)
    addr91 = seed_to_privatekey91(seed)
    addr92 = seed_to_privatekey92(seed)
    addr93 = seed_to_privatekey93(seed)
    addr94 = seed_to_privatekey94(seed)
    addr95 = seed_to_privatekey95(seed)
    addr96 = seed_to_privatekey96(seed)
    addr97 = seed_to_privatekey97(seed)
    addr98 = seed_to_privatekey98(seed)
    addr99 = seed_to_privatekey99(seed)
    addr100 = seed_to_privatekey100(seed)
    addr101 = seed_to_privatekey101(seed)
    addr102 = seed_to_privatekey102(seed)
    addr103 = seed_to_privatekey103(seed)
    addr104 = seed_to_privatekey104(seed)
    addr105 = seed_to_privatekey105(seed)
    addr106 = seed_to_privatekey106(seed)
    addr107 = seed_to_privatekey107(seed)
    addr108 = seed_to_privatekey108(seed)
    addr109 = seed_to_privatekey109(seed)
    addr110 = seed_to_privatekey110(seed)
    addr111 = seed_to_privatekey111(seed)
    addr112 = seed_to_privatekey112(seed)
    addr113 = seed_to_privatekey113(seed)
    addr114 = seed_to_privatekey114(seed)
    addr115 = seed_to_privatekey115(seed)
    addr116 = seed_to_privatekey116(seed)
    addr117 = seed_to_privatekey117(seed)
    addr118 = seed_to_privatekey118(seed)
    addr119 = seed_to_privatekey119(seed)
    addr120 = seed_to_privatekey120(seed)
    addr121 = seed_to_privatekey121(seed)
    addr122 = seed_to_privatekey122(seed)
    addr123 = seed_to_privatekey123(seed)
    addr124 = seed_to_privatekey124(seed)
    addr125 = seed_to_privatekey125(seed)
    addr126 = seed_to_privatekey126(seed)
    addr127 = seed_to_privatekey127(seed)

    query=(addr,addr1,addr2,addr3,addr4,addr5,addr6,addr7,addr8,addr9,addr10,addr11,addr12,addr13,addr14,addr15,addr16,addr17,addr18,addr19,addr20,addr21,addr22,addr23,addr24,addr25,addr26,addr27,addr28,addr29,addr30,addr31,addr32,addr33,addr34,addr35,addr36,addr37,addr38,addr39,addr40,addr41,addr42,addr43,addr44,addr45,addr46,addr47,addr48,addr49,addr50,addr51,addr52,addr53,addr54,addr55,addr56,addr57,addr58,addr59,addr60,addr61,addr62,addr63,addr64,addr65,addr66,addr67,addr68,addr69,addr70,addr71,addr72,addr73,addr74,addr75,addr76,addr77,addr78,addr79,addr80,addr81,addr82,addr83,addr84,addr85,addr86,addr87,addr88,addr89,addr90,addr91,addr92,addr93,addr94,addr95,addr96,addr97,addr98,addr99,addr100,addr101,addr102,addr103,addr104,addr105,addr106,addr107,addr108,addr109,addr110,addr11,addr112,addr113,addr114,addr115,addr116,addr117,addr118,addr119,addr120,addr121,addr122,addr123,addr124,addr125,addr126,addr127)
    count+=1
    total+=128
    if len(query) == 128:
        try:
            request = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query),timeout=10)
            request = request.json()
            print(colour_cyan + "\n massiveM.py---" + colour_red + "Random Scan for bitcoin Addresses and Balance---------mizogg.co.uk" + colour_cyan + "---massiveM.py"  + colour_reset + seconds_to_str())
            print(colour_green + '\nWords for Wallet import : ' + colour_yellow + line + colour_reset)
            print (colour_green + "\nScan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
            print (colour_red +  ' <======================== Bitcoin Addresses Checked for Final Balance / Total Received / Total Sent==================>' + '\n' +  colour_reset)
            for row in request["addresses"]:
                print(row)
                if row["total_received"] > 0 or row["final_balance"] > 0: # final_balance or n_tx or total_received or total_sent
                    print (colour_purple +  ' <================================= WINNER WINNER WINNER =================================>' + '\n' +  colour_reset)
                    print (colour_green +  ' <====== WINNER WINNER WINNER ================================= WINNER WINNER WINNER ======>' + '\n' +  colour_reset)
                    print(colour_yellow + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
                    print (colour_purple +  ' <================================= WINNER WINNER WINNER =================================>' + '\n' +  colour_reset)
                    print (colour_green +  ' <====== WINNER WINNER WINNER ================================= WINNER WINNER WINNER ======>' + '\n' +  colour_reset)
                    f=open(u"winner.txt","a")
                    f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' )
                    f.write('\n mnemonics: ' + line)
                    f.write('\n<======= Bitcoin Addresses Checked for Final Balance / Total Received / Total Sent=======>')
                    f.write('\n' + const + "0" + '      Bitcoin Address : ' +  addr)
                    f.write('\n' + const + "1" + '      Bitcoin Address : ' +  addr1)
                    f.write('\n' + const + "2" + '      Bitcoin Address : ' +  addr2)
                    f.write('\n' + const + "3" + '      Bitcoin Address : ' +  addr3)
                    f.write('\n' + const + "4" + '      Bitcoin Address : ' +  addr4)
                    f.write('\n' + const + "5" + '      Bitcoin Address : ' +  addr5)
                    f.write('\n' + const + "6" + '      Bitcoin Address : ' +  addr6)
                    f.write('\n' + const + "7" + '      Bitcoin Address : ' +  addr7)
                    f.write('\n' + const + "8" + '      Bitcoin Address : ' +  addr8)
                    f.write('\n' + const + "9" + '      Bitcoin Address : ' +  addr9)
                    f.write('\n' + const + "10" + '     Bitcoin Address : ' +  addr10)
                    f.write('\n' + const + "11" + '     Bitcoin Address : ' +  addr11)
                    f.write('\n' + const + "12" + '     Bitcoin Address : ' +  addr12)
                    f.write('\n' + const + "13" + '     Bitcoin Address : ' +  addr13)
                    f.write('\n' + const + "14" + '     Bitcoin Address : ' +  addr14)
                    f.write('\n' + const + "15" + '     Bitcoin Address : ' +  addr15)
                    f.write('\n' + const + "16" + '     Bitcoin Address : ' +  addr16)
                    f.write('\n' + const + "17" + '     Bitcoin Address : ' +  addr17)
                    f.write('\n' + const + "18" + '     Bitcoin Address : ' +  addr18)
                    f.write('\n' + const + "19" + '     Bitcoin Address : ' +  addr19)
                    f.write('\n' + const + "20" + '     Bitcoin Address : ' +  addr20)
                    f.write('\n' + const + "21" + '     Bitcoin Address : ' +  addr21)
                    f.write('\n' + const + "22" + '     Bitcoin Address : ' +  addr22)
                    f.write('\n' + const + "23" + '     Bitcoin Address : ' +  addr23)
                    f.write('\n' + const + "24" + '     Bitcoin Address : ' +  addr24)
                    f.write('\n' + const + "25" + '     Bitcoin Address : ' +  addr25)
                    f.write('\n' + const + "26" + '     Bitcoin Address : ' +  addr26)
                    f.write('\n' + const + "27" + '     Bitcoin Address : ' +  addr27)
                    f.write('\n' + const + "28" + '     Bitcoin Address : ' +  addr28)
                    f.write('\n' + const + "29" + '     Bitcoin Address : ' +  addr29)
                    f.write('\n' + const + "30" + '     Bitcoin Address : ' +  addr30)
                    f.write('\n' + const + "31" + '     Bitcoin Address : ' +  addr31)
                    f.write('\n' + const + "32" + '     Bitcoin Address : ' +  addr32)
                    f.write('\n' + const + "33" + '     Bitcoin Address : ' +  addr33)
                    f.write('\n' + const + "34" + '     Bitcoin Address : ' +  addr34)
                    f.write('\n' + const + "35" + '     Bitcoin Address : ' +  addr35)
                    f.write('\n' + const + "36" + '     Bitcoin Address : ' +  addr36)
                    f.write('\n' + const + "37" + '     Bitcoin Address : ' +  addr37)
                    f.write('\n' + const + "38" + '     Bitcoin Address : ' +  addr38)
                    f.write('\n' + const + "39" + '     Bitcoin Address : ' +  addr39)
                    f.write('\n' + const + "40" + '     Bitcoin Address : ' +  addr40)
                    f.write('\n' + const + "41" + '     Bitcoin Address : ' +  addr41)
                    f.write('\n' + const + "42" + '     Bitcoin Address : ' +  addr42)
                    f.write('\n' + const + "43" + '     Bitcoin Address : ' +  addr43)
                    f.write('\n' + const + "44" + '     Bitcoin Address : ' +  addr44)
                    f.write('\n' + const + "45" + '     Bitcoin Address : ' +  addr45)
                    f.write('\n' + const + "46" + '     Bitcoin Address : ' +  addr46)
                    f.write('\n' + const + "47" + '     Bitcoin Address : ' +  addr47)
                    f.write('\n' + const + "48" + '     Bitcoin Address : ' +  addr48)
                    f.write('\n' + const + "49" + '     Bitcoin Address : ' +  addr49)
                    f.write('\n' + const + "50" + '     Bitcoin Address : ' +  addr50)
                    f.write('\n' + const + "51" + '     Bitcoin Address : ' +  addr51)
                    f.write('\n' + const + "52" + '     Bitcoin Address : ' +  addr52)
                    f.write('\n' + const + "53" + '     Bitcoin Address : ' +  addr53)
                    f.write('\n' + const + "54" + '     Bitcoin Address : ' +  addr54)
                    f.write('\n' + const + "55" + '     Bitcoin Address : ' +  addr55)
                    f.write('\n' + const + "56" + '     Bitcoin Address : ' +  addr56)
                    f.write('\n' + const + "57" + '     Bitcoin Address : ' +  addr57)
                    f.write('\n' + const + "58" + '     Bitcoin Address : ' +  addr58)
                    f.write('\n' + const + "59" + '     Bitcoin Address : ' +  addr59)
                    f.write('\n' + const + "60" + '     Bitcoin Address : ' +  addr60)
                    f.write('\n' + const + "61" + '     Bitcoin Address : ' +  addr61)
                    f.write('\n' + const + "62" + '     Bitcoin Address : ' +  addr62)
                    f.write('\n' + const + "63" + '     Bitcoin Address : ' +  addr63)
                    f.write('\n' + const + "64" + '     Bitcoin Address : ' +  addr64)
                    f.write('\n' + const + "65" + '     Bitcoin Address : ' +  addr65)
                    f.write('\n' + const + "66" + '     Bitcoin Address : ' +  addr66)
                    f.write('\n' + const + "67" + '     Bitcoin Address : ' +  addr67)
                    f.write('\n' + const + "68" + '     Bitcoin Address : ' +  addr68)
                    f.write('\n' + const + "69" + '     Bitcoin Address : ' +  addr69)
                    f.write('\n' + const + "70" + '     Bitcoin Address : ' +  addr70)
                    f.write('\n' + const + "71" + '     Bitcoin Address : ' +  addr71)
                    f.write('\n' + const + "72" + '     Bitcoin Address : ' +  addr72)
                    f.write('\n' + const + "73" + '     Bitcoin Address : ' +  addr73)
                    f.write('\n' + const + "74" + '     Bitcoin Address : ' +  addr74)
                    f.write('\n' + const + "75" + '     Bitcoin Address : ' +  addr75)
                    f.write('\n' + const + "76" + '     Bitcoin Address : ' +  addr76)
                    f.write('\n' + const + "77" + '     Bitcoin Address : ' +  addr77)
                    f.write('\n' + const + "78" + '     Bitcoin Address : ' +  addr78)
                    f.write('\n' + const + "79" + '     Bitcoin Address : ' +  addr79)
                    f.write('\n' + const + "80" + '     Bitcoin Address : ' +  addr80)
                    f.write('\n' + const + "81" + '     Bitcoin Address : ' +  addr81)
                    f.write('\n' + const + "82" + '     Bitcoin Address : ' +  addr82)
                    f.write('\n' + const + "83" + '     Bitcoin Address : ' +  addr83)
                    f.write('\n' + const + "84" + '     Bitcoin Address : ' +  addr84)
                    f.write('\n' + const + "85" + '     Bitcoin Address : ' +  addr85)
                    f.write('\n' + const + "86" + '     Bitcoin Address : ' +  addr86)
                    f.write('\n' + const + "87" + '     Bitcoin Address : ' +  addr87)
                    f.write('\n' + const + "88" + '     Bitcoin Address : ' +  addr88)
                    f.write('\n' + const + "89" + '     Bitcoin Address : ' +  addr89)
                    f.write('\n' + const + "90" + '     Bitcoin Address : ' +  addr90)
                    f.write('\n' + const + "91" + '     Bitcoin Address : ' +  addr91)
                    f.write('\n' + const + "92" + '     Bitcoin Address : ' +  addr92)
                    f.write('\n' + const + "93" + '     Bitcoin Address : ' +  addr93)
                    f.write('\n' + const + "94" + '     Bitcoin Address : ' +  addr94)
                    f.write('\n' + const + "95" + '     Bitcoin Address : ' +  addr95)
                    f.write('\n' + const + "96" + '     Bitcoin Address : ' +  addr96)
                    f.write('\n' + const + "97" + '     Bitcoin Address : ' +  addr97)
                    f.write('\n' + const + "98" + '     Bitcoin Address : ' +  addr98)
                    f.write('\n' + const + "99" + '     Bitcoin Address : ' +  addr99)
                    f.write('\n' + const + "100" + '     Bitcoin Address : ' +  addr100)
                    f.write('\n' + const + "101" + '     Bitcoin Address : ' +  addr101)
                    f.write('\n' + const + "102" + '     Bitcoin Address : ' +  addr102)
                    f.write('\n' + const + "103" + '     Bitcoin Address : ' +  addr103)
                    f.write('\n' + const + "104" + '     Bitcoin Address : ' +  addr104)
                    f.write('\n' + const + "105" + '     Bitcoin Address : ' +  addr105)
                    f.write('\n' + const + "106" + '     Bitcoin Address : ' +  addr106)
                    f.write('\n' + const + "107" + '     Bitcoin Address : ' +  addr107)
                    f.write('\n' + const + "108" + '     Bitcoin Address : ' +  addr108)
                    f.write('\n' + const + "109" + '     Bitcoin Address : ' +  addr109)
                    f.write('\n' + const + "110" + '     Bitcoin Address : ' +  addr110)
                    f.write('\n' + const + "111" + '     Bitcoin Address : ' +  addr111)
                    f.write('\n' + const + "112" + '     Bitcoin Address : ' +  addr112)
                    f.write('\n' + const + "113" + '     Bitcoin Address : ' +  addr113)
                    f.write('\n' + const + "114" + '     Bitcoin Address : ' +  addr114)
                    f.write('\n' + const + "115" + '     Bitcoin Address : ' +  addr115)
                    f.write('\n' + const + "116" + '     Bitcoin Address : ' +  addr116)
                    f.write('\n' + const + "117" + '     Bitcoin Address : ' +  addr117)
                    f.write('\n' + const + "118" + '     Bitcoin Address : ' +  addr118)
                    f.write('\n' + const + "119" + '     Bitcoin Address : ' +  addr119)
                    f.write('\n' + const + "120" + '     Bitcoin Address : ' +  addr120)
                    f.write('\n' + const + "121" + '     Bitcoin Address : ' +  addr121)
                    f.write('\n' + const + "122" + '     Bitcoin Address : ' +  addr122)
                    f.write('\n' + const + "123" + '     Bitcoin Address : ' +  addr123)
                    f.write('\n' + const + "124" + '     Bitcoin Address : ' +  addr124)
                    f.write('\n' + const + "125" + '     Bitcoin Address : ' +  addr125)
                    f.write('\n' + const + "126" + '     Bitcoin Address : ' +  addr126)
                    f.write('\n' + const + "127" + '     Bitcoin Address : ' +  addr127)
                    f.write('\n<======= Bitcoin Addresses Checked for Final Balance / Total Received / Total Sent=======>')
                    f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' )
                    f.close()
                    break
        except:
            pass

        # Reset counter
        query = []
        sleep(10) # Reduce Sleep to go faster
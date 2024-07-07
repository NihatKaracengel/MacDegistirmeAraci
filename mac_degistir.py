"""Dağınık kodlar"""
import subprocess
import optparse

print("Mac değiştirme başlatıldı.")

"""
subprocess: linux komutlarını çalıştırmaya yarayan kütüphane
optparse: bunların input almasını sağlayan kütüphane
"""

opt_objesi = optparse.OptionParser()
opt_objesi.add_option("-i","--interface", dest="interface", help="interface değiştirici")
opt_objesi.add_option("-m","--mac",dest="mac_adresi", help="yeni mac adresi")

"""tuple olduğu için çıktıları değişkene alalım:"""
(kullanici_girdileri, opt_argumanlari) = opt_objesi.parse_args()
print(f"Girilen interface: {kullanici_girdileri.interface}")
print(f"Girilen mac: {kullanici_girdileri.mac_adresi}")

interface_girdisi = kullanici_girdileri.interface
mac_adresi_girdisi = kullanici_girdileri.mac_adresi

subprocess.call(["ifconfig",interface_girdisi,"down"])
subprocess.call(["ifconfig",interface_girdisi,"hw","ether",mac_adresi_girdisi])
subprocess.call(["ifconfig",interface_girdisi,"up"])

"""yukarıdaki parantezli yerin açıklaması kolay:
kullanici_girdileri : wlan0 ile mac adresini girecek kullanıcı
opt_argumanlari ise -i , --interface, -m, --mac . bunlardır. bunlarla şu an bir işimiz yok.

#print(opt_objesi.parse_args()) #{'interface': None, 'mac_adresi': None}>, []

2 değişkenin 2 değerini aynı anda atamak
a,b = ("AAA","BBB")
print(a) #AAA
print(b) #BBB
"""

"""
interface : wlan0 eth0 portlarının genel adıdır.
dest = kaydedilecek yerdir. yani interface değişkeni üzerinedir.
help = açıklama kısmıdır.
kodu çalıştırmak için -i kısa hali --interface uzun hali
"""

#interface = "wlan0"
#mac_adresi = "00:11:22:22:11:22"



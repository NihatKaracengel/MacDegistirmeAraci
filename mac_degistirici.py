"""Düzenli kod ama eski kütüphane optparse"""
import subprocess
import optparse
import re

def kullanici_girdileri_fonk():
    opt_objesi = optparse.OptionParser()
    opt_objesi.add_option("-i","--interface", dest="interface_adi", help="interface değiştirici")
    opt_objesi.add_option("-m","--mac",dest="mac_adresi", help="yeni mac adresi")
    return opt_objesi.parse_args() #kullanıcının interface ve mac e yazacağı argümanlar dönüyor
    #buradan wlan0 ile 00:55:44:33:22:11 dönüyor.

"""
Bu fonksiyon, komut satırından alınacak argümanları tanımlar.
optparse.OptionParser(): Yeni bir OptionParser nesnesi oluşturur.
add_option("-i", "--interface", ...): Kullanıcıdan -i veya --interface argümanlarını alır ve bunu interface_adi olarak kaydeder.
add_option("-m", "--mac", ...): Kullanıcıdan -m veya --mac argümanlarını alır ve bunu mac_adresi olarak kaydeder.
return opt_objesi.parse_args(): Kullanıcının girdiği argümanları parse eder ve döner.
"""
def mac_degistiren_fonk(interface_girdisi, mac_adresi_girdisi):
    subprocess.call(["ifconfig",interface_girdisi,"down"])
    subprocess.call(["ifconfig",interface_girdisi,"hw","ether",mac_adresi_girdisi])
    subprocess.call(["ifconfig",interface_girdisi,"up"])

"""
Bu fonksiyon, verilen ağ arayüzünün MAC adresini değiştirir.
subprocess.call([...]): Verilen komutu çalıştırır.
İlk komut: ifconfig [interface_girdisi] down - Arayüzü kapatır.
İkinci komut: ifconfig [interface_girdisi] hw ether [mac_adresi_girdisi] - MAC adresini değiştirir.
Üçüncü komut: ifconfig [interface_girdisi] up - Arayüzü açar.
"""

def mac_kontrol(interface_adi):
    ifconfig = subprocess.check_output(["ifconfig",interface_adi])
    mac_bul = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if mac_bul:
        return mac_bul.group(0) #adamlar böyle yapmış. grup sonucu çıkarıyor 0 ile ilkini al.
    else:
        return None


print("Mac değiştirme başlatıldı.")
(kullanici_girdileri, opt_argumanlari) = kullanici_girdileri_fonk()
mac_degistiren_fonk(kullanici_girdileri.interface_adi,kullanici_girdileri.mac_adresi)
final_mac_adresi = mac_kontrol(str(kullanici_girdileri.interface_adi))

if final_mac_adresi == kullanici_girdileri.mac_adresi:
    print(f"Başarılı. Yeni mac adresi: {final_mac_adresi}")
else:
    print("Başarısız. Mac Adresi değişmedi.")

"""
print("Mac değiştirme başlatıldı."): Kullanıcıya işlem başladığını bildirir.
(kullanici_girdileri, opt_argumanlari) = kullanici_girdileri_fonk(): 
Kullanıcıdan alınan argümanları (-i --interface -m -mac) kullanici_girdileri ve opt_argumanlari değişkenlerine atar.
mac_degistiren_fonk(kullanici_girdileri.interface_adi, kullanici_girdileri.mac_adresi): 
Kullanıcının verdiği arayüz adı ve MAC adresini kullanarak mac_degistiren_fonk fonksiyonunu çağırır.
mac_kontrol ile kullanici_girdileri ne atadığımız dest olan interface_adinı alarak fonk çağırdık
"""



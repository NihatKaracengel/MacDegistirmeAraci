"""chatgpt ye argparse ile yazdırdığım final program"""

import subprocess
import argparse
import re

def kullanici_girdileri_fonk():
    # Argümanları işlemek için bir ArgumentParser nesnesi oluşturulur
    parser = argparse.ArgumentParser(description="MAC adresi değiştirme aracı")
    parser.add_argument("-i", "--interface", dest="interface_adi", required=True, help="Değiştirilecek ağ arayüzü")
    parser.add_argument("-m", "--mac", dest="mac_adresi", required=True, help="Yeni MAC adresi")
    # Kullanıcının girdiği argümanları parse eder ve döner
    return parser.parse_args()

"""
Bu fonksiyon, komut satırından alınacak argümanları tanımlar.
argparse.ArgumentParser(): Yeni bir ArgumentParser nesnesi oluşturur.
add_argument("-i", "--interface", ...): Kullanıcıdan -i veya --interface argümanlarını alır ve bunu interface_adi olarak kaydeder.
add_argument("-m", "--mac", ...): Kullanıcıdan -m veya --mac argümanlarını alır ve bunu mac_adresi olarak kaydeder.
return parser.parse_args(): Kullanıcının girdiği argümanları parse eder ve döner.
"""

def mac_degistiren_fonk(interface_girdisi, mac_adresi_girdisi):
    # Ağ arayüzünü kapat, MAC adresini değiştir ve arayüzü tekrar aç
    subprocess.call(["ifconfig", interface_girdisi, "down"])
    subprocess.call(["ifconfig", interface_girdisi, "hw", "ether", mac_adresi_girdisi])
    subprocess.call(["ifconfig", interface_girdisi, "up"])

"""
Bu fonksiyon, verilen ağ arayüzünün MAC adresini değiştirir.
subprocess.call([...]): Verilen komutu çalıştırır.
İlk komut: ifconfig [interface_girdisi] down - Arayüzü kapatır.
İkinci komut: ifconfig [interface_girdisi] hw ether [mac_adresi_girdisi] - MAC adresini değiştirir.
Üçüncü komut: ifconfig [interface_girdisi] up - Arayüzü açar.
"""

def mac_kontrol(interface_adi):
    # Belirtilen ağ arayüzünün mevcut MAC adresini kontrol et
    ifconfig = subprocess.check_output(["ifconfig", interface_adi])
    mac_bul = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if mac_bul:
        return mac_bul.group(0)  # Bulunan ilk MAC adresini döndür
    else:
        return None

"""
Bu fonksiyon, belirtilen ağ arayüzünün mevcut MAC adresini kontrol eder.
subprocess.check_output([...]): Verilen komutu çalıştırır ve çıktıyı döner.
re.search(...): MAC adresi formatına uygun bir dizeyi arar.
mac_bul.group(0): Bulunan ilk MAC adresini döner.
"""

print("Mac değiştirme başlatıldı.")
kullanici_girdileri = kullanici_girdileri_fonk()
mac_degistiren_fonk(kullanici_girdileri.interface_adi, kullanici_girdileri.mac_adresi)
final_mac_adresi = mac_kontrol(kullanici_girdileri.interface_adi)

if final_mac_adresi == kullanici_girdileri.mac_adresi:
    print(f"Başarılı. Yeni mac adresi: {final_mac_adresi}")
else:
    print("Başarısız. Mac Adresi değişmedi.")

"""
print("Mac değiştirme başlatıldı."): Kullanıcıya işlem başladığını bildirir.
kullanici_girdileri = kullanici_girdileri_fonk(): Kullanıcıdan alınan argümanları döner. (-i --interface -m -mac)
mac_degistiren_fonk(kullanici_girdileri.interface_adi, kullanici_girdileri.mac_adresi): Kullanıcının verdiği arayüz adı ve MAC adresini kullanarak MAC adresini değiştirir.
final_mac_adresi = mac_kontrol(kullanici_girdileri.interface_adi): Belirtilen arayüzün yeni MAC adresini kontrol eder.
if final_mac_adresi == kullanici_girdileri.mac_adresi: MAC adresi başarılı bir şekilde değiştirilmiş mi kontrol eder ve sonucu yazdırır.
"""


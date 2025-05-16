def buchstabe_zu_position(c):
    c = c.lower()
    ersatz = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'}
    for umlaute, ersatztext in ersatz.items():
        c = c.replace(umlaute, ersatztext)
    return ord(c[0]) - ord('a')  # nur erster Buchstabe

def dezimal_zu_5bit_bin(n):
    return bin(n)[2:].zfill(5)

def berechne_paritaet(bin_str):
    anzahl_einsen = bin_str.count('1')
    return '0' if anzahl_einsen % 2 == 0 else '1'

def nachname_zu_bin_mit_paritaet(nachname):
    buchstaben = nachname[:3]  # nur erste drei
    positionen = [buchstabe_zu_position(c) for c in buchstaben]
    bin_teile = [dezimal_zu_5bit_bin(p) for p in positionen]
    bin_gesamt = ''.join(bin_teile)
    paritaet = berechne_paritaet(bin_gesamt)
    return bin_gesamt + paritaet

# Beispiel:
nachname = input("Bitte gib die ersten drei Buchstaben deines Nachnamens ein: ")
ergebnis = nachname_zu_bin_mit_paritaet(nachname)
print("Ausgabe:", ergebnis)

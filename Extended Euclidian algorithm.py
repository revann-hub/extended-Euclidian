
def genisletmis_ebob(x, y):
    if y == 0:
        return x, 1, 0
    e, u, v = genisletmis_ebob(y, x % y)
    return e, v, u - (x // y) * v

def modul_ters(p, q):
    e, u, _ = genisletmis_ebob(p, q)
    if e != 1:
        return None  
    return u % q

def yoxla(p, q, e, u, v):
    return p * u + q * v == e

def esas():
    print("Genişlənmiş Evklid Alqoritmi")
    try:
        bir = int(input("Birinci ədəd: "))
        iki = int(input("İkinci ədəd: "))
    except ValueError:
        print("Zəhmət olmasa düzgün tam ədəd daxil edin")
        return
    e, u, v = genisletmis_ebob(bir, iki)
    print("\nNəticələr:")
    print("ƏBOB:", e)
    print("u:", u)
    print("v:", v)
    if yoxla(bir, iki, e, u, v):
        print("Təsdiqləndi: a·x + b·y = ƏBOB")
    else:
        print("Təsdiqləmə uğursuz oldu")
    ters = modul_ters(bir, iki)
    if ters is not None:
        print(f"✅ {bir} ədədinin mod {iki} üzrə tərs elementi:", ters)
        print(f"Yoxlama: ({bir} * {ters}) % {iki} =", (bir * ters) % iki)
    else:
        print(f"{bir} ədədinin mod {iki} üzrə tərs elementi mövcud DEYİL")

if __name__ == "__main__":
    esas()

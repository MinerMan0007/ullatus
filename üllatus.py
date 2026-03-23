import os

def kas_net_on():
    os.system("ping -n 5 google.com")
    if "Lost = 0":
        küsib_veel = input("hästi net on kas lõbu pärasy soovid ühe korra kontrolli veel(jah/ei): ")
        if küsib_veel == "jah":
            kas_net_on()
    else:
        print("midagi valesti")
        küsib_uuesti = input("kas soovid uuesti kontrollida? (jah/ei): ")
        if küsib_uuesti == "jah":
            kas_net_on()
        else:
            print("ma ei viitsin siin änam olla kui sa ei soovi minu abi")
            exit()


kas_net_on()

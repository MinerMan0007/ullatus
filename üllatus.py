import os

def kas_net_on():
    print("kontrollin ühendus....")
    vastus = os.popen("ping -n 5 8.8.8.8").read()
    if "Lost = 0" in vastus:
        küsib_veel = input("hästi net on kas lõbu pärast soovid ühe korra kontrolli veel(jah/ei): ")
        if küsib_veel == "jah":
            kas_net_on()
        else:
            browser = input("kas soovid hakata neti kasutama pane (google-chrome, firefox, safari, opera, msedge) või ei: ")
            if browser == "ei":
                exit()
            else:
                os.startfile(f"{browser}")

    else:
        print("midagi valesti")
        küsib_uuesti = input("kas soovid uuesti kontrollida? (jah/ei): ")
        if küsib_uuesti == "jah":
            kas_net_on()
        else:
            print("ma ei viitsin siin änam olla kui sa ei soovi minu abi")
            exit()



kas_net_on()

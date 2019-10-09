import wifiidscript

test = wifiidscript.wdang()

if test.checkPing() == 0:
    print("Network Active")
else:
    test.login()
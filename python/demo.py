import deversal


device = deversal.Device("0xE8eb35AFBA98fdE9071308b4F7cfB844EE5bf666", "localhost", "1337")
status = device.getValue()
print status["name"]




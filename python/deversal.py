import requests



class Device:
    def __init__(self, _address, _bridgeIP, _port):
        self.address = _address
        self.bridgeURI = "http://" + _bridgeIP + ":" + str(_port)
        self.deviceStatusAPi = "/status/device/"

    def getValue(self):
        _url = self.bridgeURI + self.deviceStatusAPi + "?addr=" + self.address
        r = requests.get(_url)
        r = r.json()
        return r



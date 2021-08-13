from fakeap import *
from scapy.layers.eap import EAPOL, EAP, SNAP

airmon-ng start wlan0 11
ap = FakeAccessPoint('wlan0mon', 'Hello', '')
ap.run()
from fakeap import *
from scapy.layers.eap import EAPOL, EAP, SNAP
from subprocess import call

def main(interface):
	call(["airmon-ng", "start", interface, "11"])
	ap = FakeAccessPoint('wlan1mon', 'Hello', '')
	ap.run()

from fakeap import *
from scapy.layers.eap import EAPOL, EAP, SNAP
from subprocess import call
from sys import argv, exit
from parser import *
import signal

interface_previous_name = ""

def signal_handler(sig, frame):
	global interface_previous_name
	call(["./reset_interfaces.sh", interface_previous_name])

def prepare_interfaces(interface):
	call(["rfkill", "unblock", "all"])
	call(["ifconfig", interface, "down"])
	call(["ip", "link", "set", interface, "name", "wlan"])
	call(["airmon-ng", "start", "wlan", "11"])
	call(["ifconfig", "wlanmon", "up"])

def initialize_AP(config_file, fake_ap):
	parser_(config_file, 2, fake_ap)

def main(config_file):
	global interface_previous_name
	interface_previous_name = parser_(config_file, 1)
	signal.signal(signal.SIGINT, signal_handler)

	prepare_interfaces(interface_previous_name)
	fap = FakeAccessPoint()
	initialize_AP(config_file, fap)
	fap.start()
	fap.run()
	# ap = FakeAccessPoint('wlan1mon', 'Hello', '')
	# ap.run()


if __name__ == '__main__':
	if len(argv) != 2:
		print("Required number of arguments does not match")
		exit(1)
	main(argv[1])
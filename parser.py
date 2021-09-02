from json import load

def parser_(filename, step, fakeap=None):
	f = open(filename,)
	data = load(f)
	f.close()

	if step == 1:
		return data['interface']
	else:
		fakeap.channel = int(data['channel'])
		fakeap.interface = "wlanmon"
		print("la", fakeap.interface)
		fakeap.ssid = data['ssid']
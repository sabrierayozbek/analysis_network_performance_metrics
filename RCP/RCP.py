import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

a_file = open("iz.tr", "r")
line_number = len(open('iz.tr').readlines())
list_of_lists = [(line.strip()).split() for line in a_file]

a_file.close()

exdf = pd.DataFrame(list_of_lists)

data = {'Event': exdf[0],
        'Time': exdf[1],
        'Source Node': exdf[2],
        'Destination Node': exdf[3],
        'Packet Name': exdf[4],
        'Packet Size': exdf[5],
        'Flags': exdf[6],
        'Flow ID': exdf[7],
        'Source Address': exdf[8],
        'Destination Address': exdf[9],
        'Sequence Number': exdf[10],
        'Packet Unique ID': exdf[11]}

df = pd.DataFrame(data)
events = df['Event']
times = df['Time']
packets = df['Packet Name']
packets_size = df['Packet Size']
sent_packet = 0
totaltime = 0
t = []
r = []
counter = 1
routing_c_packets = 0

for i in range(line_number - 1):
	if float(times[i]) - counter <= 1:
		if events[i] == '+' and packets[i] == 'tcp':
			if int(packets_size[i]) == 40:
				sent_packet += int(packets_size[i])  # gönderilmiş paket boyutlarının toplamı
				totaltime += float(times[i])
		if events[i] == '+' and packets[i] == 'ack':
			if int(packets_size[i]) == 40:
				sent_packet += int(packets_size[i])  # gönderilmiş paket boyutlarının toplamı
				totaltime += float(times[i])
	else:
		t.append(counter)
		counter += 1
		routing_c_packets = sent_packet
		r.append(routing_c_packets)
		sent_packet = 0
		

style.use('ggplot')
plt.title('Routing Control Packets: Metrik Grafiği')
plt.ylabel('Routing Control Packets Değerleri')
plt.xlabel('Zaman(sn) - Her 1 saniyeye tekabül etmektedir.')
plt.plot(t, r, 'r', linewidth=2)
plt.grid(True, color='k')
plt.savefig("grafik.png", dpi=300)
plt.show()
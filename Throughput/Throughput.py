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
received_packet = 0
totaltime = 0
t = []
r = []
counter = 1
throughput = 0

for i in range(line_number-1):
    if float(times[i]) - counter <= 1:
        if events[i] == 'r':
                if packets[i] == 'tcp':
                        received_packet += int(packets_size[i]) #alınmış paket boyutlarının toplamı
                        totaltime += float(times[i])
                if packets[i] == 'ack':
                        received_packet += int(packets_size[i]) #alınmış paket boyutlarının toplamı
                        totaltime += float(times[i])
    else:
        t.append(counter)
        counter += 1
        throughput = (received_packet * 8 / totaltime * 1000)
        r.append(throughput)
        received_packet = 0
        totaltime = 0


style.use('ggplot')
plt.title('Throughput Performans Grafiği')
plt.ylabel('Throughput Değerleri')
plt.xlabel('Zaman(sn) - Her 1 saniyeye tekabül etmektedir.')
plt.plot(t, r, 'r', linewidth=2)
plt.grid(True, color='k')
plt.savefig("grafik.png", dpi=300)
plt.show()
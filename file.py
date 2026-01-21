from obspy import read_inventory

inv = read_inventory("invvStations.xml")
inv.write('inv2stations.xml', format='STATIONXML')
print("hello")
print("dodaje zmiany z gita")
print("dodaje zmiany z pycharma")


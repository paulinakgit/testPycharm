from obspy import read_inventory

inv = read_inventory("invvStations.xml")
inv.write('inv2stations.xml', format='STATIONXML')
jghjgjg

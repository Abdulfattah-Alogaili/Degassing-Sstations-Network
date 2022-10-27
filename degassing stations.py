#Building Stations network along with connected wells

#Import dataset sort_category 
import pandas as pd 
#import pyvis to construct our network
import pyvis.network as nt
df = pd.read_csv('sort_category.txt', sep = '\t')
#describe to get clear understanding for our data
net = nt.Network(width=1500, height=1000)

#step - 1 import the unique flow stations (these units going to be the main points)
flow_stations = df['Flow_Station'].unique()

#step - 2 add flow stations as nodes 
for station in flow_stations:
    net.add_node(station, color='#b434eb')

# step 3 get all the wells 
packed_well = zip(df['UID'], df['Water Production'])
for well, water in packed_well:
    if water > 900:
        net.add_node(well, value = water, shape = 'square')
    else:
        net.add_node(well, value= water)
    
#loop through dataframe items
packed_value = zip(df['UID'], df['Flow_Station'], df['GOR'])
for well,flow,gor in packed_value:
    if gor > 160:
        net.add_edge(source = well, to = flow, value = gor/10, color = 'red')
    else:
        net.add_edge(source = well, to = flow, value = gor/10)
net.show('degassing.html')
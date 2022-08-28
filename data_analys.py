from statistics import *
from bs4 import BeautifulSoup as bs

colors = []

with open( "data.html" ) as data:
    doc = bs( data, "html.parser" )

for item in doc.find_all( "td", class_="color" ):
    colors.extend( item.get_text().replace( " ", "" ).split( "," ) )


tracker = set(colors)

color_freq = {}
counter = []
for item in tracker:
    counter.append(colors.count(item))
    color_freq[item] = colors.count(item)


mean_value  = int( mean( counter ) )

for item in color_freq:
    if(color_freq[item] == mean_value):
        print("The mean color is {0}".format( item ))

mode_color = mode(colors)

print("The mode color is {0}".format( mode_color ) )

median_color = median( color_freq )

print( "The median color is {0}".format(median_color ) )

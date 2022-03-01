from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_data = []
    severe = []
    high = []
    moderate = []
    low = []

    for station in stations:

        #if no data, put in a separate list with warning
        #lack of data doesn't mean that they're not possibly flooded
        #if relative water level is not none & it's consistent
        if station.typical_range_consistent() != False and type(station.relative_water_level()) == float:

            #find factor of relative water level compared to typical range 
            low_level = station.typical_range[0]
            high_level = station.typical_range[1]
            #how much higher is relative over typical low / typical range
            factor = (station.relative_water_level()-low_level) / (high_level - low_level)

            #divide the stations into risk categories
            #adding *town* not name, though
            if factor >= 3:
                severe.append((station.town, factor))
            elif factor >= 2:
                high.append((station.town, factor))
            #if relative level is around the typical high level:
            elif factor >= 1:
                moderate.append((station.town, factor))
            #if less than high level, town is probably not being flooded
            else:
                low.append((station.town, factor))

        else:
            inconsistent_data.append(station.town)

    #removing duplicates
    severe = set(severe)
    high = set(high)
    moderate = set(moderate)
    low = set(low)
    
    #un-set the lists
    severe = list(severe)
    high = list(high)
    moderate = list(moderate)
    low = list(low)

    #sort each risk category list from greatest factor to smallest
    severe = sorted(severe, key=lambda x:-x[1])
    high = sorted(high, key=lambda x:-x[1])
    moderate = sorted(moderate, key=lambda x:-x[1])
    low = sorted(low, key=lambda x:-x[1])


    

    print("Towns most at risk of flooding")
    #print(severe)
    mostRisk = [i[0] for i in severe]
    #print(mostRisk) 
    for i in range(len(mostRisk)):
        print("{}".format(mostRisk[i]))
   








run()
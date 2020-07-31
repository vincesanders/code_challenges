class Customer:

    def __init__(self, id, start_time, end_time, location):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

class UndergroundSystem:

    def __init__(self):
        self.station_times = {}
        self.customers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id is None or stationName is None or t is None:
            return None

        if id not in self.customers:
            self.customers[id] = Customer(id, t, None, stationName)
        else:
            self.customers[id].start_time = t
            self.customers[id].location = stationName

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id is None or stationName is None or t is None:
            return None

        if id not in self.customers:
            return None
        else:
            self.customers[id].end_time = t

        time_this_trip = self.customers[id].end_time - self.customers[id].start_time

        start_station = self.customers[id].location

        if (start_station, stationName) not in self.station_times:
            self.station_times[(start_station, stationName)] = {
                'average': time_this_trip, 
                'total': time_this_trip, 
                'num_entries': 1
            }
        else:
            self.station_times[(start_station, stationName)]['num_entries'] += 1
            self.station_times[(start_station, stationName)]['total'] += time_this_trip
            total = self.station_times[(start_station, stationName)]['total']
            num = self.station_times[(start_station, stationName)]['num_entries']
            self.station_times[(start_station, stationName)]['average'] = total / num


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.station_times:
            return None

        return self.station_times[(startStation, endStation)]['average']


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
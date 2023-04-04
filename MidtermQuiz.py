class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def mtoc(self):
        return self.__distance * 100

    def mtok(self):
        return self.__distance / 1000

    def mtoi(self):
        return self.__distance * 39.37


distance_in_meters = float(input("Enter your distance: "))

dc = DistanceConversion(distance_in_meters)

print("Distance in cm:", dc.mtoc())
print("Distance in km:", dc.mtok())
print("Distance in inch:", dc.mtoi())
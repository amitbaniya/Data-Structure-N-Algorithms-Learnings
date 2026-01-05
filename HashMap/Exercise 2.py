
class Weather:
    def __init__(self):
        self.jan_weather = {}

    def csv_to_dict(self):
        with open('nyc_weather.csv', 'r') as f:
            for line in f:
                pair = line.split(',')
                try:
                    temperature = int(pair[1])
                    self.jan_weather[pair[0]] = temperature
                except:
                    print("Invalid temperature")


if __name__ == '__main__':
    w = Weather()
    w.csv_to_dict()
    print(w.jan_weather)
    print(w.jan_weather['Jan 9'])
    print(w.jan_weather['Jan 4'])

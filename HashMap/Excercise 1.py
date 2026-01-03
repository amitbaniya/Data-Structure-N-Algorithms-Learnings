
class Weather:
    def __init__(self):
        self.jan_weather = []

    def csv_to_list(self):
        with open('nyc_weather.csv', 'r') as f:
            for line in f:
                pair = line.split(',')
                try:
                    temperature = int(pair[1])
                    self.jan_weather.append(temperature)
                except:
                    print("Invalid temperature")

    def average_temperature_first_week(self):
        return round(sum(self.jan_weather[0:7])/7, 2)

    def max_temp_ten_days(self):
        return max(self.jan_weather)

if __name__ == '__main__':
    w = Weather()
    w.csv_to_list()
    print(w.jan_weather)
    print(w.average_temperature_first_week())
    print(w.max_temp_ten_days())
import requests


class City():
    def __init__(self, name, longtitude, latitude):
        self.name = name
        self.longtitude = longtitude
        self.latitude = latitude

    def get_temp(self):
        try:
            responce = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={self.latitude}&lon={self.longtitude}&appid=b05cb427be25ccb8d01b1be8ca15db41")
        except:
            return "Sorry, we have some problem with your responce"

        responce = responce.json()

        return [responce["main"]["temp"], responce["main"]["temp_max"], responce["main"]["temp_min"]]

    def get_info_temp(self):
        temp, temp_max, temp_min = self.get_temp()
        info = f"The currently temperature in {self.name} = {temp}°C\nMax temperature in {self.name} = {temp_max}°C\nMin temperature in {self.name} = {temp_min}°C"
        return info

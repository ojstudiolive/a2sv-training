class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        celsius = float(celsius)
        kelvin = "{:.5f}".format(celsius + 273.15)
        far =  "{:.5f}".format(celsius *1.80 + 32.00)
        conversion_mes = f'Temperatue at {celsius} Celsius converted in Kelvin is {kelvin} and converted in Fahrenheit is {far}'
        print(conversion_mes)

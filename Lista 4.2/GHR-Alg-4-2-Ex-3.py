print("Celsius\t|Fahrenheit|")
for i in range(0,101,10):
    fh = (i*9/5)+32
    print(f"{int(i)}°C\t|{int(fh)}°F")
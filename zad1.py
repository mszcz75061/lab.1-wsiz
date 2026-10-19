print(type(1 + 2), 1 + 2) #1 operator + wykonuje dodawanie liczb całkowitych    
print(type(1 + 4.5), 1 + 4.5) #2 operator + wykonuje dodawanie liczb zmiennoprzecinkowych
print(type(3 / 2), 3 / 2) #3 operator / wykonuje dzielenie klasyczne
print(type(4 / 2), 4 / 2) #4 operator / wykonuje dzielenie liczb 
print(type(3 // 2), 3 // 2) #5 operator // wykonuje dzielenie całkowitoliczbowe 
print(type(-3 // 2), -3 // 2) #6 operator // wykonuje dzielenie całkowitoliczbowe (zaokragla w dół)
print(type(11 % 2), 11 % 2) #7 operator % daje resztę z dzielenia liczb całkowitych 
print(type(2 ** 10), 2 ** 10) #8 operator ** wykonuje potęgowanie
print(type(8 ** (1/3)), 8 ** (1/3)) #9 operator ** wykonuje potęgowanie

print("-" * 30)

print(type(int(3.0)), int(3.0)) #10 Konwertuje liczbę zmiennoprzecinkową na całkowitą, obcinając część ułamkową.
print(type(float(3)), float(3)) #11 Konwertuje liczbę całkowitą na zmiennoprzecinkową.
print(type(float("3")), float("3")) #12 Konwertuje ciąg znaków na zmiennoprzecinkową liczbę.
print(type(str(12.4)), str(12.4)) #13 Konwertuje liczbę zmiennoprzecinkową na tekst.
print(type(bool(0)), bool(0)) #14 Konwertuje wartość na typ logiczny.


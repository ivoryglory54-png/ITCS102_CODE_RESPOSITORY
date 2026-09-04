money = 501

I = 1000 
V = 500 
O = 200
R = 100
Y = 50
C = 20 
U = 10
T = 5 
E = 1

print("Balance", money)

Izero = money // I
money = money % I
print("1000=", Izero)

Vzero = money // V
money = money % V
print("500=", Vzero)

Ozero = money // O
money = money % O
print("200=", Ozero)

Rzero = money // R
money = money % R
print("100=", Rzero)

Yzero = money // Y
money = money % Y
print("50=", Yzero)

Czero = money // C
money = money % C
print("20=", Czero)

Uzero = money // U
money = money % U
print("10=", Uzero)

Tzero = money // T
money = money % T
print("5=", Tzero)

Ezero = money // E
money = money % E
print("1=", Ezero)
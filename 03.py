#!/usr/bin/python3
sin = float(input('身長をm単位で入力して下さい> '))
tai = float(input('体重をkg単位で入力して下さい> '))
BMI = tai / sin**2
print(BMI)
if BMI < 18.5:
    print('やせ')
elif BMI < 25:
    print('標準')
elif BMI < 30:
    print('肥満')
else:
    print('高度肥満')

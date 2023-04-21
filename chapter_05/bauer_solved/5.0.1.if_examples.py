age = 17
if age >= 18:
    print('Możesz wziąć udział w głosowaniu')
    print('Czy zarejestrowałeś się już, aby móc głosować?')
else:
    print('Przykro nam, jesteś zbyt młody aby głosować.')
    print('Możesz się zarejestrować po ukończeniu 18 lat!')

age = 13
if age < 4:
    print('Cena biletu wstępu wynosi: 0 zł.')
elif age < 18:
    print('Cena biletu wstępu wynosi: 25 zł.')
else:
    print('Cena biletu wstępu wynosi: 40 zł.')
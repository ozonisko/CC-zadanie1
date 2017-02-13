# CC-zadanie1
Task 1: The odds are even in this war of mine The struggle

Zauważyłem kilka błędów w przykładach do zadania
battle([7,-3,-14,6]) => "evens win" // 111-11 vs -1110+110, 3-2 vs -1+1
1 > 0 czyli chyba 'oddsy' powinny wygrać

battle([17,-3, 32, -24]) => "tie" // 10111-11 vs 100000-11000, 4-2 vs 5-3
17 binarnie to 10001 nie 10111, więc wynik też będzie inny

Zrobiłem to zadanie moim zdaniem najłatwiejszym sposobem lecz pewnie nie najszybszym

Sprawdzałem czy liczba jest ujemna, jeżeli tak ustawiałem flage spyAlert
Dzieliłem liczby na parzyste i nieparzyste, zamieniałem na postać binarną i iterując
po kolejnych bitach sprawdzałem ilość 0 i 1
Jeżeli flaga spyAlert była True to zamiast dodawać odejmowałem zliczone 1 lub 0 
od całej puli

Pewnie program działałby szybciej gdyby użyć szybkich operacji binarnych lecz myślę, że nie było to wymagane

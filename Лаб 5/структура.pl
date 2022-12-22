%keyboard("Фирма производитель", "Тип соединения", "Тип клавиатуры", "Раскладка", "Кол-во клавиш клавиатуры")

keyboard(hyperx, wired, mechanical, eng, 104).
keyboard(sven, wired, membrane, ru, 104).
keyboard(rii, wireless, membrane, eng, 70).
keyboard(gembird, wired, membrane, ru, 104).
keyboard(defender, wired, membrane, ru, 104).

mechan_keyboard(X):- keyboard(X,_,mechanical,_,_).
ru_keyboard(X):- keyboard(X,_,_,ru,_).
wireless_keyboard(X):- keyboard(X,wireless,_,_,_).

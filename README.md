# prog_pyproj_2
ФИО: Титов Павел Александрович

ИСУ: 474374

Описание:
Я написал программу макрос. Пользователь вводит клавиши, которые программа будет нажимать сама. Необходимо в файле main задать интервал между нажатиями, количество повторений/время повторения, горячую клавиша для включения, которая издает звук, при успешном принятии ее программой. Применение программы ограничивается только фантазией пользователя. Можно использовать для автоматизации рутинных процессов

Пример:

#задаем значения вручную в файле main
keys = ["a", "b", "c"]
interval = 5
repeat_value= None
repeat_time= 10
hotkey = "m"

#запускаем программу 
To on simulation use: m

#нажимаем горячую клавишу как только откроем нужное для нас окно
Simulation starts working

#клавиши нажимаются с интервалами
abc

#симуляция завершается
Simulation is ended



Комментарий:
Проект оказался в разы сложнее, чем я думал, поэтому пришлось очень многое спрашивать у gpt, тк без него я бы потратил намного больше времени на поиск информации по использованию новых для меня библиотек. Также возникли проблемы с операционной системой, некоторые библиотеки, которые я хотел использовать, операционка просто не разрешала использовать (keyboard). Было очень много попыток разобраться с выключением программы тем же хоткеем, что включает ее, но я зашел в тупик и не смог это реализовать, но надеюсь это не критично, программа работает практически как заявлено. Расчет на строгое практическое применение опытными юзерами, поэтому интерфейсу уделялось мало внимания

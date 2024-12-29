"""
Файл с основным функционалом программы (сам класс макроса)
"""
from pynput import keyboard
import time
import pyautogui  #использовал именно эту библиотеку, так как она может управлять как клавиатурой, так и мышью, что
                  #может оказаться полезным для дальнейшего развития проекта
from playsound import playsound
from exceptions import InvalidRepeatError, InvalidRepeatValueError, InvalidRepeatTimeError
from decorators import validate_positive_int, validate_keys


class Macros_class():

    def __init__(self, keys, interval, repeat_value, repeat_time, hotkey):
        """
        Задача переменных класса
        """

        if interval == 0:   #я прочитал, что лучше всегда задавать интервал для корректной работы программы
            interval = 0.0015

        self.keys = keys
        self.interval = interval
        self.repeat_value = repeat_value
        self.repeat_time = repeat_time
        self.hotkey = hotkey

        self.active = False
        self.sound_file = "hotkey_sound.mp3"
        self.current_repeat = 0
        self.start_time = None
        self.duration = None

        self._validate_repeat()
        self._validate_interval()

    @validate_keys
    def _validate_keys(self):
        """
        Проверка на корректность ключей
        """
        pass

    @validate_positive_int
    def _validate_interval(self):
        """
        Проверка на корректность интервала
        """
        pass

    def _validate_repeat(self):
        """
        Валидация для повторения
        """
        if self.repeat_value is not None and self.repeat_time is not None:
            raise InvalidRepeatError("Both repeat value and repeat time cannot be set")

        if self.repeat_value is None and self.repeat_time is None:
            raise InvalidRepeatError("Either repeat value or repeat time must be choosed")

        if self.repeat_value is not None and self.repeat_value <= 0:
            raise InvalidRepeatValueError("Repeat value must be positive")

        if self.repeat_time is not None and self.repeat_time <= 0:
            raise InvalidRepeatTimeError("Repeat time must be positive")

    def start(self):
        """
        Запуск симуляции нажатий
        """
        if self.active == True:
            print("Program is already working")
            return

        self.active = True
        print("Simulation starts working")
        self.current_repeat = 0
        self.start_time = time.time()
        while self.active:
            if self.repeat_value is not None and self.current_repeat >= self.repeat_value:
                break

            if self.repeat_time is not None and time.time() - self.start_time >= self.repeat_time:
                break

            for key in self.keys:
                if not self.active:
                    break
                pyautogui.press(key)
                time.sleep(self.interval)
            self.current_repeat += 1

        self.active = False
        print("Simulation is ended")

    def stop(self):
        """
        Остановка симуляции
        """
        print("Simulation stopped")
        self.active = False

    def toggle(self):
        """
        Проигрывание звука, смена состояния
        """
        if self.sound_file:
            playsound(self.sound_file)  # Проигрывание звука при переключении состояния

        if self.active:
            self.stop()
        else:
            self.start()

    def listen_for_hotkey(self):
        """
        Задача горячей клавиши
        """

        def on_press(key):
            try:
                if isinstance(key, keyboard.KeyCode) and key.char == self.hotkey:
                    self.toggle()  # Переключение состояния программы

                elif key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r] and self.hotkey.lower() == "ctrl":
                    self.toggle()

            except AttributeError:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # Этот вызов запускает слушатель в фоновом формате
        print(f"To on simulation use: {self.hotkey}")
        listener.join()  # Это блокирует основной поток, пока не нажата горячая клавиша

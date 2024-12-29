from Macros import Macros_class

keys = ["a", "b", "c"]
interval = 5
repeat_value= None
repeat_time= 10
hotkey = "m"


simulator = Macros_class(
    keys=keys,
    interval=interval,
    repeat_value=repeat_value,
    repeat_time=repeat_time,
    hotkey=hotkey,
)

simulator.listen_for_hotkey()

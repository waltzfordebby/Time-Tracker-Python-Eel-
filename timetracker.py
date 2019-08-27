import eel

eel.init('web')

@eel.expose
def say_hello_py(x):
    print(f"Hello from {x}")

say_hello_py("Python World!")
eel.say_hello_js("Python World")

eel.start("main.html", size=(600,500))
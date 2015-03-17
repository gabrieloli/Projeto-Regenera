import os
import numpy
import time
import thread
import threading
import sys
import serial

serial = serial.Serial('/dev/ttyACM0', 9600)

random = numpy.random.randint(1, 3)

def speak(n):
    speech = 'espeak -vpt+f3 -k5 -s150' + ' ' + '"' + n + '"' + " 2>/dev/null"
    print speech
    os.system(speech)

def raw_input_with_timeout(prompt, timeout=14):    
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = raw_input(prompt)
    except KeyboardInterrupt:
        pass
    timer.cancel()
    for char in astring:
     time.sleep(0.2)
     sys.stdout.write(char)
     sys.stdout.flush()

    return astring

speak("Nucleos iniciados com sucesso")
speak("Administrador,insira seu comando,por favor")
user_input = raw_input_with_timeout("Comando ")

serial.write('4')

if user_input == 'Debug':
    time.sleep(1)
    serial.write('5')
    time.sleep(0.2)
    speak("Modo de Desenvolvedor iniciado")
else:
    speak("ok")

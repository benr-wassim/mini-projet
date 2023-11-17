#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Définir la numérotation des broches (BCM ou BOARD)
GPIO.setmode(GPIO.BCM)

# Configurer la broche comme une sortie
GPIO.setup(17, GPIO.OUT)

# Éteindre la LED en mettant la broche à LOW
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()
print("LED éteinte")

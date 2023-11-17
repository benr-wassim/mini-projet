#!/usr/bin/python
import RPi.GPIO as GPIO

# Définir la numérotation des broches (BCM ou BOARD)
GPIO.setmode(GPIO.BCM)

# Configurer la broche comme une sortie
GPIO.setup(17, GPIO.OUT)

# Allumer la LED en mettant la broche à HIGH
GPIO.output(17, GPIO.HIGH)

print("LED allumée")

#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

# Définir la numérotation des broches (BCM ou BOARD)
GPIO.setmode(GPIO.BCM)

# Configurer les broches comme des sorties
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Créer des objets PWM pour chaque broche avec une fréquence de 50 Hz
pwm_R = GPIO.PWM(17, 50)
pwm_G = GPIO.PWM(27, 50)
pwm_B = GPIO.PWM(22, 50)

# Démarrer les PWM avec un rapport cyclique de 0%
pwm_R.start(0)
pwm_G.start(0)
pwm_B.start(0)


# Fonction pour définir la couleur de la LED RGB
def set_led_color(red, green, blue):
    # Convertir les valeurs de 0-255 à 0-100 pour le rapport cyclique PWM
    pwm_R.ChangeDutyCycle(red / 2.55)
    pwm_G.ChangeDutyCycle(green / 2.55)
    pwm_B.ChangeDutyCycle(blue / 2.55)

# Si les valeurs de couleur sont fournies en ligne de commande
    red_value = int(sys.argv[1])
    green_value = int(sys.argv[2])
    blue_value = int(sys.argv[3])

    set_led_color(red_value, green_value, blue_value)

# Éteindre la LED
set_led_color(0, 0, 0)

# Arrêter les PWM et nettoyer les broches GPIO
pwm_R.stop()
pwm_G.stop()
pwm_B.stop()
GPIO.cleanup()

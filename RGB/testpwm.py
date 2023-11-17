import RPi.GPIO as GPIO
import time

# Configuration des broches pour le contrôle PWM
GPIO.setmode(GPIO.BCM)  # Utilisation de la numérotation des broches BCM
led_pins = [17, 27, 22]  # Remplacez ces valeurs par les broches que vous utilisez

# Configuration des broches en mode PWM
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Création d'objets PWM pour chaque composante RGB
led_pwm = [GPIO.PWM(pin, 100) for pin in led_pins]

# Démarrage des signaux PWM avec un rapport cyclique nul (LED éteinte au départ)
for pwm in led_pwm:
    pwm.start(0)

# Réglage de l'intensité lumineuse de chaque composante RGB
led_pwm[0].ChangeDutyCycle(37)  # Rouge à 50 %
led_pwm[1].ChangeDutyCycle(95)  # Vert à 75 %
led_pwm[2].ChangeDutyCycle(56)  # Bleu à 25 %
time.sleep(10)
# Pour éteindre la LED RGB, mettez le rapport cyclique de toutes les broches à 0 %
for pwm in led_pwm:
    pwm.ChangeDutyCycle(0)

# Nettoyage des broches GPIO
GPIO.cleanup()

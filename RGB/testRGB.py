import RPi.GPIO as GPIO
import time

# Configuration des broches pour le contr�le PWM
GPIO.setmode(GPIO.BCM)  # Utilisation de la num�rotation des broches BCM
led_pins = [17, 27, 22]  # Remplacez ces valeurs par les broches que vous utilis
ez

# Configuration des broches en mode PWM
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Cr�ation d'objets PWM pour chaque composante RGB
led_pwm = [GPIO.PWM(pin, 100) for pin in led_pins]

# D�marrage des signaux PWM avec un rapport cyclique nul (LED �teinte au d�part)
for pwm in led_pwm:
    pwm.start(0)

# R�glage de l'intensit� lumineuse de chaque composante RGB
led_pwm[0].ChangeDutyCycle(100)  # Rouge � 50 %
led_pwm[1].ChangeDutyCycle(0)  # Vert � 75 %
led_pwm[2].ChangeDutyCycle(100)  # Bleu � 25 %
time.sleep(1)
# Pour �teindre la LED RGB, mettez le rapport cyclique de toutes les broches � 0
 %
for pwm in led_pwm:
    pwm.ChangeDutyCycle(0)

# Nettoyage des broches GPIO
GPIO.cleanup()
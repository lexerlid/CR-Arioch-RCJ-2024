import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

in1_uno = 20
in2_uno = 21
in1_dos = 26
in2_dos = 24
in1_tres = 19
in2_tres = 16
in1_cuatro = 13
in2_cuatro = 12

ena = 25
enb = 27
enc = 6
end = 5

GPIO.setup(in1_uno, GPIO.OUT)
GPIO.setup(in2_uno, GPIO.OUT)
GPIO.setup(in1_dos, GPIO.OUT)
GPIO.setup(in2_dos, GPIO.OUT)
GPIO.setup(in1_tres, GPIO.OUT)
GPIO.setup(in2_tres, GPIO.OUT)
GPIO.setup(in1_cuatro, GPIO.OUT)
GPIO.setup(in2_cuatro, GPIO.OUT)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
GPIO.setup(enc, GPIO.OUT)
GPIO.setup(end, GPIO.OUT)

enable_a = GPIO.PWM(ena, 50)
enable_b = GPIO.PWM(enb, 50)
enable_c = GPIO.PWM(enc, 50)
enable_d = GPIO.PWM(end, 50)

enable_a.start(0)
enable_b.start(0)
enable_c.start(0)
enable_d.start(0)

def direction(w1, w2, w3, w4):
    if w1 > 0:
        GPIO.output(in1_uno, GPIO.HIGH)
        GPIO.output(in2_uno, GPIO.LOW)
    else:
        GPIO.output(in1_uno, GPIO.LOW)
        GPIO.output(in2_uno, GPIO.HIGH)
    if w2 > 0:
        GPIO.output(in1_dos, GPIO.HIGH)
        GPIO.output(in2_dos, GPIO.LOW)
    else:
        GPIO.output(in1_dos, GPIO.LOW)
        GPIO.output(in2_dos, GPIO.HIGH)
    if w3 > 0:
        GPIO.output(in1_tres, GPIO.HIGH)
        GPIO.output(in2_tres, GPIO.LOW)
    else:
        GPIO.output(in1_tres, GPIO.LOW)
        GPIO.output(in2_tres, GPIO.HIGH)
    if w4 > 0:
        GPIO.output(in1_cuatro, GPIO.HIGH)
        GPIO.output(in2_cuatro, GPIO.LOW)
    else:
        GPIO.output(in1_cuatro, GPIO.LOW)
        GPIO.output(in2_cuatro, GPIO.HIGH)

def interrupcion(ldr,v1, v2, v3, v4):
    if ldr == "derecha":
        print("inter, derecha")
        direction(v1, v2, v3, v4)
        enable_a.ChangeDutyCycle(v1)
        enable_b.ChangeDutyCycle(v2)
        enable_c.ChangeDutyCycle(v3)
        enable_d.ChangeDutyCycle(v4)
    elif ldr == "izquierda":
        print("inter, izquierda")
        direction(v1, v2, v3, v4)
        enable_a.ChangeDutyCycle(v1)
        enable_b.ChangeDutyCycle(v2)
        enable_c.ChangeDutyCycle(v3)
        enable_d.ChangeDutyCycle(v4)
    elif ldr == "atras":
        print("inter, atras")
        direction(v1, v2, v3, v4)
        enable_a.ChangeDutyCycle(v1)
        enable_b.ChangeDutyCycle(v2)
        enable_c.ChangeDutyCycle(v3)
        enable_d.ChangeDutyCycle(v4)
    elif ldr == "adelante":
        print("inter, adelante")
        direction(v1, v2, v3, v4)
        enable_a.ChangeDutyCycle(v1)
        enable_b.ChangeDutyCycle(v2)
        enable_c.ChangeDutyCycle(v3)
        enable_d.ChangeDutyCycle(v4)

def stop():
    print("Stopping")
    GPIO.output(in1_uno, GPIO.LOW)
    GPIO.output(in2_uno, GPIO.LOW)
    GPIO.output(in1_dos, GPIO.LOW)
    GPIO.output(in2_dos, GPIO.LOW)
    GPIO.output(in1_tres, GPIO.LOW)
    GPIO.output(in2_tres, GPIO.LOW)
    GPIO.output(in1_cuatro, GPIO.LOW)
    GPIO.output(in2_cuatro, GPIO.LOW)
    
    enable_a.ChangeDutyCycle(0)
    enable_b.ChangeDutyCycle(0)
    enable_c.ChangeDutyCycle(0)
    enable_d.ChangeDutyCycle(0)

    enable_a.stop()
    enable_b.stop()
    enable_c.stop()
    enable_d.stop()

    GPIO.cleanup()

def move(interrupt,ldr,v1, v2, v3, v4):
    try:
        direction(v1, v2, v3, v4)
        enable_a.ChangeDutyCycle(v1)
        enable_b.ChangeDutyCycle(v2)
        enable_c.ChangeDutyCycle(v3)
        enable_d.ChangeDutyCycle(v4)
    except interrupt == "interrupcion":
        print("Interrupt")
        interrupcion(ldr,v1, v2, v3, v4)

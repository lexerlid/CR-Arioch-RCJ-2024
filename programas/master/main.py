import vectores as vc
import decisionOfMove as d_m
import comunicacion as serial

def decision (ir):
    if ir == 1:
        deg = 
    elif ir == 2:
        deg =
    elif ir == 3:
        deg =
    elif ir == 4:
        deg =
    elif ir == 5:
        deg =
    elif ir == 6:
        deg =
    elif ir == 7:
        deg =
    elif ir == 8:
        deg =
    elif ir == 9:
        deg =
    elif ir == 10:
        deg =
    elif ir == 11:
        deg =
    elif ir == 12:
        deg =
    elif ir == 13:
        deg =
    elif ir == 14:
        deg =
    
    return deg 

try:
    while True:
        vW1, vW2, vW3, vW4 = vc.Velocity_wheels(int(input("Ingrese un ángulo en grados: ")))
        interrupt = int(input("si hay interrupcion pon -interrupcion-: "))
        ldr = int(input("cual interrupcion : "))
        ir = int(input("cual ir: "))

        d_m.move(interrupt,ldr,vW1, vW2, vW3, vW4)
        
except KeyboardInterrupt:
    d_m.stop()
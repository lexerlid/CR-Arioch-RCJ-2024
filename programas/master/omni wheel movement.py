import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#var
fig, ax = plt.subplots()

x_center = 0
y_center = 0
#whit the robot size
radius = 8.7*10

L = float(0.0865)
V = float(1.17825)

circle = Circle((x_center, y_center), radius, fill=True, color='lavender')

while True:
    deg = int(input("Ingrese un ángulo en grados: "))  # Corrección en la solicitud de entrada
    theta = math.radians(deg)
    W = float(theta/7.5)
    #formula de cosenos
    Vw_1a = V*math.cos(theta+math.pi/4)-W*L
    Vw_2a = V*math.cos(theta+math.pi/4)-W*L
    Vw_3a = V*math.cos(theta+3*math.pi/4)-W*L
    Vw_4a = V*math.cos(theta+3*math.pi/4)-W*L
    
    VW_1ab = -(Vw_1a*100)#deg=135
    VW_2ab = -(Vw_2a*100)#deg=135
    VW_3ab = -(Vw_3a*100)#deg=45
    VW_4ab = -(Vw_4a*100)#deg=45
    
    print("formula con cos",VW_1ab, VW_2ab, VW_3ab, VW_4ab)

    #componentes rectangulares
    xw_1 = [VW_1ab * math.cos(math.radians(135))]
    yw_1 = [VW_1ab * math.sin(math.radians(135))]

    xw_2 = [VW_2ab * math.cos(math.radians(135))]
    yw_2 = [VW_2ab * math.sin(math.radians(135))]

    xw_3 = [VW_3ab * math.cos(math.radians(45))]
    yw_3 = [VW_3ab * math.sin(math.radians(45))]

    xw_4 = [VW_4ab * math.cos(math.radians(45))]
    yw_4 = [VW_4ab * math.sin(math.radians(45))]

    print(xw_1, yw_1, xw_2, yw_2, xw_3, yw_3, xw_4, yw_4)
    
    xw_5 = sum(xw_1 + xw_2 + xw_3 + xw_4)
    yw_5 = sum(yw_1 + yw_2 + yw_3 + yw_4)
    
    x_i1 = 0 + (6.1165*10) 
    y_i1 = 0 + (6.1165*10)
    x_f1 = xw_1
    y_f1 = yw_1
    
    x_i2 = 0 - (6.1165*10)
    y_i2 = 0 - (6.1165*10)
    x_f2 = xw_2
    y_f2 = yw_2
    
    x_i3 = 0 - (6.1165*10)
    y_i3 = 0 + (6.1165*10) 
    x_f3 = xw_3
    y_f3 = yw_3
    
    x_i4 = 0 + (6.1165*10)
    y_i4 = 0 - (6.1165*10)
    x_f4 = xw_4
    y_f4 = yw_4
    
    x_i5 = 0
    y_i5 = 0
    x_f5 = xw_5  
    y_f5 = yw_5  
    
    ax.clear()
    ax.add_patch(circle)
    
    W_1 = round(VW_1ab,5)
    W_2 = round(VW_2ab,5)
    W_3 = round(VW_3ab,5)
    W_4 = round(VW_4ab,5)
    
    plt.quiver(x_i1,y_i1,x_f1,y_f1, scale_units='xy', angles='xy',scale=1, color='b')
    plt.text(x_i1, y_i1, str(W_1), fontsize=10, color='b', horizontalalignment='left')
    plt.quiver(x_i2,y_i2,x_f2,y_f2, scale_units='xy', angles='xy',scale=1, color='c')
    plt.text(x_i2-20, y_i2, str(W_2), fontsize=10, color='c', horizontalalignment='right')
    plt.quiver(x_i3,y_i3,x_f3,y_f3, scale_units='xy', angles='xy',scale=1, color='r')
    plt.text(x_i3, y_i3, str(W_3), fontsize=10, color='r', horizontalalignment='right')
    plt.quiver(x_i4,y_i4,x_f4,y_f4, scale_units='xy', angles='xy',scale=1, color='m')
    plt.text(x_i4+20, y_i4, str(W_4), fontsize=10, color='m', horizontalalignment='left')
    
    plt.quiver(x_i5, y_i5, x_f5, y_f5, scale_units='xy', angles='xy', scale=1, color='grey')
    
    plt.xlim(-300,300)
    plt.ylim(-300,300)
    #guias
    plt.axvline(x=0)
    plt.axhline(y=0)

    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.grid()
    
    plt.xlabel("cordenada X")
    plt.ylabel("cordenada Y")
    plt.title("Movimiento robot - velocidades de ruedas")
    
    plt.pause(.1)


plt.show()
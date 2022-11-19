
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as mt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Rot(axis,angle):
    if axis=='x':
        matrix=np.mat([[round(1,3),round(0,3),round(0,3),round(0,3)],
                       [round(0,3),round(mt.cos(mt.radians(angle)),3),round(-mt.sin(mt.radians(angle)),3),round(0,3)],
                       [round(0,3),round(mt.sin(mt.radians(angle)),3),round(mt.cos(mt.radians(angle)),3),round(0,3)],
                       [round(0,3),round(0,3),round(0,3),round(1,3)]])

    else:
        if axis=='y':
            matrix=np.mat([[round(mt.cos(mt.radians(angle)),3),round(0,3),round(mt.sin(mt.radians(angle)),3),round(0,3)],
                           [round(0,3),round(1,3),round(0,3),round(0,3)],
                           [round(-mt.sin(mt.radians(angle)),3),round(0,3),round(mt.cos(mt.radians(angle)),3),round(0,3)],
                           [round(0,3),round(0,3),round(0,3),round(1,3)]])

        else:
            if axis=='z':
                matrix=np.mat([[round(mt.cos(mt.radians(angle)),3),round(-mt.sin(mt.radians(angle)),3),round(0,3),round(0,3)],
                               [round(mt.sin(mt.radians(angle)),3),round(mt.cos(mt.radians(angle)),3),round(0,3),round(0,3)],
                               [round(0,3),round(0,3),round(1,3),round(0,3)],
                               [round(0,3),round(0,3),round(0,3),round(1,3)]])
                
    return matrix

def Trans(axis,distance):
    if axis == 'x':
        matrix = np.mat([[round(1,3),round(0,3),round(0,3),round(distance,3)],
                         [round(0,3),round(1,3),round(0,3),round(0,3)],
                         [round(0,3),round(0,3),round(1,3),round(0,3)],
                         [round(0,3),round(0,3),round(0,3),round(1,3)]])
        
    else:
        if axis == 'y':
            matrix = np.mat([[round(1,3),round(0,3),round(0,3),round(0,3)],
                             [round(0,3),round(1,3),round(0,3),round(distance,3)],
                             [round(0,3),round(0,3),round(1,3),round(0,3)],
                             [round(0,3),round(0,3),round(0,3),round(1,3)]])

        else:
            if axis == 'z':
                matrix = np.mat([[round(1,3),round(0,3),round(0,3),round(0,3)],
                                 [round(0,3),round(1,3),round(0,3),round(0,3)],
                                 [round(0,3),round(0,3),round(1,3),round(distance,3)],
                                 [round(0,3),round(0,3),round(0,3),round(1,3)]])

    return matrix
 
plt.subplot(projection='3d')

def draw(result):
    x=result.getA()[0][3]
    y=result.getA()[1][3]
    z=result.getA()[2][3]
    list = [x,y,z]
    return list
def main():

    print("记得要写乘号")
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    plt.clabel('z轴')
    plt.title('机械臂三维图')
    getcmd = input("输入运动学式子：")
    while(getcmd!='0'):
        yuandian = [0.0,0.0,0.0]
        result = eval(getcmd)
        print(result)
        weizhi=draw(result)
        plt.plot(weizhi,yuandian,marker='+',color='coral')
        plt.plot(weizhi,yuandian,linewidth=1, color='red')
        plt.show()
        getcmd = input("输入运动学式子：")

if __name__ == '__main__':
    main()

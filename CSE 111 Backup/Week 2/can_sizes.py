# 04 Team Activity: Writing Functions

"""
In many countries, food is stored in steel cans 
(also known as tin cans) that are shaped like cylinders. 
There are many different sizes of steel cans. 
The storage efficiency of a can tells us how much a can stores 
versus how much steel is required to make the can. 
Some sizes of cans require a lot of steel to store a small amount of food. 
Other sizes of cans require less steel and store more food. 
A can size with a large storage efficiency is considered 
more friendly to the environment than a can size with a small storage efficiency.

The storage efficiency of a steel can is computed 
by dividing the volume of a can by its surface area.

storage_efficiency = volume/surface_area
In other words, the storage efficiency of a can 
is the space inside the can divided by the amount of steel required to make the can. 
The formulas for the volume and surface area of a cylinder are:
volume = π*radius**2*height
surface_area = 2π*radius*(radius + height)
π is the constant PI, the ratio of the circumference of a circle 
divided by its diameter (use math.pi)
radius is the radius of the cylinder
height is the height of the cylinder

Core Requirements¶
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
Name	Radius(cm)	Height (cm)	Cost per Can (U.S. dollars)
#1 Picnic	6.83	10.16	$0.28
#1 Tall	7.78	11.91	$0.43
#2	8.73	11.59	$0.45
#2.5	10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	13.02	14.29	$0.83
#6Z	5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	15.72	17.78	$1.53
#211	6.83	12.38	$0.34
#300	7.62	11.27	$0.38
#303	8.10	11.11	$0.42
"""
from cmath import pi
import math


def main ():
    can_name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3",
        "#5", "#6Z", "#8Z short", "#10", "#211", "#300","#303"]

    can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1]

    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26,
        1.53, 0.34, 0.38, 0.42]
    for i in range(len(can_name)):
        name = can_name[i]
        radius = can_radius[i]
        height = can_height[i]
        cost = can_cost[i]
        print(f"{name} {compute_storage_efficiency(radius, height):.2f}",
        f"{compute_cost_efficiency(cost,radius,height):.2f}")


def compute_volume (radius, height):
    return pi * radius**2 * height

def compute_surface_area (radius, height):
    return 2 * pi * radius * (radius + height)

def compute_storage_efficiency (radius, height):
    return compute_volume(radius,height)/compute_surface_area(radius, height)


main()
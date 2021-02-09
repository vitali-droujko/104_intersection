##
## EPITECH PROJECT, 2021
## 104intersection (Workspace)
## File description:
## msg_print
##

from sys import exit, argv
from math import pi

def error_handling(n):
    if n == 84 or len(argv) != 4:
        print("USAGE")
        print("    Usage: ./104intersection opt xp yp zp xv yv zv p")
        print("DESCRIPTION")
        print("    opt             surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
        print("    (xp, yp, zp)    coordinates of a point by which the light ray passes through")
        print("    (xv, yv, zv)    coordinates of a vector parallel to the light ray")
        print("    p               parameter: radius of the sphere, radius of the cylinder, or")
        print("                    angle formed by the cone and the Z-axis")
        exit(84)
    return

def printer(opt, coords, p, racine):
    if (opt == 1):
        print("Sphere of radius %d" % (p))
    elif (opt == 2):
        print("Cylinder of radius %d" % (p))
    else:
        print("Cone with a %d degree angle" % (p))
    print("Line passing through the point (%d, %d, %d) "    \
        % (coords[0][0], coords[0][1], coords[0][2]), end="")
    print("and parallel to the vector (%d, %d, %d)"         \
                % (coords[1][0], coords[1][1], coords[1][2]))
    if racine[0][0] == pi:
        print("There is an infinite number of intersection points.")
    elif racine[0][0] > 0:
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)" % (racine[1][0], racine[1][1], racine[1][2]))
        print("(%.3f, %.3f, %.3f)" % (racine[2][0], racine[2][1], racine[2][2]))
    elif racine[0][0] == 0:
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)" % (racine[1][0], racine[1][1], racine[1][2]))
    else:
        print("No intersection point.")
    return

from math import cos, pi
from ti_system import disp_clr
from menu_sys import *


def RA():
    print("Sketch situation. Create a list of kinematic variables beginning with what you are asked for and what is given. Solve")


def v_t():
    disp_clr()
    print("avg_v_t = 2pi*r/T, where T is the time for a full rotation.")
    print("v_t = r*w, where w is the angular velocity.")

    
def a_c():
    disp_clr()
    print("a_c = v_t^2/r, where a_c is centripital acceleration.")


def s():
    disp_clr()
    print("s=change(radians)*r")
    print("s=rad*r")


def a_t():
    disp_clr()
    print("a_t=r*a_a")


def rot_keni():
    disp_clr()
    # Initializing all variables as None
    w_i = input("w_i (angular velocity): ")
    w_f = input("w_f (angular velocity): ")
    a = input("a (angular acceleration): ")
    t = input("t: ")
    rad = input("rad: ")

    # Convert input values to float or set to None if left blank
    w_i = float(w_i) if w_i != '' else None
    w_f = float(w_f) if w_f != '' else None
    a = float(a) if a != '' else None
    t = float(t) if t != '' else None
    rad = float(rad) if rad != '' else None

    # Equation 1: w_i = w_f + a * t
    if w_i is None and w_f is not None and a is not None and t is not None:
        w_i = w_f + a * t
        print("Initial angular velocity (w_i) = " + str(w_i))

    if w_f is None and w_i is not None and a is not None and t is not None:
        w_f = w_i + a * t
        print("Final angular velocity (w_f) = " + str(w_f))

    # Equation 2: rad = w_i * t + 0.5 * a * t^2
    if rad is None and w_i is not None and a is not None and t is not None:
        rad = w_i * t + 0.5 * a * t ** 2
        print("Angular displacement (rad) = " + str(rad))

    if t is None and w_i is not None and rad is not None and a is not None:
        # Corrected discriminant calculation for quadratic equation
        discriminant = (w_i ** 2) + (2 * a * rad)
        if discriminant >= 0:
            t1 = (-w_i + discriminant**0.5) / a
            t2 = (-w_i - discriminant**0.5) / a
            if t1 >= 0 and t2 >= 0:
                print("Two possible solutions for time (t): " + str(t1) + " and " + str(t2))
            elif t1 >= 0:
                print("Time (t) = " + str(t1))
            elif t2 >= 0:
                print("Time (t) = " + str(t2))
            else:
                print("No valid solution for time (t).")

    # Equation 3: w_f^2 = w_i^2 + 2 * a * rad
    if w_f is None and w_i is not None and a is not None and rad is not None:
        w_f = (w_i ** 2 + 2 * a * rad) ** 0.5
        print("Final angular velocity (w_f) = " + str(w_f))

    if a is None and w_f is not None and w_i is not None and rad is not None:
        a = (w_f ** 2 - w_i ** 2) / (2 * rad)
        print("Angular acceleration (a) = " + str(a))

    # Equation 4: rad = (w_f + w_i) / 2 * t
    if rad is None and w_f is not None and w_i is not None and t is not None:
        rad = ((w_f + w_i) / 2) * t
        print("Angular displacement (rad) = " + str(rad))

    if t is None and w_f is not None and w_i is not None and rad is not None:
        t = (2 * rad) / (w_f + w_i)
        print("Time (t) = " + str(t))

    if w_i is None or w_f is None or a is None or t is None or rad is None:
        print("Not enough information to solve all variables.")


menu_structure = {
    "Main Menu": {
        "title": "Energy Approach",
        "options": {
            "Reasoning Strategy": RA,
            "Avg Tang Veloc": v_t,
            "Centrip Accel": a_c,
            "Arc Length": s,
            "Tang Accel": a_t,
            "Centrip Accel": a_c,
            "Kenimatics": rot_keni
        }
    },
}   


menu_system = Menu_System(menu_structure)
menu_system.run()

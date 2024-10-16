from ti_system import *
from math import *
from menu_sys import *


def force_RA():
    disp_clr()
    print("Graph forces. Solve for missing")


def force():
    disp_clr()
    f = input("F: ")
    m = input("m: ")
    a = input("a: ")

    try:
        # Convert inputs to float or None
        f = float(f) if f else None
        m = float(m) if m else None
        a = float(a) if a else None

        if f is None and m is not None and a is not None:
            f = m * a
            print("Force (F) = " + str(f) + " N")
        elif m is None and f is not None and a is not None:
            m = f / a
            print("Mass (m) = " + str(m) + " kg")
        elif a is None and f is not None and m is not None:
            a = f / m
            print("Acceleration (a) = " + str(a) + " m/s²")
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def F_g():
    disp_clr()
    G = 6.67430e-11  # Gravitational constant
    m1 = input("m1: ")
    m2 = input("m2: ")
    r = input("r: ")
    f_g = input("F_g: ")

    try:
        # Convert inputs to float or None
        m1 = float(m1) if m1 else None
        m2 = float(m2) if m2 else None
        r = float(r) if r else None
        f_g = float(f_g) if f_g else None

        if f_g is None:
            f_g = G * (m1 * m2) / r ** 2
            print("Gravitational Force (F_g) = " + str(f_g) + " N")
        elif m1 is None:
            m1 = (f_g * r ** 2) / (G * m2)
            print("Mass of first object (m1) = " + str(m1) + " kg")
        elif m2 is None:
            m2 = (f_g * r ** 2) / (G * m1)
            print("Mass of second object (m2) = " + str(m2) + " kg")
        elif r is None:
            r = ((f_g * m1 * m2)/G)**0.5
            print("Distance between the centers of the objects (r) = " + str(r) + " m")
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def F_w(): #### continue here
    disp_clr()
    mass = input("m: ")
    g = 9.8  # Acceleration due to gravity

    try:
        mass = float(mass) if mass else None
        if mass is not None:
            F_w = mass * g
            print("Weight (F_w) = " + str(F_w) + " N")
        elif mass is None:
            pass
        else:
            print("Mass (m) must be provided to calculate weight.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def F_s():
    disp_clr()
    mu_s = input("Enter coefficient of static friction (μ_s): ")
    F_n = input("Enter normal force (F_n) or leave blank if unknown: ")

    try:
        mu_s = float(mu_s)
        F_n = float(F_n) if F_n else None
        if F_n is None:
            print("Normal force (F_n) must be provided to calculate static friction force.")
        else:
            F_s = mu_s * F_n
            print("Static Friction Force (F_s) = " + str(F_s) + " N")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def F_k():
    disp_clr()
    mu_k = input("Enter coefficient of kinetic friction (μ_k): ")
    F_n = input("Enter normal force (F_n) or leave blank if unknown: ")

    try:
        mu_k = float(mu_k)
        F_n = float(F_n) if F_n else None
        if F_n is None:
            print("Normal force (F_n) must be provided to calculate kinetic friction force.")
        else:
            F_k = mu_k * F_n
            print("Kinetic Friction Force (F_k) = " + str(F_k) + " N")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")




menu_structure = {
    "Main Menu": {
        "title": "Force Approach",
        "options": {
            "Reasoning Strategy": force_RA,
            "Force": force,
            "Grav Attraction Force": F_g,
            "Weight": F_w,
            "Static Friction Force": F_s,
            "Kinetic Friction Force": F_k
        }
    },
}   


menu_system = Menu_System(menu_structure)
menu_system.run()


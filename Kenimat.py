from ti_system import *
from math import *
from menu_sys import *

def kenimatics_RA():
    disp_clr()
    print("""
        Sketch situation
        Create a list of kinematic variables beginning with what you are asked for and what is given. Make a separate list for each dimension.
        Solve
    """)


def kenimat():
    disp_clr()
    # Initializing all variables as None
    v0 = input("v_i: ")
    v = input("v_f: ")
    a = input("a: ")
    t = input("t: ")
    x = input("x: ")

    # Convert input values to float or set to None if left blank
    v0 = float(v0) if v0 != '' else None
    v = float(v) if v != '' else None
    a = float(a) if a != '' else None
    t = float(t) if t != '' else None
    x = float(x) if x != '' else None

    # Equation 1: v = v0 + a * t
    if v is None and v0 is not None and a is not None and t is not None:
        v = v0 + a * t
        print("Final velocity (v) = " + str(v) + " m/s")

    if v0 is None and v is not None and a is not None and t is not None:
        v0 = v - a * t
        print("Initial velocity (v0) = " + str(v0) + " m/s")

    # Equation 2: x = v0 * t + 0.5 * a * t^2
    if x is None and v0 is not None and a is not None and t is not None:
        x = v0 * t + 0.5 * a * t ** 2
        print("Displacement (x) = " + str(x) + " m")

    if t is None and v0 is not None and x is not None and a is not None:
        # Corrected discriminant calculation for quadratic equation
        discriminant = (v0 ** 2) + (2 * a * x)
        if discriminant >= 0:
            t1 = (-v0 + discriminant**0.5) / a
            t2 = (-v0 - discriminant**0.5) / a
            if t1 >= 0 and t2 >= 0:
                print("Two possible solutions for time (t): " + str(t1) + " s and " + str(t2) + " s")
            elif t1 >= 0:
                print("Time (t) = " + str(t1) + " s")
            elif t2 >= 0:
                print("Time (t) = " + str(t2) + " s")
            else:
                print("No valid solution for time (t).")

    # Equation 3: v^2 = v0^2 + 2 * a * x
    if v is None and v0 is not None and a is not None and x is not None:
        v = (v0 ** 2 + 2 * a * x) ** 0.5
        print("Final velocity (v) = " + str(v) + " m/s")

    if a is None and v is not None and v0 is not None and x is not None:
        a = (v ** 2 - v0 ** 2) / (2 * x)
        print("Acceleration (a) = " + str(a) + " m/s²")

    # Equation 4: x = (v + v0) / 2 * t
    if x is None and v is not None and v0 is not None and t is not None:
        x = ((v + v0) / 2) * t
        print("Displacement (x) = " + str(x) + " m")

    if t is None and v is not None and v0 is not None and x is not None:
        t = (2 * x) / (v + v0)
        print("Time (t) = " + str(t) + " s")

    if v0 is None or v is None or a is None or t is None or x is None:
        print("Not enough information to solve all variables.")



menu_structure = {
    "Main Menu": {
        "title": "Kenimatics",
        "options": {
            "Reasoning Strategy": kenimatics_RA,
            "Kenimatics": kenimat,
        }
    }
}   


menu_system = Menu_System(menu_structure)
menu_system.run()

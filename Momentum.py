from math import *
from ti_system import *
from menu_sys import *


def momentum_RA():
    print("If potential energy NOT exists then use W=E_k. Else if there is any work done by nonconservative forces then use W=sum(E) (Nonconservative work-energy theorem). Else use E_f=E_i (Law of conservation of mechanical energy)")


def momentum_RA():
    disp_clr()
    print("""If net external force NOT zero, use I-M Theroem. Else, use Conserv of Lin M. Identify type of collision. If completely inelastic apply Conserv of Lin M. Else if elastic apply Conserv Of E_k in addition to  Conserv of Lin M. Solve""")


def I():
    disp_clr()
    print("Impulse: I = F * T")
    print("Impulse: mv_f - mv_i")
    F = input("Force (F): ")
    T = input("Time (T): ")
    m = input("Mass (m): ")
    v_i = input("Initial velocity (v_i): ")
    v_f = input("Final velocity (v_f): ")
    I = input("Impulse (I): ")

    try:
        F = float(F) if F else None
        T = float(T) if T else None
        m = float(m) if m else None
        v_i = float(v_i) if v_i else None
        v_f = float(v_f) if v_f else None
        I = float(I) if I else None

        if I is None:
            if F is not None and T is not None:
                I = F * T  # Calculate impulse using I = F * T
            elif m is not None and v_i is not None and v_f is not None:
                I = m * (v_f - v_i)  # Calculate impulse using I = m(v_f - v_i)
            print("Impulse (I) = " + str(I) + " Ns")
        elif F is None and T is not None:
            F = I / T  # Calculate force
            print("Force (F) = " + str(F) + " N")
        elif T is None and F is not None:
            T = I / F  # Calculate time
            print("Time (T) = " + str(T) + " s")
        elif v_f is None and m is not None and v_i is not None:
            v_f = (I / m) + v_i  # Calculate final velocity
            print("Final velocity (v_f) = " + str(v_f) + " m/s")
        elif v_i is None and m is not None and v_f is not None:
            v_i = v_f - (I / m)  # Calculate initial velocity
            print("Initial velocity (v_i) = " + str(v_i) + " m/s")
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def M_l():
    disp_clr()
    print("Linear Momentum: p = mv")
    m = input("Mass (m): ")
    v = input("Velocity (v): ")
    p = input("Momentum (p): ")

    try:
        m = float(m) if m else None
        v = float(v) if v else None
        p = float(p) if p else None

        if p is None:
            p = m * v  # Calculate linear momentum
            print("Linear Momentum (p) = " + str(p) + " kg*m/s")
        elif m is None:
            m = p / v  # Calculate mass
            print("Mass (m) = " + str(m) + " kg")
        elif v is None:
            v = p / m  # Calculate velocity
            print("Velocity (v) = " + str(v) + " m/s")
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def M_im():
    print("Impulse-Momentum Theorem: sum(I) = p_f - p_i")


def M_cl():
    print("Law of conservation of linear momentum: sum(p_f) = sum(p_i)")
    print("Note: you may need to also solve for E_kf = E_ki if there are two unknowns in the conservation of linear momentum equation, which gives you a system of equations.")


menu_structure = {
    "Main Menu": {
        "title": "Momentum Approach",
        "options": {
            "Reasoning Strategy": momentum_RA,
            "Impulse": I,
            "Linear Momentum": M_l,
            "Impulse-Momentum Theorem": M_im,
            "Conservation of Linear Momentum": M_cl
        }
    },
}   


menu_system = Menu_System(menu_structure)
menu_system.run()

from math import cos, pi
from ti_system import disp_clr
from menu_sys import *


def energy_RA():
    print("If potential energy NOT exists then use W=E_k. Else if there is any work done by nonconservative forces then use W=sum(E) (Nonconservative work-energy theorem). Else use E_f=E_i (Law of conservation of mechanical energy)")


def work():
    disp_clr()
    print("W=F*d*cos(theta)")
    F = input("F: ")
    d = input("d: ")
    theta = input("theta: ")
    W = input("W: ")

    try:
        F = float(F) if F else None
        d = float(d) if d else None
        theta = float(theta) if theta else None
        W = float(W) if W else None

        if F is None:
            F = W / (d * cos(theta * 3.14159 / 180))  # Calculate F
            print("Force (F) = " + str(F))
        elif d is None:
            d = W / (F * cos(theta * 3.14159 / 180))  # Calculate d
            print("Distance (d) = " + str(d))
        elif W is None:
            W = F * d * cos(theta * pi / 180)  # Calculate W
            print("Work Done (W) = " + str(W))
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def E_k():
    disp_clr()
    print("E_k = (1/2) * m * v^2")
    m = input("m: ")
    v = input("v: ")
    E_k = input("E_k: ")

    try:
        m = float(m) if m else None
        v = float(v) if v else None
        E_k = float(E_k) if E_k else None

        if E_k is None:
            E_k = 0.5 * m * v**2  # Calculate E_k
            print("Kinetic Energy (E_k) = " + str(E_k))
        elif m is None:
            m = (2 * E_k) / (v**2)  # Calculate m
            print("Mass (m) = " + str(m))
        elif v is None:
            v = (2 * E_k / m)**0.5  # Calculate v
            print("Velocity (v) = " + str(v))
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def E_g():
    disp_clr()
    print("E_g = m * g * h")
    m = input("m: ")
    g = input("g: ")
    h = input("h: ")
    E_g = input("E_g: ")

    try:
        m = float(m) if m else None
        g = float(g) if g else None
        h = float(h) if h else None
        E_g = float(E_g) if E_g else None

        if E_g is None:
            E_g = m * g * h  # Calculate E_g
            print("Gravitational Potential Energy (E_g) = " + str(E_g))
        elif m is None:
            m = E_g / (g * h)  # Calculate m
            print("Mass (m) = " + str(m))
        elif g is None:
            g = E_g / (m * h)  # Calculate g
            print("Acceleration due to gravity (g) = " + str(g))
        elif h is None:
            h = E_g / (m * g)  # Calculate h
            print("Height (h) = " + str(h))
        else:
            print("Insufficient information to solve for any variable.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


def E_wk():
    disp_clr()
    print("The work-kinetic energy theorem:")
    print("Work = change in kinetic energy")
    print("W = 0.5 * m * v_f^2 - 0.5 * m * v_i^2")


def E_nc():
    disp_clr()
    print("The Nonconservative Work-Energy Theorem: W_nc = ΔE")
    print("W_nc = change in the sum of all the energies.")


def E_mc():
    disp_clr()
    print("Conservation of mechanical energy:")
    print("E_gf + E_kf = E_gi + E_ki")
    print("m*g*h_f + 0.5*m*v_f^2 = m*g*h_i + 0.5*m*v_i^2")


menu_structure = {
    "Main Menu": {
        "title": "Energy Approach",
        "options": {
            "Reasoning Strategy": energy_RA,
            "Work": work,
            "Kinetic Energy": E_k,
            "Grav Poten Energy": E_g,
            "THE W-E_k Theorem": E_wk,
            "THE W_nc-E Theorem": E_nc,
            "Conserv Mech E": E_mc
        }
    },
}   


menu_system = Menu_System(menu_structure)
menu_system.run()

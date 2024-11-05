from math import cos, pi
from ti_system import disp_clr
from menu_sys import *


def RA():
    disp_clr()
    print("Draw sketch. After selecting a convenient axis of rotation, determine torques with respect to that axis. Algebraically add torques and equate to: I*a_a if there is angular acceleration or zero if there is rotational equilibrium. Solve.")


def t():
    disp_clr()
    print("sum(t) = I*a_a")
    print("NET external torque = moment of inertia * angular acceleration")
    print("t = F*l = F*r*sin(theta)")
    print("torque = force * lever arm")


def T():
    disp_clr()
    print("T^2 = (4*pi^2*r^3)/(G*M_e) where T is the time to rotate an object once.")


def E_r():
    disp_clr()
    print("E_r = (1/2) * I * w^2")
    print("Rotational Kinetic Energy = (0.5) * Moment of Inertia * angular velocity^2")


def M_a():
    disp_clr()
    print("L = I * w")
    print("Angular Momentum = Moment of Inertia * angular velocity")


def conserv_ang_M():
    disp_clr()
    print("Law of conservation of angular momentum: L_f = L_i")


menu_structure = {
    "Main Menu": {
        "title": "Energy Approach",
        "options": {
            "Reasoning Strategy": RA,
            "Torque": t,
            "Orbital Period": T,
            "Moment of Inertia": {
                "title": "Moment of Inertia",
                "options": {
                    "Hoop or thin cylindrical shell": lambda: print("I = m*r^2"),
                    "Solid cylinder or disk": lambda: print("I = (1/2)*m*r^2"),
                    "Solid sphere": lambda: print("I = (2/5)*m*r^2"),
                    "Hollow sphere": lambda: print("I = (2/3)*m*r^2"),
                    "Long, thin rod with rotation axis at center": lambda: print("I = (1/12)*m*L^2"),
                    "Long, thin rod with rotation axis at end": lambda: print("I = (1/3)*m*L^2"),
                }
            },
            "Rotational Kinetic Energy": E_r,
            "Angular Momentum": M_a,
            "Conservation of Angular Momentum": conserv_ang_M
        }
    },
}   


menu_system = Menu_System(menu_structure)
menu_system.run()

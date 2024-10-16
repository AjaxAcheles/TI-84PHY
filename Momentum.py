from math import *
from ti_system import *
from menu_sys import *


def momentum_RA():
    print("If potential energy exists then use W=E_k")
    print("else if there is any work done by nonconservative forces then use W=sum(E) (Nonconservative work-energy theorem)")
    print("else use E_f=E_i (Law of conservation of mechanical energy)")


def momentum_RA():
    disp_clr()
    print("""If net external force NOT zero, use I-M Theroem. Else, use Conserv of Lin M. Identify type of collision. If completely inelastic apply Conserv of Lin M. Else if elastic apply Conserv Of E_k in addition to  Conserv of Lin M. Solve""")


def I():
    print("Impulse: I = F * T")
    print("Impulse: mv_f - mv_i")


def M_l():
    print("Linear Momentum: p = mv")


def M_im():
    print("Impulse-Momentum Theorem: sum(I) = p_f - p_i")


def M_cl():
    print("Law of conservation of linear momentum: sum(p_f) = sum(p_i)")


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

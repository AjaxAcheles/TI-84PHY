from math import pi, sqrt
from menu_sys import Menu_System


def spring_force():
    print("Hooke's Law: F = -k * x")
    print("Where:\nF = Restoring force (N)\nk = Spring constant (N/m)\nx = Displacement from equilibrium position (m)")


def oscillatory_motion():
    print("Position: x(t) = A * cos(wt)\nVelocity: v(t) = -Aw * sin(wt)\nAcceleration: a(t) = -Aw^2 * cos(wt)")
    print("Where:\nA = Amplitude (m)\nw = Angular frequency (rad/s)\nt = Time (s)")


def angular_frequency():
    print("Angular Frequency: w = 2pif = sqrt(k / m)")
    print("Where:\nw = Angular frequency (rad/s)\nf = Frequency (Hz)\nk = Spring constant (N/m)\nm = Mass (kg)")


def pendulum_frequency():
    print("Simple Pendulum Frequency: f = (1 / 2pi) * sqrt(g / L)")
    print("Where:\ng = Acceleration due to gravity (9.8 m/s^2)\nL = Length of the pendulum (m)")
    print("Physical Pendulum Frequency: f = (1 / 2pi) * sqrt(mgr / I)")
    print("Where:\nm = Mass (kg)\ng = Acceleration due to gravity (9.8 m/s^2)\nr = Distance to pivot (m)\nI = Moment of inertia (kg*m^2)")


def elastic_potential_energy():
    print("Elastic Potential Energy: E = 0.5 * k * x^2")
    print("Where:\nE = Elastic potential energy (J)\nk = Spring constant (N/m)\nx = Displacement (m)")


menu_structure = {
    "Main Menu": {
        "title": "Oscillatory Motion and Waves",
        "options": {
            "Spring Force (Hooke's Law)": spring_force,
            "Oscillatory Motion Equations": oscillatory_motion,
            "Angular Frequency": angular_frequency,
            "Pendulum Frequency": pendulum_frequency,
            "Elastic Potential Energy": elastic_potential_energy
        }
    }
}

menu_system = Menu_System(menu_structure)
menu_system.run() 



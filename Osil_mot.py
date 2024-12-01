from math import pi, sqrt
from menu_sys import Menu_System


def spring_force():
    print("Hooke's Law: F = -k * x")
    print("Where:F = Restoring force (N)\nk = Spring constant (N/m)\nx = Displacement from equilibrium position (m)")


def frequency():
    print("Frequency: f = (N/t) = 1/T")
    print("Frequency of spring: f = 1/2pi * sqrt(k/m)")
    print("Where:f = Frequency (Hz)\nk = Spring constant (N/m)\nm = Mass (kg)")


def angular_frequency():
    print("w = 2*pi*f")
    print("Where:w = Angular frequency (rad/s)\nf = Frequency (Hz)")


def oscillatory_motion():
    print("Position: x = A * cos(wt)")
    print("Velocity: v = -A * 2*pi*f * sin(2pi*f*t) = -v_max * sin(2pi*f*t))")
    print("Acceleration: a = -4A * pi^2 * f^2 * cos(2pi*f*t) = -a_max * cos(2pi*f*t)")
    print("Where:A = Amplitude (m)")


def simple_pendulum_frequency():
    print("Simple Pendulum Frequency: f = (1 / 2pi) * sqrt(g / L)")
    print("Where:g = Acceleration due to gravity (9.8 m/s^2)\nL = Length of the pendulum (m)")
    
    
def normal_pendulum_frequency():
    print("Physical Pendulum Frequency: f = (1 / 2pi) * sqrt(mgr / I)")
    print("Where:m = Mass (kg)\ng = Acceleration due to gravity (9.8 m/s^2)\nr = Distance to pivot (m)\nI = Moment of inertia (kg*m^2)")
    print("Beam Pendulum Frequency: f = (1 / 2pi) * sqrt(3g/2L)")


def elastic_potential_energy():
    print("Elastic Potential Energy: E = 0.5 * k * x^2")
    print("Where:E = Elastic potential energy (J)\nk = Spring constant (N/m)\nx = Displacement (m)")


menu_structure = {
    "Main Menu": {
        "title": "Oscillatory Motion and Waves",
        "options": {
            "Spring Force (Hooke's Law)": spring_force,
            "Frequency of Oscillations": frequency,
            "Oscillatory Motion Equations": oscillatory_motion,
            "Simple Pendulum Frequency": simple_pendulum_frequency,
            "Other Pendulum Frequencies": normal_pendulum_frequency,
            "Elastic Potential Energy": elastic_potential_energy,
            "Angular frequency": angular_frequency
        }
    }
}

menu_system = Menu_System(menu_structure)
menu_system.run() 



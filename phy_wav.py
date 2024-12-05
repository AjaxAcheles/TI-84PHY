from menu_sys import Menu_System
from ti_system import disp_clr

def wave_speed():
    disp_clr()
    print("Wave Speed Equation:")
    print("v = (lambda)f")
    print("Where:")
    print("v = wave speed")
    print("(lambda) = wavelength")
    print("f = frequency")

def wave_function():
    disp_clr()
    print("Wave Function:")
    print("y = A*sin((2*pi*x/(lambda) -+ 2pi*f*t))")
    print("Where:")
    print("-+ = wave direction (use - for +x direction and + for -x direction)")
    print("y = displacement")
    print("A = amplitude")
    print("x = position")
    print("(lambda) = wavelength")
    print("f = frequency")
    print("t = time")

def sound_pressure_variation():
    disp_clr()
    print("Sound Pressure Variation:")
    print("P = Pmax*sin((2*pi*x/(lambda) -+ 2pi*f*t))")
    print("Where:")
    print("-+ = wave direction (use - for +x direction and + for -x direction)")
    print("P = pressure variation")
    print("Pmax = maximum pressure variation")
    print("x = position")
    print("(lambda) = wavelength")
    print("f = frequency")
    print("t = time")

def speed_of_sound_in_air():
    disp_clr()
    print("Speed of Sound in Air:")
    print("v = 331 m/s * sqrt(1 + T/273)")
    print("Where:")
    print("v = speed of sound")
    print("T = temperature in Celsius")

def doppler_effect():
    disp_clr()
    print("Doppler Effect:")
    print("f_ob = f_s * ((v +- v_ob) / (v -+ v_s))")
    print("Where:")
    print("f_ob = observed frequency")
    print("f_s = source frequency")
    print("v = wave speed in the medium")
    print("v_s = source velocity (- if moving toward, + if moving away)")
    print("v_ob = observer velocity (+ if moving toward, - if moving away)")

def law_of_reflection():
    disp_clr()
    print("Law of Reflection:")
    print("(theta)_i = (theta)_r")
    print("Where:")
    print("(theta)_i = angle of incidence")
    print("(theta)_r = angle of reflection")

def standing_wave():
    disp_clr()
    print("Standing Wave:")
    print("y = 2A*sin(2*pi*x/(lambda))*cos(2*pi*f*t)")
    print("Where:")
    print("y = displacement")
    print("A = amplitude")
    print("x = position")
    print("(lambda) = wavelength")
    print("f = frequency")
    print("t = time")

def standing_wave_frequencies():
    disp_clr()
    print("Standing Wave Frequencies (fixed string and open tube):")
    print("fn = n * (v / 2*L)")
    print("Where:")
    print("fn = nth harmonic frequency")
    print("n = 1, 2, 3, ...")
    print("v = wave speed")
    print("L = length of string or tube")

def beat_frequency():
    disp_clr()
    print("Beat Frequency:")
    print("fbeat = |f1 - f2|")
    print("Where:")
    print("fbeat = beat frequency")
    print("f1, f2 = frequencies of interfering waves")

menu_structure = {
    "Main Menu": {
        "title": "Important Physics Equations",
        "options": {
            "Wave Speed": wave_speed,
            "Wave Function": wave_function,
            "Sound Pressure Variation": sound_pressure_variation,
            "Speed of Sound in Air": speed_of_sound_in_air,
            "Doppler Effect": doppler_effect,
            "Law of Reflection": law_of_reflection,
            "Standing Wave": standing_wave,
            "Standing Wave Frequencies": standing_wave_frequencies,
            "Beat Frequency": beat_frequency
        }
    }
}

menu_system = Menu_System(menu_structure)
menu_system.run()
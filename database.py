from classes import *
from datetime import *

barbers = [
    Barber("Bas"),
    Barber("Melanie"),
    Barber("Jan")
]

treatments = [
    Treatment("Cut", 30, 40),
    Treatment("Cut & Wash", 45, 45),
    Treatment("Cut & Dye", 90, 80)
]

shifts = [
    Shift(datetime(2023, 10, 24, 9, 30), datetime(2023, 10, 24, 17, 30), barbers[0]),
    Shift(datetime(2023, 10, 24, 9, 30), datetime(2023, 10, 24, 17, 30), barbers[1]),
    Shift(datetime(2023, 10, 24, 9, 30), datetime(2023, 10, 24, 17, 30), barbers[2])
]

appointments = [
    Appointment(datetime(2023, 10, 24, 9, 30), "Dennis", "0630943449", barbers[0], 30),
    Appointment(datetime(2023, 10, 24, 12, 30), "Jaap", "0630943449", barbers[0], 45),
    Appointment(datetime(2023, 10, 24, 15, 30), "Gijs", "0630943449", barbers[0], 90)

]

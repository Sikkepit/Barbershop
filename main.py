from functions import *
from database import *

barber_list = list_barber_names(barbers)
treatment_list = list_treatment_names(treatments)
free_slots = get_free_slots(shifts, appointments, "Bas")

new_appointment = make_appointment(barber_list, treatment_list, treatments, free_slots)
print(new_appointment)



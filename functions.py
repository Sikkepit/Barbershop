from datetime import *
from classes import *


def list_treatment_names(treatments):
    treatment_list = []
    for treatment in treatments:
        treatment_list.append(treatment.tr_name)
    return treatment_list


def get_treatment_duration(requested_treatment, treatment_list):
    for treatment in treatment_list:
        if treatment.tr_name == requested_treatment:
            duration = treatment.tr_duration
            return duration


def list_barber_names(barbers):
    barber_list = []
    for barber in barbers:
        barber_list.append(barber.barber_name)
    return barber_list


def validate_input(accepted_values, prompt):
    validated = False
    input_to_be_validated = ""
    while not validated:
        input_to_be_validated = input(prompt + "\n" + str(accepted_values) + "> ")
        for value in accepted_values:
            if value.lower() == input_to_be_validated.lower():
                input_to_be_validated = value
                validated = True
                break
        if not validated:
            print("The input is invalid.")
    return input_to_be_validated


def get_phone_number():
    validated = False
    while not validated:
        phone_number = str(input("What is your phone-number? "))
        if not phone_number.isnumeric():
            print("Only use numbers for the input.")
        elif len(phone_number) != 10:
            print("You should enter 10 digits.")
        else:
            return phone_number


def validate_time_slot(list_with_time_slots):
    validated = False
    while not validated:
        time_slot = input("Please type the number of your preferred time slot: ")
        if not time_slot.isnumeric():
            print("The number is invalid.")
        elif int(time_slot) > len(list_with_time_slots):
            print("The time slot doesn't exist.")
        else:
            return time_slot


def make_appointment(barber_list, treatment_name_list, treatment_detail_list, free_slots):
    print("It's good to see you! You can use this app to schedule an appointment for your next haircut.")
    barber = validate_input(barber_list, "Who is your barber of choice?")
    treatment = validate_input(treatment_name_list, "What kind of treatment would you like?")
    duration = get_treatment_duration(treatment, treatment_detail_list)
    choose_a_time = list_free_slots(free_slots, duration)
    print("These are the available timeslots you can choose from:")
    for time_slot in choose_a_time:
        print(f"{time_slot}")
    chosen_time_slot = validate_time_slot(choose_a_time)
    appointment_date = choose_a_time[int(chosen_time_slot)-1]
    customer = input("What is your name? ")
    while not customer.replace(" ", "").isalpha():
        print("Name's can only contain letters. ")
        customer = input("What is your name? ")
    phone_number = get_phone_number()
    appointment = Appointment(appointment_date, customer, phone_number, barber, duration)
    return appointment


# Dividing a shift into 15 minute time blocks
def get_free_slots(shifts, appointments, barber):
    available_slots = []
    for shift in shifts:
        if str(shift.sh_barber) == barber:
            shift_time = shift.sh_begins_at
            block_list = []
            while shift_time < shift.sh_ends_at:
                block_list.append(shift_time)
                shift_time += timedelta(minutes=15)
            i = 1
            for block in block_list:
                available_slots.append([i, block, "Available"])
                i += 1

# Checking which time blocks are already taken by other appointments
    for appointment in appointments:
        blocked_slots = 0
        for slot in available_slots:
            if blocked_slots > 0:
                slot[2] = "Unavailable"
                blocked_slots -= 1
            if appointment.app_time == slot[1]:
                blocked_slots = (appointment.app_duration / 15) - 1
                slot[2] = "Unavailable"
    return available_slots


# Looking at which overlapping time blocks are unavailable considering the duration of appointments
def list_free_slots(free_slots, duration):
    slots = int((duration / 15))
    only_free_slots = []
    for slot in free_slots:
        if slot[2] != 'Unavailable':
            only_free_slots.append(slot)
    last_slot = len(only_free_slots)
    i = 0  # index for all the slots, available and unavailable
    x = 0  # index for available slots
    list_with_slots = []
    while i < last_slot - slots:
        if only_free_slots[i][1] == only_free_slots[i + slots][1] - timedelta(minutes=duration):
            slot_time = only_free_slots[i][1].strftime("%d %B, %H:%M")
            list_with_slots.append(f"Slot {x+1}, {slot_time}")
            x += 1
        i += 1
    return list_with_slots

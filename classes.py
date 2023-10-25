class Barber:
    def __init__(self, barber_name):
        self.barber_name = barber_name

    def __str__(self):
        return self.barber_name

    def __repr__(self):
        return str(self)


class Treatment:
    def __init__(self, tr_name, tr_duration, tr_price):
        self.tr_name = tr_name
        self.tr_duration = tr_duration
        self.tr_price = tr_price

    def __str__(self):
        return f"{self.tr_name}, €{self.tr_price}"


class Shift:
    def __init__(self, sh_begins_at, sh_ends_at, sh_barber):
        self.sh_begins_at = sh_begins_at
        self.sh_ends_at = sh_ends_at
        self.sh_barber = sh_barber


class Appointment:
    def __init__(self, app_time, customer, phone_number, barber, app_duration):
        self.app_time = app_time
        self.customer = customer
        self.phone_number = phone_number
        self.barber = barber
        self.app_duration = app_duration

    def __str__(self):
        app_date = self.app_time.split(", ")
        return (f'Hi {self.customer}, You\'ve successfully made an appointment with {self.barber}! '
                f'We will see you on {app_date[1]} at {app_date[2]}. '
                f'The phone number you\'ve supplied is {self.phone_number}. '
                f'Have a nice day!')

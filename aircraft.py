class Aircraft:
    def __init__(self, name, current_hours):
        self.name = name
        self.current_hours = current_hours

    def update_hours(self, hours):
        if hours < 0:
            raise ValueError("Aircraft hours cannot be negative.")
        self.current_hours = hours

    def __str__(self):
        return self.name + " - " + str(self.current_hours) + " flight hours"
    

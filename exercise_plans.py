#This function creates an Exercise Plan object with specified attributes and returns it
class ExercisePlan:
    def __init__(self, trainer, equipment, duration=0):
        self.trainer = trainer
        self.equipment = equipment
        self.duration = duration

    def __str__(self):
        return f"Trainer: {self.trainer}, Equipment: {self.equipment}, Duration: {self.duration}"

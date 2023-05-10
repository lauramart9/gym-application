class Subscription:
    def __init__(self, customer, trainer, exercise_plan, start_date, end_date):
        self.customer = customer
        self.trainer = trainer
        self.exercise_plan = exercise_plan
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Customer: {self.customer}, Trainer: {self.trainer}, Exercise Plan: {self.exercise_plan}, Start Date: {self.start_date}, End Date: {self.end_date}"

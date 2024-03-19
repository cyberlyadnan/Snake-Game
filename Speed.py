import time

# Define the initial delay values for each level
# EASY_DELAY = 0.9999999999
# MEDIUM_DELAY = 0.09999999
# HARD_DELAY = 0.99

class Speed:
    def __init__(self):
        # Initialize the delay values for each level
        self.easy_delay = 0.499
        self.medium_delay = 0.299
        self.hard_delay = 0.99

    def easy_level(self):
        # Decrease the delay value for the easy level
        self.easy_delay -= 0.015
        print(self.easy_delay)
        return time.sleep(self.easy_delay)
        # EASY_DELAY += -0.099

    def medium_level(self):
        # Decrease the delay value for the medium level
        self.medium_delay -= 0.010
        print(self.medium_delay)
        return time.sleep(self.medium_delay)
        # MEDIUM_DELAY += -0.0055

    def hard_level(self):
        # Decrease the delay value for the hard level
        self.hard_delay -= 0.05
        print(self.hard_delay)
        return time.sleep(self.hard_delay)
        # HARD_DELAY =+ -0.0011

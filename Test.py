class Character_Research_Tracker:
    def __init__(self) -> None:
        self.metal_research_days_s0 = 0
        self.metal_research_days_s1 = 0
        self.metal_research_days_s2 = 0

        self.cloth_research_days_s0 = 0
        self.cloth_research_days_s1 = 0
        self.cloth_research_days_s2 = 0

        self.wood_research_days_s0 = 0
        self.wood_research_days_s1 = 0
        self.wood_research_days_s2 = 0

        self.jewelry_research_days = 0

        self.metal_days_passed_s0 = 0
        self.metal_days_passed_s1 = 0
        self.metal_days_passed_s2 = 0

        self.cloth_days_passed_s0 = 0
        self.cloth_days_passed_s1 = 0
        self.cloth_days_passed_s2 = 0

        self.wood_days_passed_s0 = 0
        self.wood_days_passed_s1 = 0
        self.wood_days_passed_s2 = 0

        self.jewelry_days_passed = 0

    # Ran upon server moving to new day
    def update_days_passed(self):
        self.metal_days_passed_s0 += 1
        self.metal_days_passed_s1 += 1
        self.metal_days_passed_s2 += 1

        self.cloth_days_passed_s0 += 1
        self.cloth_days_passed_s1 += 1
        self.cloth_days_passed_s2 += 1

        self.wood_days_passed_s0 += 1
        self.wood_days_passed_s1 += 1
        self.wood_days_passed_s2 += 1

        self.jewelry_days_passed += 1

# Test Code
# test_class = Character_Research_Tracker()
# test_class.update_days_passed()
# test_class.update_days_passed()
# test_class.update_days_passed()
# print(test_class.metal_days_passed_s0)


# When character loads up the following checks are made
# if remaining days greater than 0?
# Subtract days passed from remaining days

# If remaining days is less than 1,
# Mark research completed

# When starting new research, 
# Set remaining days variable for research slot equal to appropriate days
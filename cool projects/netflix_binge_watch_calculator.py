#******************************************
# 01. Netflix Binge-Watching Planner     #
# Concepts: Variables, Functions, If/Else #
# Data Types, Operators, Casting         #
#******************************************
def calculate_binge_time(episodes, episode_length):
    """Calculate total time needed to binge a series"""
    total_minutes = episodes * episode_length
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes

def can_finish_today(total_hours, available_hours):
    """Check if you can finish the series today"""
    if total_hours <= available_hours:
        return True
    else:
        return False

# Real scenario: Planning to watch "Stranger Things"
series_name = "Stranger Things"
episodes = 34
episode_length = 50  # minutes

hours, minutes = calculate_binge_time(episodes, episode_length)
available_time = int(input("How many hours you have available today? "))  # hours available today

print(f"Total time needed: {hours}h {minutes}m")

if can_finish_today(hours, available_time):
    print("Perfect! You can finish it today!")
else:
    days_needed = hours // available_time + 1
    print(f"You'll need {days_needed} days to finish")
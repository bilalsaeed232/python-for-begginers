#******************************************
# 03. Phone Battery Life Predictor       #
# Concepts: Variables, Numbers, If/Else  #
# Operators, Casting, Booleans          #
#******************************************

# Current battery status
current_battery = int(input("Current battery percentage: "))
screen_time = float(input("Hours of screen time per day: "))

# Battery drain calculations
drain_per_hour = 15  # Percentage per hour of screen time
hours_left = current_battery / drain_per_hour

# Check if you'll make it through the day
hours_until_bedtime = 24 - 8  # Assuming 8 AM start
will_survive = hours_left >= hours_until_bedtime
needs_charging = current_battery < 20

print(f"Battery remaining: {current_battery}%")
print(f"Estimated hours left: {hours_left:.1f}h")

if needs_charging:
    print("🔴 LOW BATTERY! Charge now!")
elif will_survive:
    print("✅ You'll make it through the day!")
else:
    print("⚠️ You might need to charge later")

# Charging time needed
if current_battery < 100:
    charge_needed = 100 - current_battery
    charging_time = charge_needed / 50  # 50% per hour charging
    print(f"To full charge: {charging_time:.1f} hours")
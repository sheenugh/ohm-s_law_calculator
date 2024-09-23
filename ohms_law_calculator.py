# =========== PSEUDO CODE ==========
# || ACTUAL CODE ||
# === Computation using conditional statement ===
def find_voltage():
    while True:
        # - Ask the user what they want to calculate: Voltage, Current, or Resistance.
        print("What do you want to calculate?\n1 = Voltage\n2 = Current\n3 = Resistance\nPick from 1-3")
        ask_what_to_calculate = input("\nInput your choice here: ")
        
        # - Conditional Statement: If voltage was chosen.
        if ask_what_to_calculate == "1":
            print("If so, give me the values of current and resistance so that we could find the value of the voltage.")
            while True:
                try:
                    ask_user_for_current_value = float(input("\nCurrent Value: "))
                    ask_user_for_resistance_value = float(input("Resistance Value: "))
                    voltage = ask_user_for_current_value * ask_user_for_resistance_value
                    print(f"The value of the voltage is {voltage}V.")
                    break
                except ValueError:
                    print("\nError.\nInvalid input.")
            break
        # - Conditional Statement: If current was chosen.
        elif ask_what_to_calculate == "2":
            print("If so, give me the values of voltage and resistance so that we could find the value of the current.")
            while True:
                try:
                    ask_user_for_voltage_value = float(input("\nVoltage Value: "))
                    ask_user_for_resistance_value = float(input("Resistance Value: "))
                    if ask_user_for_resistance_value == 0:
                        raise ZeroDivisionError
                    current = ask_user_for_voltage_value / ask_user_for_resistance_value
                    print(f"The value of the current is {current}A.")
                    break
                except ZeroDivisionError:
                    print("\nError.\nCannot be divide to 0.")
                except ValueError:
                    print("\nError.\nInvalid input.")
            break
        # - Conditional Statement: If resistance was chosen.
        elif ask_what_to_calculate == "3":
            print("If so, give me the values of voltage and current so that we could find the value of the resistance.")
            while True:
                try:
                    ask_user_for_voltage_value = float(input("\nVoltage Value: "))
                    ask_user_for_current_value = float(input("Current Value: "))
                    if ask_user_for_current_value == 0:
                        raise ZeroDivisionError
                    resistance = ask_user_for_voltage_value / ask_user_for_current_value
                    print(f"The value of the resistance is {resistance}Ω.")
                    break
                except ZeroDivisionError:
                    print("\nError.\nCannot be divide to 0.")
                except ValueError:
                    print("\nError.\nInvalid input.")
            break
        else:
            print("\nError\nNot among the mentioned choices.")
        
                
find_voltage()

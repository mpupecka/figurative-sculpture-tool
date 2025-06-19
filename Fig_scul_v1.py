# %%
# Figurative Sculpture Body Scaler
# Author: Malgorzata Pupecka-Swider
# Version: 1.0
# Date: 2025-06-19
# Description: Scales human body proportions for figurative sculpture based on target height.

import math
def scale_body_proportions():
    print("Welcome to the Figurative Sculpture Body Scaler!")
    try:
        target_height_cm = float(input("Enter the desired height of the sculpture (in cm): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Proportional values based on mixed references from internet and books
    # These proportions are based on a standard human body, adjusted for a figurative sculpture style
    proportions = {
        "Head height (chin to crown)": 0.133,  # 1/7.5
        "Head height (mastoid to crown)": 0.100,  # Approximate, slightly less than full head
        "Head width (biparietal)": 0.067,  # About half head height-I need to check this
        "Neck length": 0.040,
        "Clavicle length (each)": 0.09,
        "Shoulder width (widest point)": 0.235,
        "Upper arm length (from armpit to inside of elbow)": 0.16,
        "Forearm length (radius/ulna)": 0.12,
     # Sculptural hand and palm bones (~20% larger than natural)

        "Hand length (sculptural max)": 0.12,  
        "Hand palm length (sculptural max)": 0.06,  
        "Hand Metacarpal (Thumb, sculptural max)": 0.023,
        "Hand Metacarpal (Index, sculptural max)": 0.036,
        "Hand Metacarpal (Middle, sculptural max)": 0.038,
        "Hand Metacarpal (Ring, sculptural max)": 0.033,
        "Hand Metacarpal (Little, sculptural max)": 0.031,
        "Hand Thumb Proximal Phalanx (sculptural max)": 0.020,
        "Hand Thumb Distal Phalanx (sculptural max)": 0.018,
        "Hand Index Proximal Phalanx (sculptural max)": 0.024,
        "Hand Index Intermediate Phalanx (sculptural max)": 0.024/1.618,  # Golden ratio approximation
        "Hand Index Distal Phalanx (sculptural max)": 0.024/1.618/1.618,  # Golden ratio approximation
        "Hand Middle Proximal Phalanx (sculptural max)": 0.029,
        "Hand Middle Intermediate Phalanx (sculptural max)": 0.029/1.618,  # Golden ratio approximation
        "Hand Middle Distal Phalanx (sculptural max)": 0.029/1.618/1.618,  # Golden ratio approximation
       
        "Hand Ring Proximal Phalanx (sculptural max)": 0.027,
        "Hand Ring Intermediate Phalanx (sculptural max)": 0.027/1.618,  # Golden ratio approximation

        "Hand Ring Distal Phalanx (sculptural max)": 0.027/1.618/1.618,  # Golden ratio approximation
        "Hand Little Proximal Phalanx (sculptural max)": 0.0216,
        "Hand Little Intermediate Phalanx (sculptural max)": 0.0216/1.618,  # Golden ratio approximation
        "Hand Little Distal Phalanx (sculptural max)": 0.0216/1.618/1.618,  # Golden ratio approximation
   
        "Torso length (neck to pubis)": 0.32,
        "Pelvis width": 0.170,
        "Waist width": 0.140,
        "Ribcage width": 0.160,
        "Femur length (from hip to centre of knee cap)": 0.240,
        "Tibia length(from below knee cap to medial ankle)": 0.208,
        "Knee height (floor to under kneecap)": 0.252, #checked
        "Ankle height (floor to medial malleolus)": 0.252-0.208,  # knee high minus Tibia length
        "Foot length": 0.132, #checked
        "Foot width from outsie of bit toe knuckle to outide of small toe ": 0.050,  # Approximate, based on average foot width


    }
    
    print(f"\nScaled body part dimensions for a sculpture of {target_height_cm} cm:\n")
    for part, ratio in proportions.items():
        length = target_height_cm * ratio
        print(f"{part}: {length:.2f} cm")
    ankle_height = proportions["Ankle height (floor to medial malleolus)"] * target_height_cm
    foot_width_midknuckle = proportions["Ankle height (floor to medial malleolus)"] * target_height_cm #same as ankle height
    print(f"Foot width from centre of big toe knuckle to outside of small toe: {foot_width_midknuckle:.2f} cm")
    foot_slope_length = math.sqrt(((ankle_height*2) ** 2) + (ankle_height ** 2))
    print(f"Slope of foot lenth from front top on ankle square to tip of big toe: {foot_slope_length:.2f} cm")    # Print the scaled dimensions
    print(f"Ankle height for ankle square measurement is: {ankle_height:.2f} cm")
# Run the program
scale_body_proportions()





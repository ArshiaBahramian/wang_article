import pandas as pd

n_samples = 20

administartion = {1: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  2: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  3: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  4: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  5: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  6: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  7: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  8: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  9: {'Option1': {'Cost': 90, 'Quality': 0.7},
                      'Option2': {'Cost': 120, 'Quality': 0.85},
                      'Option3': {'Cost': 150, 'Quality': 1.0}},
                  10: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  11: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  12: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  13: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  14: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  15: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  16: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  17: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  18: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  19: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}},
                  20: {'Option1': {'Cost': 90, 'Quality': 0.7},
                       'Option2': {'Cost': 120, 'Quality': 0.85},
                       'Option3': {'Cost': 150, 'Quality': 1.0}}}

material = {
    1: {"Option1": {"Cost": 3200, "Quality": 0.7},
        "Option2": {"Cost": 3850, "Quality": 0.85},
        "Option3": {"Cost": 4500, "Quality": 1.0}},
    2: {"Option1": {"Cost": 800, "Quality": 0.7},
        "Option2": {"Cost": 950, "Quality": 0.85},
        "Option3": {"Cost": 1100, "Quality": 1.0}},
    3: {"Option1": {"Cost": 5600, "Quality": 0.7},
        "Option2": {"Cost": 6400, "Quality": 0.85},
        "Option3": {"Cost": 7200, "Quality": 1.0}},
    4: {"Option1": {"Cost": 18200, "Quality": 0.7},
        "Option2": {"Cost": 20800, "Quality": 0.85},
        "Option3": {"Cost": 23400, "Quality": 1.0}},
    5: {"Option1": {"Cost": 16000, "Quality": 0.7},
        "Option2": {"Cost": 18000, "Quality": 0.85},
        "Option3": {"Cost": 20000, "Quality": 1.0}},
    6: {"Option1": {"Cost": 6400, "Quality": 0.7},
        "Option2": {"Cost": 7500, "Quality": 0.85},
        "Option3": {"Cost": 8600, "Quality": 1.0}},
    7: {"Option1": {"Cost": 1200, "Quality": 0.7},
        "Option2": {"Cost": 1450, "Quality": 0.85},
        "Option3": {"Cost": 1700, "Quality": 1.0}},
    8: {"Option1": {"Cost": 11200, "Quality": 0.7},
        "Option2": {"Cost": 12800, "Quality": 0.85},
        "Option3": {"Cost": 14400, "Quality": 1.0}},
    9: {"Option1": {"Cost": 16800, "Quality": 0.7},
        "Option2": {"Cost": 19200, "Quality": 0.85},
        "Option3": {"Cost": 21600, "Quality": 1.0}},
    10: {"Option1": {"Cost": 13200, "Quality": 0.7},
         "Option2": {"Cost": 14900, "Quality": 0.85},
         "Option3": {"Cost": 16600, "Quality": 1.0}},
    11: {"Option1": {"Cost": 1100, "Quality": 0.7},
         "Option2": {"Cost": 1350, "Quality": 0.85},
         "Option3": {"Cost": 1600, "Quality": 1.0}},
    12: {"Option1": {"Cost": 9800, "Quality": 0.7},
         "Option2": {"Cost": 11200, "Quality": 0.85},
         "Option3": {"Cost": 12600, "Quality": 1.0}},
    13: {"Option1": {"Cost": 15050, "Quality": 0.7},
         "Option2": {"Cost": 17200, "Quality": 0.85},
         "Option3": {"Cost": 19350, "Quality": 1.0}},
    14: {"Option1": {"Cost": 11700, "Quality": 0.7},
         "Option2": {"Cost": 13200, "Quality": 0.85},
         "Option3": {"Cost": 14700, "Quality": 1.0}},
    15: {"Option1": {"Cost": 1100, "Quality": 0.7},
         "Option2": {"Cost": 1350, "Quality": 0.85},
         "Option3": {"Cost": 1600, "Quality": 1.0}},
    16: {"Option1": {"Cost": 7700, "Quality": 0.7},
         "Option2": {"Cost": 8800, "Quality": 0.85},
         "Option3": {"Cost": 9900, "Quality": 1.0}},
    17: {"Option1": {"Cost": 13300, "Quality": 0.7},
         "Option2": {"Cost": 15200, "Quality": 0.85},
         "Option3": {"Cost": 17100, "Quality": 1.0}},
    18: {"Option1": {"Cost": 10600, "Quality": 0.7},
         "Option2": {"Cost": 11950, "Quality": 0.85},
         "Option3": {"Cost": 13300, "Quality": 1.0}},
    19: {"Option1": {"Cost": 3200, "Quality": 0.7},
         "Option2": {"Cost": 3500, "Quality": 0.85},
         "Option3": {"Cost": 3800, "Quality": 1.0}},
    20: {"Option1": {"Cost": 7000, "Quality": 0.7},
         "Option2": {"Cost": 7750, "Quality": 0.85},
         "Option3": {"Cost": 8500, "Quality": 1.0}}
}

equipment = {
    1: {"Option1": {"Cost": 1440.0, "Quality": 0.8},
        "Option2": {"Cost": 1200.0, "Quality": 0.9},
        "Option3": {"Cost": 1040.0, "Quality": 1.0}},
    2: {"Option1": {"Cost": 1210.0, "Quality": 0.8},
        "Option2": {"Cost": 1150.0, "Quality": 0.9},
        "Option3": {"Cost": 1100.0, "Quality": 1.0}},
    3: {"Option1": {"Cost": 341.3, "Quality": 0.8},
        "Option2": {"Cost": 310.9, "Quality": 0.9},
        "Option3": {"Cost": 288.0, "Quality": 1.0}},
    4: {"Option1": {"Cost": 520.0, "Quality": 0.9},
        "Option2": {"Cost": 490.3, "Quality": 0.95},
        "Option3": {"Cost": 468.0, "Quality": 1.0}},
    5: {"Option1": {"Cost": 14062.5, "Quality": 0.8},
        "Option2": {"Cost": 12375.0, "Quality": 0.9},
        "Option3": {"Cost": 11250.0, "Quality": 1.0}},
    6: {"Option1": {"Cost": 360.0, "Quality": 0.8},
        "Option2": {"Cost": 360.0, "Quality": 0.9},
        "Option3": {"Cost": 360.0, "Quality": 1.0}},
    7: {"Option1": {"Cost": 3150.0, "Quality": 0.9},
        "Option2": {"Cost": 2778.9, "Quality": 0.95},
        "Option3": {"Cost": 2509.1, "Quality": 1.0}},
    8: {"Option1": {"Cost": 1024.0, "Quality": 0.8},
        "Option2": {"Cost": 870.4, "Quality": 0.9},
        "Option3": {"Cost": 768.0, "Quality": 1.0}},
    9: {"Option1": {"Cost": 1371.4, "Quality": 0.9},
        "Option2": {"Cost": 1242.4, "Quality": 0.95},
        "Option3": {"Cost": 1152.0, "Quality": 1.0}},
    10: {"Option1": {"Cost": 19220.0, "Quality": 0.8},
         "Option2": {"Cost": 16913.6, "Quality": 0.9},
         "Option3": {"Cost": 15376.0, "Quality": 1.0}},
    11: {"Option1": {"Cost": 2362.5, "Quality": 0.8},
         "Option2": {"Cost": 2100.0, "Quality": 0.9},
         "Option3": {"Cost": 1909.1, "Quality": 1.0}},
    12: {"Option1": {"Cost": 784.0, "Quality": 0.8},
         "Option2": {"Cost": 666.4, "Quality": 0.9},
         "Option3": {"Cost": 588.0, "Quality": 1.0}},
    13: {"Option1": {"Cost": 1105.7, "Quality": 0.9},
         "Option2": {"Cost": 986.5, "Quality": 0.95},
         "Option3": {"Cost": 903.0, "Quality": 1.0}},
    14: {"Option1": {"Cost": 15125.0, "Quality": 0.8},
         "Option2": {"Cost": 13310.0, "Quality": 0.9},
         "Option3": {"Cost": 12100.0, "Quality": 1.0}},
    15: {"Option1": {"Cost": 2442.9, "Quality": 0.8},
         "Option2": {"Cost": 2179.4, "Quality": 0.9},
         "Option3": {"Cost": 1995.0, "Quality": 1.0}},
    16: {"Option1": {"Cost": 484.0, "Quality": 0.8},
         "Option2": {"Cost": 411.4, "Quality": 0.9},
         "Option3": {"Cost": 363.0, "Quality": 1.0}},
    17: {"Option1": {"Cost": 950.0, "Quality": 0.9},
         "Option2": {"Cost": 813.6, "Quality": 0.95},
         "Option3": {"Cost": 722.0, "Quality": 1.0}},
    18: {"Option1": {"Cost": 12500.0, "Quality": 0.8},
         "Option2": {"Cost": 11000.0, "Quality": 0.9},
         "Option3": {"Cost": 10000.0, "Quality": 1.0}},
    19: {"Option1": {"Cost": 300.0, "Quality": 0.8},
         "Option2": {"Cost": 289.3, "Quality": 0.9},
         "Option3": {"Cost": 281.3, "Quality": 1.0}},
    20: {"Option1": {"Cost": 400.0, "Quality": 0.8},
         "Option2": {"Cost": 391.1, "Quality": 0.9},
         "Option3": {"Cost": 384.0, "Quality": 1.0}}
}

volume = {
    1: 1.9,
    2: 10.0,
    3: 2.3,
    4: 3.0,
    5: 7.5,
    6: 2.7,
    7: 12.6,
    8: 3.2,
    9: 5.6,
    10: 12.4,
    11: 11.1,
    12: 2.8,
    13: 5.1,
    14: 11.0,
    15: 11.2,
    16: 2.2,
    17: 4.5,
    18: 10.0,
    19: 6.4,
    20: 3.6
}

labor_cost = {
    1: 700,
    2: 300,
    3: 600,
    4: 750,
    5: 1700,
    6: 430,
    7: 450,
    8: 800,
    9: 1000,
    10: 750,
    11: 460,
    12: 800,
    13: 100,
    14: 750,
    15: 470,
    16: 800,
    17: 1000,
    18: 750,
    19: 300,
    20: 750
}

task_list = []

for task_no in range(1, 21, 1):
    for admin_option in ["Option1", "Option2", "Option3"]:
        for material_option in ["Option1", "Option2", "Option3"]:
            for equip_option in ["Option1", "Option2", "Option3"]:
                for work_day in [5, 6, 7]:
                    for day_hour in [8, 9, 10, 11, 12]:
                        task_list.append({
                            "task_no": task_no,
                            "administration_option": admin_option,
                            "administration_cost": administartion[task_no][admin_option]["Cost"],
                            "administration_quality": administartion[task_no][admin_option]["Quality"],
                            "material_option": material_option,
                            "material_cost": material[task_no][material_option]["Cost"],
                            "material_quality": material[task_no][material_option]["Quality"],
                            "equipment_option": equip_option,
                            "equipment_cost": equipment[task_no][equip_option]["Cost"],
                            "equipment_quality": equipment[task_no][equip_option]["Quality"],
                            "volume": volume[task_no],
                            "labor_cost": labor_cost[task_no],
                            "work_day": work_day,
                            "day_hour": day_hour
                        })


def e_calculator(work_day, day_hour):
    if work_day == 5 and day_hour == 8:
        return 1
    elif work_day == 5 and day_hour == 9:
        return 0.9
    elif work_day == 5 and day_hour == 10:
        return 0.85
    elif work_day == 5 and day_hour == 11:
        return 0.65
    elif work_day == 5 and day_hour == 12:
        return 0.6
    elif work_day == 6 and day_hour == 8:
        return 0.9
    elif work_day == 6 and day_hour == 9:
        return 0.85
    elif work_day == 6 and day_hour == 10:
        return 0.8
    elif work_day == 6 and day_hour == 11:
        return 0.65
    elif work_day == 6 and day_hour == 12:
        return 0.6
    elif work_day == 7 and day_hour == 8:
        return 0.75
    elif work_day == 7 and day_hour == 9:
        return 0.7
    elif work_day == 7 and day_hour == 10:
        return 0.65
    elif work_day == 7 and day_hour == 11:
        return 0.6
    elif work_day == 7 and day_hour == 12:
        return 0.55


df = pd.DataFrame(task_list)
df["e"] = [e_calculator(wd, dh) for wd, dh in df[["work_day", "day_hour"]].values]

df["duration"] = df["volume"] / (df["day_hour"] / 8 * df["e"])
df.to_csv("tasks.csv", index=False)

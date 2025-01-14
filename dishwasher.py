from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
import random
import time


class washer:
    def __init__(self, dirtiness, dish_quantity, water_hardness):
        self.dirtiness_input = dirtiness
        self.dish_quantity_input = dish_quantity
        self.water_hardness_input = water_hardness

        self.rules = {}

        # Inputs
        self.dirtiness = np.arange(0, 6, 1)
        self.dish_quantity = np.arange(0, 11, 1)
        self.water_hardness = np.arange(0, 11, 1)

        # Outputs
        self.wash_time = np.arange(0, 61, 1)
        self.detergent = np.arange(0, 11, 1)
        self.water_temperature = np.arange(30, 91, 1)

    def initrialize(self):
        '''INPUTS'''
        # Dirtiness Level
        # Range: 0 (clean) to 5 (extremely dirty)
        dirtiness_low = fuzz.trimf(self.dirtiness, [0, 0, 2])
        dirtiness_medium = fuzz.trimf(self.dirtiness, [1, 3, 5])
        dirtiness_high = fuzz.trimf(self.dirtiness, [3, 5, 5])

        # Dish Quantity
        # Range: 0 (no dishes) to 10 (maximum capacity)
        dish_quantity_few = fuzz.trimf(self.dish_quantity, [0, 0, 3])
        dish_quantity_moderate = fuzz.trimf(self.dish_quantity, [2, 5, 7])
        dish_quantity_many = fuzz.trimf(self.dish_quantity, [6, 10, 10])

        # Water Hardness
        # Range: 0 (soft water) to 10 (very hard water)
        water_hardness_soft = fuzz.trimf(self.water_hardness, [0, 0, 3])
        water_hardness_moderate = fuzz.trimf(self.water_hardness, [2, 5, 8])
        water_hardness_hard = fuzz.trimf(self.water_hardness, [7, 10, 10])

        '''OUTPUTS'''
        # Wash Time
        # Range: 0 to 60 minutes
        wash_time_short = fuzz.trimf(self.wash_time, [0, 15, 30])
        wash_time_medium = fuzz.trimf(self.wash_time, [20, 30, 45])
        wash_time_long = fuzz.trimf(self.wash_time, [40, 60, 60])

        # Detergent Amount
        # Range: 0 (none) to 10 (maximum dosage)
        detergent_low = fuzz.trimf(self.detergent, [0, 2, 5])
        detergent_medium = fuzz.trimf(self.detergent, [3, 5, 8])
        detergent_high = fuzz.trimf(self.detergent, [7, 10, 10])

        # Water Temperature
        # Range: 30°C to 90°C
        water_temperature_low = fuzz.trimf(self.water_temperature, [30, 40, 50])
        water_temperature_medium = fuzz.trimf(self.water_temperature, [50, 60, 70])
        water_temperature_high = fuzz.trimf(self.water_temperature, [70, 80, 90])

        '''KNOWLEDGE BASE'''
        self.rules = {
            'rule1': {
                'conditions': (dirtiness_low, dish_quantity_few, water_hardness_soft),
                'outputs': (wash_time_short, detergent_low, water_temperature_low)
            },
            'rule2': {
                'conditions': (dirtiness_low, dish_quantity_few, water_hardness_moderate),
                'outputs': (wash_time_short, detergent_low, water_temperature_medium)
            },
            'rule3': {
                'conditions': (dirtiness_low, dish_quantity_few, water_hardness_hard),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule4': {
                'conditions': (dirtiness_low, dish_quantity_moderate, water_hardness_soft),
                'outputs': (wash_time_short, detergent_low, water_temperature_medium)
            },
            'rule5': {
                'conditions': (dirtiness_low, dish_quantity_moderate, water_hardness_moderate),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule6': {
                'conditions': (dirtiness_low, dish_quantity_moderate, water_hardness_hard),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule7': {
                'conditions': (dirtiness_low, dish_quantity_many, water_hardness_soft),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule8': {
                'conditions': (dirtiness_low, dish_quantity_many, water_hardness_moderate),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule9': {
                'conditions': (dirtiness_low, dish_quantity_many, water_hardness_hard),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule10': {
                'conditions': (dirtiness_medium, dish_quantity_few, water_hardness_soft),
                'outputs': (wash_time_medium, detergent_low, water_temperature_medium)
            },
            'rule11': {
                'conditions': (dirtiness_medium, dish_quantity_few, water_hardness_moderate),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule12': {
                'conditions': (dirtiness_medium, dish_quantity_few, water_hardness_hard),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule13': {
                'conditions': (dirtiness_medium, dish_quantity_moderate, water_hardness_soft),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule14': {
                'conditions': (dirtiness_medium, dish_quantity_moderate, water_hardness_moderate),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule15': {
                'conditions': (dirtiness_medium, dish_quantity_moderate, water_hardness_hard),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            },
            'rule16': {
                'conditions': (dirtiness_medium, dish_quantity_many, water_hardness_soft),
                'outputs': (wash_time_long, detergent_medium, water_temperature_high)
            },
            'rule17': {
                'conditions': (dirtiness_medium, dish_quantity_many, water_hardness_moderate),
                'outputs': (wash_time_long, detergent_medium, water_temperature_high)
            },
            'rule18': {
                'conditions': (dirtiness_medium, dish_quantity_many, water_hardness_hard),
                'outputs': (wash_time_long, detergent_medium, water_temperature_high)
            },
            'rule19': {
                'conditions': (dirtiness_high, dish_quantity_few, water_hardness_soft),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_medium)
            },
            'rule20': {
                'conditions': (dirtiness_high, dish_quantity_few, water_hardness_moderate),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_high)
            },
            'rule21': {
                'conditions': (dirtiness_high, dish_quantity_few, water_hardness_hard),
                'outputs': (wash_time_medium, detergent_medium, water_temperature_high)
            },
            'rule22': {
                'conditions': (dirtiness_high, dish_quantity_moderate, water_hardness_soft),
                'outputs': (wash_time_medium, detergent_high, water_temperature_medium)
            },
            'rule23': {
                'conditions': (dirtiness_high, dish_quantity_moderate, water_hardness_moderate),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            },
            'rule24': {
                'conditions': (dirtiness_high, dish_quantity_moderate, water_hardness_hard),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            },
            'rule25': {
                'conditions': (dirtiness_high, dish_quantity_many, water_hardness_soft),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            },
            'rule26': {
                'conditions': (dirtiness_high, dish_quantity_many, water_hardness_moderate),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            },
            'rule27': {
                'conditions': (dirtiness_high, dish_quantity_many, water_hardness_hard),
                'outputs': (wash_time_long, detergent_high, water_temperature_high)
            }
        }

    # Inference Engine
    def infer(self):
        # Init
        aggregated_wash_time = np.zeros_like(self.wash_time)
        aggregated_detergent = np.zeros_like(self.detergent)
        aggregated_temperature = np.zeros_like(self.water_temperature)

        for idx, rule in enumerate(self.rules.values()):
            # Load membership functions
            condition_dirtiness, condition_quantity, condition_hardness = rule['conditions']
            output_wash_time, output_detergent, output_temperature = rule['outputs']

            # Compute membership values for inputs
            dirtiness_membership = fuzz.interp_membership(self.dirtiness, condition_dirtiness, self.dirtiness_input)
            dish_quantity_membership = fuzz.interp_membership(self.dish_quantity, condition_quantity, self.dish_quantity_input)
            water_hardness_membership = fuzz.interp_membership(self.water_hardness, condition_hardness, self.water_hardness_input)
            print(f'[!] Membership Value for rule.{idx+1}:\n\tdirtiness membership - {dirtiness_membership}\n\tdish quantity membership - {dish_quantity_membership}\n\twater hardness membership - {water_hardness_membership}')

            # Compute firing strength for the rule
            firing_strength = np.fmin(
                np.fmin(dirtiness_membership, dish_quantity_membership),
                water_hardness_membership
            )

            # Aggregate the outputs
            aggregated_wash_time = np.fmax(aggregated_wash_time, np.fmin(firing_strength, output_wash_time))
            aggregated_detergent = np.fmax(aggregated_detergent, np.fmin(firing_strength, output_detergent))
            aggregated_temperature = np.fmax(aggregated_temperature, np.fmin(firing_strength, output_temperature))

        print(f'\n[!] Aggregated wash time:\n{aggregated_wash_time}\n[!] Aggregated detergent:\n{aggregated_detergent}\n[!] Aggregated_temperature:\n{aggregated_temperature}\n')

        return aggregated_wash_time, aggregated_detergent, aggregated_temperature

    # Defuzzification
    def defuzzify(self, aggregated_wash_time, aggregated_detergent, aggregated_temperature):
        crisp_wash_time = fuzz.defuzz(self.wash_time, aggregated_wash_time, 'centroid')
        crisp_detergent = fuzz.defuzz(self.detergent, aggregated_detergent, 'centroid')
        crisp_temperature = fuzz.defuzz(self.water_temperature, aggregated_temperature, 'centroid')

        return crisp_wash_time, crisp_detergent, crisp_temperature

    def wash(self):
        print('[*] Activating Fuzzy Dishwasher 3000...')
        self.initrialize()
        time.sleep(1)
        print('[*] Done.')

        # Set input values
        print(f'[*] Current status:\n\t-dirtness:{self.dirtiness_input}\n\t-dish quantity:{self.dish_quantity_input}\n\t-water hardness:{self.water_hardness_input}')
        aggregated_wash_time, aggregated_detergent, aggregated_temperature = self.infer()
        time.sleep(1)

        # Perform computation
        print('[*] Performing computation...')
        crisp_wash_time, crisp_detergent, crisp_temperature = self.defuzzify(
            aggregated_wash_time,
            aggregated_detergent,
            aggregated_temperature
        )
        time.sleep(1)

        # Get outputs
        print(f"[*] Recommended Wash Time: {crisp_wash_time :.1f} minutes")
        print(f"[*] Recommended Detergent Amount: {crisp_detergent :.1f} units")
        print(f"[*] Recommended Water Temperature: {crisp_temperature :.1f} °C")
        time.sleep(1)

        # :)
        print('[*] Starting dishwasher...')
        progress_bar = [' \\ ', ' | ', ' / ', '---']
        for i in range(int(round(crisp_wash_time, 1))):
            print(f'\r[*] Washing ' + progress_bar[i % 4], end='')
            time.sleep(0.1)

        print('\r[*] Complete :)               ')


if __name__ == '__main__':
    print('=========Fuzzy Dishwasher 3000=========')
    random.seed(time.time())
    dirtiness = round(random.uniform(0, 5), 1)
    dish_quantity = random.randint(1, 10)
    water_hardness = round(random.uniform(0, 10), 1)

    mywasher = washer(dirtiness, dish_quantity, water_hardness)
    mywasher.wash()

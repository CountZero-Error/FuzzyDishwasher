from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np
import random
import time


class washer:
    def __init__(self, dirtiness, dish_quantity, water_hardness):
        self.dirtiness = dirtiness
        self.dish_quantity = dish_quantity
        self.water_hardness = water_hardness
        self.rules = {}

    def initrialize(self):
        '''INPUTS'''
        # Dirtiness Level
        dirtiness = ctrl.Antecedent(np.arange(0, 6, 1), 'dirtiness')
        dirtiness['low'] = fuzz.trimf(dirtiness.universe, [0, 0, 2])
        dirtiness['medium'] = fuzz.trimf(dirtiness.universe, [1, 3, 5])
        dirtiness['high'] = fuzz.trimf(dirtiness.universe, [3, 5, 5])

        # Dish Quantity
        dish_quantity = ctrl.Antecedent(np.arange(0, 11, 1), 'dish_quantity')
        dish_quantity['few'] = fuzz.trimf(dish_quantity.universe, [0, 0, 3])
        dish_quantity['moderate'] = fuzz.trimf(dish_quantity.universe, [2, 5, 7])
        dish_quantity['many'] = fuzz.trimf(dish_quantity.universe, [6, 10, 10])

        # Water Hardness
        water_hardness = ctrl.Antecedent(np.arange(0, 11, 1), 'water_hardness')
        water_hardness['soft'] = fuzz.trimf(water_hardness.universe, [0, 0, 3])
        water_hardness['moderate'] = fuzz.trimf(water_hardness.universe, [2, 5, 8])
        water_hardness['hard'] = fuzz.trimf(water_hardness.universe, [7, 10, 10])

        '''OUTPUTS'''
        # Wash Time
        wash_time = ctrl.Consequent(np.arange(0, 61, 1), 'wash_time')
        wash_time['short'] = fuzz.trimf(wash_time.universe, [0, 15, 30])
        wash_time['medium'] = fuzz.trimf(wash_time.universe, [20, 30, 45])
        wash_time['long'] = fuzz.trimf(wash_time.universe, [40, 60, 60])

        # Detergent Amount
        detergent = ctrl.Consequent(np.arange(0, 11, 1), 'detergent')
        detergent['low'] = fuzz.trimf(detergent.universe, [0, 2, 5])
        detergent['medium'] = fuzz.trimf(detergent.universe, [3, 5, 8])
        detergent['high'] = fuzz.trimf(detergent.universe, [7, 10, 10])

        # Water Temperature
        water_temperature = ctrl.Consequent(np.arange(30, 91, 1), 'water_temperature')
        water_temperature['low'] = fuzz.trimf(water_temperature.universe, [30, 40, 50])
        water_temperature['medium'] = fuzz.trimf(water_temperature.universe, [50, 60, 70])
        water_temperature['high'] = fuzz.trimf(water_temperature.universe, [70, 80, 90])

        self.IO = {
            'Inputs': {
                'dirtiness': dirtiness,
                'dish_quantity': dish_quantity,
                'water_hardness': water_hardness,
            },
            'Outputs': {
                'wash_time': wash_time,
                'detergent': detergent,
                'water_temperature': water_temperature,
            }
        }

        self.rules = {
            'rule1': ctrl.Rule(dirtiness['low'] & dish_quantity['few'] & water_hardness['soft'],
                               [wash_time['short'], detergent['low'], water_temperature['low']]),
            'rule2': ctrl.Rule(dirtiness['low'] & dish_quantity['few'] & water_hardness['moderate'],
                               [wash_time['short'], detergent['low'], water_temperature['medium']]),
            'rule3': ctrl.Rule(dirtiness['low'] & dish_quantity['few'] & water_hardness['hard'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule4': ctrl.Rule(dirtiness['low'] & dish_quantity['moderate'] & water_hardness['soft'],
                               [wash_time['short'], detergent['low'], water_temperature['medium']]),
            'rule5': ctrl.Rule(dirtiness['low'] & dish_quantity['moderate'] & water_hardness['moderate'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule6': ctrl.Rule(dirtiness['low'] & dish_quantity['moderate'] & water_hardness['hard'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule7': ctrl.Rule(dirtiness['low'] & dish_quantity['many'] & water_hardness['soft'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule8': ctrl.Rule(dirtiness['low'] & dish_quantity['many'] & water_hardness['moderate'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule9': ctrl.Rule(dirtiness['low'] & dish_quantity['many'] & water_hardness['hard'],
                               [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule10': ctrl.Rule(dirtiness['medium'] & dish_quantity['few'] & water_hardness['soft'],
                                [wash_time['medium'], detergent['low'], water_temperature['medium']]),
            'rule11': ctrl.Rule(dirtiness['medium'] & dish_quantity['few'] & water_hardness['moderate'],
                                [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule12': ctrl.Rule(dirtiness['medium'] & dish_quantity['few'] & water_hardness['hard'],
                                [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule13': ctrl.Rule(dirtiness['medium'] & dish_quantity['moderate'] & water_hardness['soft'],
                                [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule14': ctrl.Rule(dirtiness['medium'] & dish_quantity['moderate'] & water_hardness['moderate'],
                                [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule15': ctrl.Rule(dirtiness['medium'] & dish_quantity['moderate'] & water_hardness['hard'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
            'rule16': ctrl.Rule(dirtiness['medium'] & dish_quantity['many'] & water_hardness['soft'],
                                [wash_time['long'], detergent['medium'], water_temperature['high']]),
            'rule17': ctrl.Rule(dirtiness['medium'] & dish_quantity['many'] & water_hardness['moderate'],
                                [wash_time['long'], detergent['medium'], water_temperature['high']]),
            'rule18': ctrl.Rule(dirtiness['medium'] & dish_quantity['many'] & water_hardness['hard'],
                                [wash_time['long'], detergent['medium'], water_temperature['high']]),
            'rule19': ctrl.Rule(dirtiness['high'] & dish_quantity['few'] & water_hardness['soft'],
                                [wash_time['medium'], detergent['medium'], water_temperature['medium']]),
            'rule20': ctrl.Rule(dirtiness['high'] & dish_quantity['few'] & water_hardness['moderate'],
                                [wash_time['medium'], detergent['medium'], water_temperature['high']]),
            'rule21': ctrl.Rule(dirtiness['high'] & dish_quantity['few'] & water_hardness['hard'],
                                [wash_time['medium'], detergent['medium'], water_temperature['high']]),
            'rule22': ctrl.Rule(dirtiness['high'] & dish_quantity['moderate'] & water_hardness['soft'],
                                [wash_time['medium'], detergent['high'], water_temperature['medium']]),
            'rule23': ctrl.Rule(dirtiness['high'] & dish_quantity['moderate'] & water_hardness['moderate'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
            'rule24': ctrl.Rule(dirtiness['high'] & dish_quantity['moderate'] & water_hardness['hard'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
            'rule25': ctrl.Rule(dirtiness['high'] & dish_quantity['many'] & water_hardness['soft'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
            'rule26': ctrl.Rule(dirtiness['high'] & dish_quantity['many'] & water_hardness['moderate'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
            'rule27': ctrl.Rule(dirtiness['high'] & dish_quantity['many'] & water_hardness['hard'],
                                [wash_time['long'], detergent['high'], water_temperature['high']]),
        }

        # Control System Setup
        dishwasher_ctrl = ctrl.ControlSystem(self.rules.values())
        dishwasher_sim = ctrl.ControlSystemSimulation(dishwasher_ctrl)

        return dishwasher_sim

    def wash(self):
        print('[*] Activating Fuzzy Dishwasher 3000...')
        dishwasher_sim = self.initrialize()
        time.sleep(1)
        print('[*] Done.')

        # Set input values
        print(f'[*] Current status:\n\t-dirtness:{self.dirtiness}\n\t-dish quantity:{self.dish_quantity}\n\t-water hardness:{self.water_hardness}')
        dishwasher_sim.input['dirtiness'] = self.dirtiness
        dishwasher_sim.input['dish_quantity'] = self.dish_quantity
        dishwasher_sim.input['water_hardness'] = self.water_hardness
        time.sleep(1)

        # Perform computation
        print('[*] Performing computation...')
        dishwasher_sim.compute()
        time.sleep(1)
        
        # Get outputs
        print(f"[*] Recommended Wash Time: {round(dishwasher_sim.output['wash_time'], 1)} minutes")
        print(f"[*] Recommended Detergent Amount: {round(dishwasher_sim.output['detergent'], 1)} units")
        print(f"[*] Recommended Water Temperature: {round(dishwasher_sim.output['water_temperature'], 1)} °C")
        time.sleep(1)

        # :)
        print('[*] Starting dishwasher...')
        progress_bar = [' \\ ', ' | ', ' / ', '---']
        for i in range(int(round(dishwasher_sim.output['wash_time'], 1))):
            print(f'\r[*] Washing ' + progress_bar[i%4], end='')
            time.sleep(0.5)


        print('\r[*] Complete :)               ')


if __name__ == '__main__':
    print('=========Fuzzy Dishwasher 3000=========')
    random.seed(time.time())
    dirtiness = round(random.uniform(0, 5), 1)
    dish_quantity = random.randint(0, 10)
    water_hardness = round(random.uniform(0, 10), 1)

    mywasher = washer(dirtiness, dish_quantity, water_hardness)
    mywasher.wash()

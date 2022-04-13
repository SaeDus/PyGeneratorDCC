from random import *
from textwrap import dedent

separator = '*' * 80
file_separator = '-' * 80


class CharacterSheet(object):

    def __init__(self, name, do_gen, load_stats):

        self.name = ""
        self.alignment = "Lawful / Neutral / Chaotic"
        self.occupation = ""
        self.hit_points = 0
        self.ability_scores = {
            'Strength': 0,
            'Agility': 0,
            'Stamina': 0,
            'Personality': 0,
            'Intelligence': 0,
            'Luck': 0
        }
        self.score_modifiers = {
            'Strength': 0,
            'Agility': 0,
            'Stamina': 0,
            'Personality': 0,
            'Intelligence': 0,
            'Luck': 0
        }
        self.lucky_roll = ""
        self.languages = "Common"
        self.weapon = ""
        self.equipment = ""
        self.trade_goods = ""
        self.purse = {'gp': 0, 'sp': 0, 'cp': 0}

        if do_gen:

            self.__generate_random_character()

            self.name = name

            self.equipment = equipment.get(roll_die(1, 24))

            self.purse['cp'] = roll_die(5, 12)

        else:

            self.__load_character_details(load_stats)

    def __generate_random_character(self):

        self.__generate_ability_scores()
        self.__set_score_modifiers()
        self.__roll_health()
        self.__generate_occupation()
        self.__generate_luck_roll()
        self.__generate_languages()

    def __generate_ability_scores(self):

        for score in self.ability_scores:

            self.ability_scores[score] = roll_die(3, 6)

    def __set_score_modifiers(self):

        for score in self.ability_scores:

            self.score_modifiers[score] = score_modifiers.get(self.ability_scores.get(score))

    def __roll_health(self):

        self.hit_points = roll_die(1, 4)

        self.hit_points += self.score_modifiers.get('Stamina')

        if self.hit_points <= 0:
            self.hit_points = 1

    def __generate_occupation(self):

        selected_occupation = roll_die(1, 100)

        self.occupation = occupation.get(selected_occupation)

        self.weapon = trained_weapon.get(selected_occupation)

        if selected_occupation == 62:
            self.purse['gp'] = 5
            self.purse['sp'] = 10
            self.purse['cp'] += 200

        elif selected_occupation == 63:
            self.purse['sp'] = 20

        elif selected_occupation == 76:
            self.purse['gp'] = 4
            self.purse['sp'] = 14
            self.purse['cp'] += 27

        elif selected_occupation == 91:
            self.purse['cp'] += 100

        else:

            self.trade_goods = trade_goods.get(selected_occupation)

    def __generate_luck_roll(self):

        luck_roll = roll_die(1, 30) + self.score_modifiers.get('Luck')

        if luck_roll > 30:
            luck_roll -= 30

        elif luck_roll < 1:
            luck_roll += 30

        self.lucky_roll = luck_score.get(luck_roll)

    def __generate_languages(self):

        if self.score_modifiers.get('Intelligence') <= 0:
            return

        for i in range(self.score_modifiers.get('Intelligence')):

            self.languages += ", " + get_random_language()

    def __load_character_details(self, data):

        self.name = data[0].removeprefix('Name: ')
        self.alignment = data[1].removeprefix('Alignment: ')
        self.occupation = data[2].removeprefix('Occupation: ')
        self.weapon = data[3].removeprefix('Weapon: ')
        self.hit_points = data[4].removeprefix('Hit Points: ')

        score_index = 5

        for score in self.ability_scores:

            load_scores = data[score_index].removeprefix(score.title() + ": ").split()

            self.ability_scores[score] = int(load_scores[0])

            self.score_modifiers[score] = int(load_scores[1].removeprefix('(').removesuffix(')'))

            score_index += 1

        self.lucky_roll = data[11].removeprefix('Lucky Roll: ')
        self.equipment = data[12].removeprefix('Equipment: ')
        self.trade_goods = data[13].removeprefix('Trade Goods: ')
        self.languages = data[14].removeprefix('Known Languages: ')

        purse_string = data[15].removeprefix('Purse: ').split()

        self.purse['gp'] = int(purse_string[0].removesuffix('gp'))
        self.purse['sp'] = int(purse_string[1].removesuffix('sp'))
        self.purse['cp'] = int(purse_string[2].removesuffix('cp'))

    def get_character_details(self):

        purse_value = str(self.purse.get('gp')) + "gp " + \
            str(self.purse.get('sp')) + "sp " + \
            str(self.purse.get('cp')) + "cp"

        return dedent(f"""
            Name: {self.name}
            Alignment: {self.alignment}
            Occupation: {self.occupation}
            Weapon: {self.weapon}
            Hit Points: {self.hit_points}
            Strength: {self.ability_scores.get('Strength')} ({self.score_modifiers.get('Strength')})
            Agility: {self.ability_scores.get('Agility')} ({self.score_modifiers.get('Agility')})
            Stamina: {self.ability_scores.get('Stamina')} ({self.score_modifiers.get('Stamina')})
            Personality: {self.ability_scores.get('Personality')} ({self.score_modifiers.get('Personality')})
            Intelligence: {self.ability_scores.get('Intelligence')} ({self.score_modifiers.get('Intelligence')})
            Luck: {self.ability_scores.get('Luck')} ({self.score_modifiers.get('Luck')})
            Lucky Roll: {self.lucky_roll}
            Equipment: {self.equipment}
            Trade Goods: {self.trade_goods}
            Known Languages: {self.languages}
            Purse: {purse_value}
            """)

    def get_character_info(self, index):

        if index == 0:
            return self.name.replace("\n", "")
        elif index == 1:
            return str(self.hit_points)
        elif index == 2:
            return self.occupation.replace("\n", "")
        elif index == 3:
            return self.alignment.replace("\n", "")
        elif index == 4:
            return str(self.ability_scores.get('Strength'))
        elif index == 5:
            return str(self.score_modifiers.get('Strength'))
        elif index == 6:
            return str(self.ability_scores.get('Agility'))
        elif index == 7:
            return str(self.score_modifiers.get('Agility'))
        elif index == 8:
            return str(self.ability_scores.get('Stamina'))
        elif index == 9:
            return str(self.score_modifiers.get('Stamina'))
        elif index == 10:
            return str(self.ability_scores.get('Personality'))
        elif index == 11:
            return str(self.score_modifiers.get('Personality'))
        elif index == 12:
            return str(self.ability_scores.get('Intelligence'))
        elif index == 13:
            return str(self.score_modifiers.get('Intelligence'))
        elif index == 14:
            return str(self.ability_scores.get('Luck'))
        elif index == 15:
            return str(self.score_modifiers.get('Luck'))
        elif index == 16:
            return self.lucky_roll.replace("\n", "")
        elif index == 17:
            return self.weapon.replace("\n", "")
        elif index == 18:
            return self.equipment.replace("\n", "")
        else:
            return self.trade_goods.replace("\n", "")


# region FUNCTIONS

def roll_die(rolls, faces):

    total_roll = 0

    for i in range(rolls):

        total_roll += randint(1, faces)

    return total_roll


def roll_ammo(weapon_name):

    if 'sling' in weapon_name.lower():
        ammo_type = 'Rocks'

    elif 'dart' in weapon_name.lower():
        ammo_type = 'Darts'

    else:
        ammo_type = 'Arrows'

    return f'{weapon_name} (x{roll_die(1, 6)} {ammo_type})'


def get_random_language():

    roll = roll_die(1, 100)

    if 1 <= roll <= 20:
        return "Alignment"

    elif 21 <= roll <= 30:
        return "Dwarf"

    elif 31 <= roll <= 35:
        return "Elf"

    elif 36 <= roll <= 40:
        return "Halfling"

    elif 41 <= roll <= 45:
        return "Gnome"

    elif 46 <= roll <= 47:
        return "Bugbear"

    elif 48 <= roll <= 57:
        return "Goblin"

    elif 58 <= roll <= 60:
        return "Gnoll"

    elif 61 <= roll <= 65:
        return "Hobgoblin"

    elif 66 <= roll <= 75:
        return "Kobold"

    elif 76 <= roll <= 80:
        return "Lizard Man"

    elif roll == 81:
        return "Minotaur"

    elif 82 <= roll <= 83:
        return "Ogre"

    elif 84 <= roll <= 93:
        return "Orc"

    elif 94 <= roll <= 99:
        return "Troglodyte"

    else:
        return "Giant"

# endregion


# region TABLES

score_modifiers = {
    3: -3,
    4: -2,
    5: -2,
    6: -1,
    7: -1,
    8: -1,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 1,
    14: 1,
    15: 1,
    16: 2,
    17: 2,
    18: 3
}

luck_score = {
    1: 'Harsh winter: All attack rolls',
    2: 'The bull: Melee attack rolls',
    3: 'Fortunate date: Missile fire attack rolls',
    4: 'Raised by wolves: Unarmed attack rolls',
    5: 'Conceived on horseback: Mounted attack rolls',
    6: 'Born on the battlefield: Damage rolls',
    7: 'Path of the bear: Melee damage rolls',
    8: 'Hawkeye: Missile fire damage rolls',
    9: 'Pack hunter: Attack and damage rolls for 0-level starting weapon',
    10: 'Born under the loom: Skill checks (including thief skills)',
    11: 'Fox\'s cunning: Find/disable traps',
    12: 'Four-leafed clover: Find secret doors',
    13: 'Seventh son: Spell checks',
    14: 'The raging storm: Spell damage',
    15: 'Righteous heart: Turn unholy checks',
    16: 'Survived the plague: Magical healing',
    17: 'Lucky sign: Saving throws',
    18: 'Guardian angel: Savings throws to escape traps',
    19: 'Survived a spider bite: Saving throws against poison',
    20: 'Struck by lightning: Reflex saving throws',
    21: 'Lived through famine: Fortitude saving throws',
    22: 'Resisted temptation: Willpower saving throws',
    23: 'Charmed house: Armor Class',
    24: 'Speed of the cobra: Initiative',
    25: 'Bountiful harvest: Hit points (applies at each level)',
    26: 'Warrior\'s arm: Critical hit tables',
    27: 'Unholy house: Corruption rolls',
    28: 'The Broken Star: Fumbles',
    29: 'Birdsong: Number of languages',
    30: 'Wild child: Speed (each +1/-1 = +5\'/-5\' speed)'
}

farmer_type = {
    1: 'Potato Farmer', 2: 'Wheat Farmer', 3: 'Turnip Farmer', 4: 'Corn Farmer',
    5: 'Rice Farmer', 6: 'Parsnip Farmer', 7: 'Radish Farmer', 8: 'Rutabaga Farmer'
}

farm_animal = {1: 'Sheep', 2: 'Goat', 3: 'Cow', 4: 'Duck', 5: 'Goose', 6: 'Mule'}

cart_contents = {1: 'Tomatoes', 2: 'Nothing', 3: 'Straw', 4: 'Your Dead', 5: 'Dirt', 6: 'Rocks'}

occupation = {
    1: 'Alchemist',                     2: 'Animal trainer',                3: 'Armorer',
    4: 'Astrologer',                    5: 'Barber',                        6: 'Beadle',
    7: 'Beekeeper',                     8: 'Blacksmith',                    9: 'Butcher',
    10: 'Caravan guard',                11: 'Cheesemaker',                  12: 'Cobbler',
    13: 'Confidence artist',            14: 'Cooper',                       15: 'Costermonger',
    16: 'Cutpurse',                     17: 'Ditch digger',                 18: 'Dock worker',
    19: 'Dwarven apothecarist',         20: 'Dwarven blacksmith',           21: 'Dwarven chest-maker',
    22: 'Dwarven herder',               23: 'Dwarven miner',                24: 'Dwarven miner',
    25: 'Dwarven mushroom-farmer',      26: 'Dwarven rat-catcher',          27: 'Dwarven stonemason',
    28: 'Dwarven stonemason',           29: 'Elven artisan',                30: 'Elven barrister',
    31: 'Elven chandler',               32: 'Elven falconer',               33: 'Elven forester',
    34: 'Elven forester',               35: 'Elven glassblower',            36: 'Elven navigator',
    37: 'Elven sage',                   38: 'Elven sage',                   39: farmer_type.get(roll_die(1, 8)),
    40: farmer_type.get(roll_die(1, 8)), 41: farmer_type.get(roll_die(1, 8)), 42: farmer_type.get(roll_die(1, 8)),
    43: farmer_type.get(roll_die(1, 8)), 44: farmer_type.get(roll_die(1, 8)), 45: farmer_type.get(roll_die(1, 8)),
    46: farmer_type.get(roll_die(1, 8)), 47: farmer_type.get(roll_die(1, 8)), 48: 'Fortune-teller',
    49: 'Gambler',                      50: 'Gongfarmer',                   51: 'Grave digger',
    52: 'Grave digger',                 53: 'Guild beggar',                 54: 'Guild beggar',
    55: 'Halfling chicken butcher',     56: 'Halfling dyer',                57: 'Halfling dyer',
    58: 'Halfling glovemaker',          59: 'Halfling gypsy',               60: 'Halfling haberdasher',
    61: 'Halfling mariner',             62: 'Halfling moneylender',         63: 'Halfling trader',
    64: 'Halfling vagrant',             65: 'Healer',                       66: 'Herbalist',
    67: 'Herder',                       68: 'Hunter',                       69: 'Hunter',
    70: 'Indentured servant',           71: 'Jester',                       72: 'Jeweler',
    73: 'Locksmith',                    74: 'Mendicant',                    75: 'Mercenary',
    76: 'Merchant',                     77: 'Miller/baker',                 78: 'Minstrel',
    79: 'Noble',                        80: 'Orphan',                       81: 'Ostler',
    82: 'Outlaw',                       83: 'Rope maker',                   84: 'Scribe',
    85: 'Shaman',                       86: 'Slave',                        87: 'Smuggler',
    88: 'Soldier',                      89: 'Squire',                       90: 'Squire',
    91: 'Tax collector',                92: 'Trapper',                      93: 'Trapper',
    94: 'Urchin',                       95: 'Wainwright',                   96: 'Weaver',
    97: 'Wizard\'s apprentice',         98: 'Woodcutter',                   99: 'Woodcutter',
    100: 'Woodcutter'
}

trained_weapon = {
    1: 'Staff',                         2: 'Club',                          3: 'Hammer (as club)',
    4: 'Dagger',                        5: 'Razor (as dagger)',             6: 'Staff',
    7: 'Staff',                         8: 'Hammer (as club)',              9: 'Cleaver (as axe)',
    10: 'Short sword',                  11: 'Cudgel (as staff)',            12: 'Awl (as dagger)',
    13: 'Dagger',                       14: 'Crowbar (as club)',            15: 'Knife (as dagger)',
    16: 'Dagger',                       17: 'Shovel (as staff)',            18: 'Pole (as staff)',
    19: 'Cudgel (as staff)',            20: 'Hammer (as club)',             21: 'Chisel (as dagger)',
    22: 'Staff',                        23: 'Pick (as club)',               24: 'Pick (as club)',
    25: 'Shovel (as staff)',            26: 'Club',                         27: 'Hammer',
    28: 'Hammer',                       29: 'Staff',                        30: roll_ammo('Quill (as dart)'),
    31: 'Scissors (as dagger)',         32: 'Dagger',                       33: 'Staff',
    34: 'Staff',                        35: 'Hammer (as club)',             36: roll_ammo('Shortbow'),
    37: 'Dagger',                       38: 'Dagger',                       39: 'Pitchfork (as spear)',
    40: 'Pitchfork (as spear)',         41: 'Pitchfork (as spear)',         42: 'Pitchfork (as spear)',
    43: 'Pitchfork (as spear)',         44: 'Pitchfork (as spear)',         45: 'Pitchfork (as spear)',
    46: 'Pitchfork (as spear)',         47: 'Pitchfork (as spear)',         48: 'Dagger',
    49: 'Club',                         50: 'Trowel (as dagger)',           51: 'Shovel (as staff)',
    52: 'Shovel (as staff)',            53: roll_ammo('Sling'),             54: roll_ammo('Sling'),
    55: 'Hand axe',                     56: 'Staff',                        57: 'Staff',
    58: 'Awl (as dagger)',              59: roll_ammo('Sling'),             60: 'Scissors (as dagger)',
    61: 'Knife (as dagger)',            62: 'Short sword',                  63: 'Short sword',
    64: 'Club',                         65: 'Club',                         66: 'Club',
    67: 'Staff',                        68: roll_ammo('Shortbow'),          69: roll_ammo('Shortbow'),
    70: 'Staff',                        71: roll_ammo('Dart'),              72: 'Dagger',
    73: 'Dagger',                       74: 'Club',                         75: 'Longsword',
    76: 'Dagger',                       77: 'Club',                         78: 'Dagger',
    79: 'Longsword',                    80: 'Club',                         81: 'Staff',
    82: 'Short sword',                  83: 'Knife (as dagger)',            84: roll_ammo('Dart'),
    85: 'Mace',                         86: 'Club',                         87: roll_ammo('Sling'),
    88: 'Spear',                        89: 'Longsword',                    90: 'Longsword',
    91: 'Longsword',                    92: roll_ammo('Sling'),             93: roll_ammo('Sling'),
    94: 'Stick (as club)',              95: 'Club',                         96: 'Dagger',
    97: 'Dagger',                       98: 'Handaxe',                      99: 'Handaxe',
    100: 'Handaxe'
}

trade_goods = {
    1: 'Oil, 1 flask',                  2: 'Pony',                          3: 'Iron helmet',
    4: 'Spyglass',                      5: 'Scissors',                      6: 'Holy symbol',
    7: 'Jar of honey',                  8: 'Steel tongs',                   9: 'Side of beef',
    10: 'Linen, 1 yard',                11: 'Stinky cheese',                12: 'Shoehorn',
    13: 'Quality cloak',                14: 'Barrel',                       15: 'Fruit',
    16: 'Small chest',                  17: 'Fine dirt, 1lb.',              18: '1 late RPG book',
    19: 'Steel vial',                   20: 'Mithril, 1 oz.',               21: 'Wood, 10lbs.',
    22: farm_animal.get(roll_die(1, 6)), 23: 'Lantern',                     24: 'Lantern',
    25: 'Sack',                         26: 'Net',                          27: 'Fine stone, 10 lbs.',
    28: 'Fine stone, 10 lbs.',          29: 'Clay, 1 lb.',                  30: 'Book',
    31: 'Candles, 20',                  32: 'Falcon',                       33: 'Herbs, 1 lb.',
    34: 'Herbs, 1 lb.',                 35: 'Glass beads',                  36: 'Spyglass',
    37: 'Parchment and quill pen',      38: 'Parchment and quill pen',      39: farm_animal.get(roll_die(1, 6)),
    40: farm_animal.get(roll_die(1, 6)), 41: farm_animal.get(roll_die(1, 6)), 42: farm_animal.get(roll_die(1, 6)),
    43: farm_animal.get(roll_die(1, 6)), 44: farm_animal.get(roll_die(1, 6)), 45: farm_animal.get(roll_die(1, 6)),
    46: farm_animal.get(roll_die(1, 6)), 47: farm_animal.get(roll_die(1, 6)), 48: 'Tarot deck',
    49: 'Dice',                         50: 'Sack of night soil',           51: 'Trowel',
    52: 'Trowel',                       53: 'Crutches',                     54: 'Crutches',
    55: 'Chicken meat, 5 lbs.',         56: 'Fabric, 3 yards',              57: 'Fabric, 3 yards',
    58: 'Gloves, 4 pairs',              59: 'Hex doll',                     60: 'Fine suits, 3 sets',
    61: 'Sailcloth, 2 yards',           62: '5 gp, 10 sp, 200 cp',          63: '20 sp',
    64: 'Begging bowl',                 65: 'Holy water, 1 vial',           66: 'Herbs, 1 lb.',
    67: 'Herding dog',                  68: 'Deer pelt',                    69: 'Deer pelt',
    70: 'Locket',                       71: 'Silk clothes',                 72: 'Gem worth 20 gp',
    73: 'Fine tools',                   74: 'Cheese dip',                   75: 'Hide armor',
    76: '4 gp, 14 sp, 27 cp',           77: 'Flour, 1 lb.',                 78: 'Ukulele',
    79: 'Gold ring worth 10 gp',        80: 'Rag doll',                     81: 'Bridle',
    82: 'Leather armor',                83: 'Rope, 100\'',                  84: 'Parchment, 10 sheets',
    85: 'Herbs, 1 lb.',                 86: 'Strange-looking rock',         87: 'Waterproof sack',
    88: 'Shield',                       89: 'Steel helmet',                 90: 'Steel helmet',
    91: '100 cp',                       92: 'Badger pelt',                  93: 'Badger pelt',
    94: 'Begging bowl',                 95: cart_contents.get(roll_die(1, 6)), 96: 'Fine suit of clothes',
    97: 'Black grimoire',               98: 'Bundle of wood',               99: 'Bundle of wood',
    100: 'Bundle of wood'
}

equipment = {
    1: 'Backpack',              2: 'Candle',            3: 'Chain, 10\'',           4: 'Chalk, 1 piece',
    5: 'Chest, empty',          6: 'Crowbar',           7: 'Flask, empty',          8: 'Flint & steel',
    9: 'Grappling hook',        10: 'Hammer, small',    11: 'Holy symbol',          12: 'Holy water, 1 vial',
    13: 'Iron  spikes, each',   14: 'Lantern',          15: 'Mirror, hand-sized',   16: 'Oil, 1 flask',
    17: 'Pole, 10-foot',        18: 'Rations, per day', 19: 'Rope, 50\'',           20: 'Sack, large',
    21: 'Sack, small',          22: 'Thieves\' tools',  23: 'Torch, each',          24: 'Waterskin'
}

# endregion

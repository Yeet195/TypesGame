import pokebase as pb

# Types Constant
TYPES = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']

WEAKNESSCHART = [
    [0, 2, 1],  # Normal
    [5, 5, 1],  # fighting
    [3, 3, 0],  # flying
    [2, 4, 1],  # poison
    [5, 2, 1],  # ground  
    [4, 3, 0],  # rock
    [3, 7, 0],  # bug
    [2, 1, 1],  # ghost
    [3, 3, 0],  # steel
    [4, 4, 0],  # fire
    [3, 3, 0],  # water
    [3, 7, 0],  # grass
    [2, 3, 0],  # electric
    [2, 2, 0],  # psychic
    [4, 4, 0],  # ice
    [1, 1, 1],  # dragon
    [2, 3, 0],  # dark
    [3, 3, 0]]  # fairy

# Get multiplyers for types
def type_multiplier(attack: str, defense: str) -> float:
    atk_type = pb.type_(attack)
    if defense in [t.name for t in atk_type.damage_relations.no_damage_to]:
        return 0.0
    elif defense in [t.name for t in atk_type.damage_relations.half_damage_to]:
        return 0.5
    elif defense in [t.name for t in atk_type.damage_relations.double_damage_to]:
        return 2.0
    else:
        return 1.0
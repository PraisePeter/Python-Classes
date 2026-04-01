def create_character(character_name, strength, intelligence, charisma):
    full_dot = '●'
    empty_dot = '○'

    if not isinstance(character_name, str):
        return "The character name should be a string"
    elif character_name.strip() == "":
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]

    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
        elif stat < 1:
            return "All stats should be no less than 1"
        elif stat > 4:
            return "All stats should be no more than 4"
    sum_of_stats = strength + intelligence + charisma
    if sum_of_stats != 7:
        return "The character should start with 7 points"

    str_bar = full_dot * strength + empty_dot * (10 - strength)
    int_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_bar = full_dot * charisma + empty_dot * (10 - charisma)
    return (f"{character_name}\n"
            f"STR {str_bar}\n"
            f"INT {int_bar}\n"
            f"CHA {cha_bar}"
            )


print(create_character('ren', 4, 2, 1))

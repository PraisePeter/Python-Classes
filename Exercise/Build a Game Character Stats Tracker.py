"""

Build a Game Character Stats Tracker
In this lab, you'll build a game character stats tracker. The program will allow you to create a character with specific attributes, update those attributes, and retrieve the current stats of the character.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

Create a class named GameCharacter that represents a game character and manages character stats.

When instantiated, a new GameCharacter object should have the following attributes:

_name set to the string given at the moment of the instantiation.
_health set to 100.
_mana set to 50.
_level set to 1.
Create a name property for read-only access to the character's name.

For the health property:

Define a getter that returns the current health.
Define a setter that prevents health from being set below 0, and caps the health at 100.
For the mana property:

Define a getter that returns the current mana.
Define a setter that prevents mana from being set below 0, and caps the mana at 50.
Create a getter for level to return the character's current level.

Define a method named level_up that:

Increases the character's level by 1.
Resets health to 100 and mana to 50 using their corresponding property setters.
Prints a message in the form of <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
Define a __str__ method that returns a formatted string including:

The character's name.
The character's level.
The character's current health.
The character's current mana.
For example, a character named Kratos, right after the instantiation, should be represented as the following:

Name: Kratos
Level: 1
Health: 100
Mana: 50
Usage example
hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
Tests:
Failed:1. You should have a GameCharacter class.
Failed:2. You should have an __init__ method in the GameCharacter class.
Failed:3. The __init__ method should have two parameters, with the first being self.
Failed:4. You should set self._name to the string given at the moment of instantiation inside the __init__ method.
Failed:5. You should assign 100 to self._health inside the __init__ method.
Failed:6. You should assign 50 to self._mana inside the __init__ method.
Failed:7. You should assign 1 to self._level inside the __init__ method.
Failed:8. You should have a name method in the GameCharacter class.
Failed:9. The name method should have only one parameter, self.
Failed:10. You should return self._name in the name method.
Failed:11. The name method should have a @property decorator.
Failed:12. You should have a health method in the GameCharacter class.
Failed:13. The health method should have only one parameter, self.
Failed:14. You should return self._health in the health method.
Failed:15. The health method should have a @property decorator.
Failed:16. You should create a health setter method.
Failed:17. The health setter method should have a @health.setter decorator.
Failed:18. The health setter method should have two parameters, with the first being self.
Failed:19. You should set self._health to 0 if the value given to the health setter is less than 0.
Failed:20. You should set self._health to 100 if the value given to the health setter is greater than 100.
Failed:21. You should set self._health to the value given to the health setter when the value is between 0 and 100.
Failed:22. You should have a mana method in the GameCharacter class.
Failed:23. The mana method should have only one parameter, self.
Failed:24. You should return self._mana in the mana method.
Failed:25. The mana method should have a @property decorator.
Failed:26. You should create a mana setter method.
Failed:27. The mana setter method should have a @mana.setter decorator.
Failed:28. The mana setter method should have two parameters, with the first being self.
Failed:29. You should set self._mana to 0 if the value given to the mana setter is less than 0.
Failed:30. You should set self._mana to 50 if the value given to the mana setter is greater than 50.
Failed:31. You should set self._mana to the value given to the mana setter if the value is between 0 and 50.
Failed:32. You should have a level method in the GameCharacter class.
Failed:33. The level method should have only one parameter, self.
Failed:34. You should return self._level in the level method.
Failed:35. The level method should have a @property decorator.
Failed:36. You should have a level_up method in the GameCharacter class.
Failed:37. The level_up method should have only one parameter, self.
Failed:38. You should increase self._level by 1 in the level_up method.
Failed:39. You should set self.health to 100 in the level_up method.
Failed:40. You should set self.mana to 50 in the level_up method.
Failed:41. The level_up method should print <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
Failed:42. You should have a __str__ method in the GameCharacter class.
Failed:43. The __str__ method should have only one parameter, self.
Failed:44. Your __str__ method should return a string with the character's stats using the provided format.

"""


class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health_values):
        if health_values < 0:
            self._health = 0
        elif health_values > 100:
            self._health = 100
        else:
            self._health = health_values

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana_values):
        if mana_values < 0:
            self._mana = 0
        elif mana_values > 50:
            self._mana = 50
        else:
            self._mana = mana_values

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")

    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"


hero = GameCharacter('Kratos')
print(hero)
hero.health -= 30
hero.mana -= 10
print(hero)

hero.level_up()
print(hero)

"""

Step 1
In this workshop, you are going to build a salary tracking system for employees.

Start by creating a class named Employee. Inside it create an __init__ method with self, name, and level parameters. Within the __init__ method, assign name and level to the instance attributes with the same name.

Ans:
class Employee:
    def __init__ (self, name, level):
        self.name = name
        self.level = level


Step 2
Now create an instance of the Employee class passing in the strings Charlie Brown and trainee. Assign the instance to a variable named charlie_brown.

ANS:

charlie_brown = Employee("Charlie Brown", "trainee")


Step 3
In a previous lesson, you learned that an attribute prefixed with a single underscore is meant for internal use by convention.

Modify both name and level attributes into _name and _level, since these are not supposed to be modified from outside their class.

Note that this does not prevent the attribute from being accessed or modified outside the class. Also, in Python there's always a way to access private attributes (prefixed with a double underscore) as well.

ANS:

def __init__(self, name, level):
        self._name = name
        self._level = level


Step 4
Add a __str__ method to the Employee class. Make it return an f-string with the format name: level, replacing name and level with the corresponding attributes.

After that, print charlie_brown to the console.

ANS:

        self._level = level

    def __str__ (self):
        return f"{self._name}: {self._level}"

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)


Step 5
The @property decorator is used in Python to turn a method into a property. It is typically used to define getter methods, which are methods used to retrieve the value of an attribute:

Example Code
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person('Alice')
print(p.name)  # Alice
Create a method named name with a self parameter and decorate it with @property. Inside the method, return self._name.

ANS:

    def __str__(self):
        return f'{self._name}: {self._level}'

    @property
    def name(self):
        return self._name


Step 6
Now that you defined a getter for name, you can access the _name attribute through the name property. So print charlie_brown.name to the console.

ANS:

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown.name)


Step 7
Following what you did in the previous steps, create a getter for the _level attribute.

ANS:

    @property
    def level(self):
        return self._level



Step 8
Now print charlie_brown.level to the console.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(charlie_brown.name)
print(charlie_brown.level)


Step 9
Now that you have getters for both _name and _level attributes, update the string returned by __str__ to use self.name and self.level. This will call the getters instead of directly accessing the attributes.

ANS:
    def __str__(self):
        return f'{self.name}: {self.level}'


Step 10
Now remove the last two print calls.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)


Step 11
The __repr__ method is a special method that is supposed to return a string representation of the object that can be used to instantiate it.

For example, the __repr__ method of Employee('Charlie', 'developer') should return the string Employee('Charlie', 'developer'), which is the same string used to create the object.

Give your Employee class a __repr__ method with a self parameter, and make it return a string that can be used to instantiate the object.

ANS:
def __repr__(self):
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"


Step 12
The __repr__ method is called under the hood when you call the repr function. To see it in action, print the result of calling repr(charlie_brown) at the bottom of your code.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(repr(charlie_brown))


Step 13
Remove the last print call from your code.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)


Step 14
Now it's time to add some validation to the __init__ method. At the beginning of the method, create an if statement that checks if either name or level are not instances of str.

Inside the if statement, raise a TypeError with the message 'name' and 'level' attribute must be of type 'str'.

ANS:

    def __init__(self, name, level):
        if not isinstance (name, str) or not isinstance (level, str):
            raise TypeError ("'name' and 'level' attribute must be of type 'str'.")
        self._name = name
        self._level = level


Step 15
Create a class attribute named _base_salaries and assign it the following dictionary:

Example Code
{
    'trainee': 1000,
    'junior': 2000,
    'mid-level': 3000,
    'senior': 4000
}

ANS:
class Employee:
    _base_salaries = {
    'trainee': 1000,
    'junior': 2000,
    'mid-level': 3000,
    'senior': 4000
}


Step 16
The level used to instantiate an employee should be chosen among specific levels. You'll use _base_salaries to validate the level and set the right salary for the employee.

After your existing if statement, create another if that checks if level is not in Employee._base_salaries.

Inside the new if statement, raise a ValueError with the message Invalid value '{level}' for 'level' attribute., where {level} should be replaced by the value of the level argument.

ANS:
 elif level not in Employee._base_salaries:
            raise ValueError (f"Invalid value '{level}' for 'level' attribute.")


Step 17
Finally, at the bottom of the __init__ method, set the _salary attribute to the value corresponding to level inside the _base_salaries dictionary.

ANS:

        self._salary = Employee._base_salaries[level]


Step 18
Now that you have a new attribute, you're going to create a getter for it.

Create a method named salary with a self parameter and use the @property decorator on it. Inside the method, return self._salary.

ANS:
    @property
    def salary(self):
        return self._salary


Step 19
At the bottom of your code, use an f-string to print Base salary: $ followed by the amount of charlie_brown's salary.

ANS:

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')


Step 20
A setter is a method used to set the value of an attribute, allowing for validation checks and restrictions. You can create a setter using the @propertyName.setter decorator, where propertyName should match the name of the property to set:

Example Code
class Person:
    def __init__(self, name):
        self.name = name  # Calling the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p = Person('Alice')
p.name = 'Abigail' # Calls the setter
print(p.name) # Abigail
After your getter method, create a name method with parameters self and new_name. Decorate the method with @name.setter. Inside the method, set self._name to new_name.

ANS:
    @name.setter
    def name(self, new_name):
        self._name = new_name


Step 21
Now that the name setter is created, update __init__ to use self.name = name instead of self._name = name. This delegates name assignment through the setter, and validation will be added to it in the next step.

Also, adjust the if condition to only check level, and update the TypeError message accordingly:

ANS:
 def __init__(self, name, level):
        if not isinstance (level, str):
            raise TypeError("'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self.name = name


Step 22
As you learned in a previous lesson, a setter offers a way to control how an attribute can be modified. To ensure that new_name is the right type, create an if statement that raises a TypeError with the message 'name' must be a string. when new_name is not an instance of str.

ANS:
    @name.setter
    def name(self, new_name):
        if not isinstance (new_name, str):
            raise TypeError ("'name' must be a string.")


Step 23
Right after setting the _name attribute to new_name, print 'name' updated to 'new_name'., where new_name should be replaced by the new value of _name.

ANS:
        self._name = new_name
        print(f"'name' updated to '{self._name}'.")


Step 24
Now you have a setter method for the _name attribute that exposes the name property.

So try to update charlie_brown's name to a different name as you would normally do with any attribute. This will call the setter method under the hood.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.name = 'Charles Brown'
print(charlie_brown)


Step 25
Feel free to set the name property to something that is not a string to see the validation process in action. After that, restore charlie_brown's name by removing any line of code that changes its name.

ANS:
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')


Step 26
Now you'll create a setter for the _level attribute. Create a method named level with parameters self and new_level. Decorate the method with @level.setter.

Inside the method, set self._level to new_level.

ANS:
   @level.setter
    def level(self, new_level):
        self._level = new_level



Step 27
Now that the level setter is created, update __init__ to use self.level = level instead of self._level = level. This delegates level assignment through the setter, and validation will be added to it in the next step.

Also, remove the if not isinstance(level, str) check from __init__ since the setter will handle that validation in the next step.

ANS:
def __init__(self, name, level):
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self.name = name
        self.level = level
        self._salary = Employee._base_salaries[level]


Step 28
To ensure that new_level is the right type, create an if statement that raises a TypeError with the message 'level' must be a string. when new_level is not an instance of str.

ANS:
    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, str):
            raise TypeError ("'level' must be a string.")


Step 29
Now that the level setter handles the validation for invalid levels, remove the if level not in Employee._base_salaries check from __init__. This will be handled by the setter in the next step.

ANS:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self._salary = Employee._base_salaries[level]


Step 30
The new level cannot be set without checking if it's a valid level. After the isinstance check, create an if statement that raises a ValueError when new_level is not a key of Employee._base_salaries.

For the error message, use Invalid value '{new_level}' for 'level' attribute., where {new_level} should be replaced by the argument passed to the setter.

ANS:
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")


Step 31
After the existing if statements, create another one to raise a ValueError when new_level is already the selected level.

Note that _level doesn't exist yet during initialization, so use hasattr(self, '_level') to check if it exists before comparing. This avoids an AttributeError when the object is first created.

For the message, use '{level}' is already the selected level., where {level} should be replaced by the current level.

ANS:
if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")


Step 32
Finally, create a fourth if statement that raises a ValueError with the message Cannot change to lower level. when the base salary of the new level is less than the base salary of the current level.

Use hasattr(self, '_level') to avoid an AttributeError during initialization.

ANS:
       if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")


Step 33
When the level is modified, you need to update the salary as well.

Before setting self._level, set self._salary to the base salary for the new level.

ANS:
        self._salary = Employee._base_salaries[new_level]


Step 34
Complete the setter by printing '{name}' promoted to '{new_level}'. inside your method. Replace {name} and {new_level} with the employee's name and new level, respectively.

ANS:
        print(f"'{self.name}' promoted to '{new_level}'.")


Step 35
It's time to test your new setter. Try to assign invalid values such as a random string or the current level (trainee) to charlie_brown.level and see the error messages in the console.

Once you've done, remove the lines raising errors and set charlie_brown.level to the string junior.

ANS:

charlie_brown.level = "manager"
print(charlie_brown.level)  #VALUE ERROR

charlie_brown.level = "junior"
print(charlie_brown.level)



Step 36
Now you'll focus on coding a salary setter. After the salary getter, create a simple setter for the salary property that sets self._salary to the value passed to the method as its argument. After that, print Salary updated to $ followed by the new salary and a period.

You'll take care of validating the new salary in the next few steps.

ANS:
    @salary.setter
    def salary (self, new_salary):
        self._salary = new_salary
        print(f"Salary updated to ${new_salary}.")



Step 37
Now that the salary setter is created, update __init__ to call it instead of assigning directly to self._salary. Change self._salary = Employee._base_salaries[level] to self.salary = Employee._base_salaries[level].

ANS:
        self.level = level
        self.salary = Employee._base_salaries[level]



Step 38
At the beginning of your setter, create an if statement that raises a TypeError with the message 'salary' must be a number. when new_salary is not either an integer or a float.

ANS:
        if not isinstance(new_salary, int) and not isinstance(new_salary, float):
            raise TypeError("'salary' must be a number.")


Step 39
After your existing if statement, create another one for when the new salary is less than the base salary for the current level. Use hasattr(self, '_level') to avoid an AttributeError during initialization.

Inside the if statement, raise a ValueError with the message Salary must be higher than minimum salary $ followed by the base salary for the current level and a period.

ANS:

        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f"Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.")


Step 40
Finally, now that you have completed the salary setter, you can call it within the level setter.

Modify the line self._salary = Employee._base_salaries[new_level] so that it calls the salary setter instead of modifying directly the _salary attribute.

With that the salary tracker workshop is complete.

ANS:
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

"""

class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'
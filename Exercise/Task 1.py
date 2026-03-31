"""
Task:
. Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following
example: if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method.
"""
class Time:
    def __init__(self, seconds):
        self.seconds = seconds
    def convert_to_minutes(self):
        mins = self.seconds // 60
        secs = self.seconds % 60
        return f"{mins} : {secs:02d}"
    def convert_to_hours(self):
        hours = self.seconds // 3600
        remainder = self.seconds % 3600
        mins = remainder // 60
        secs = remainder % 60
        return f"{hours} : {mins:02d} : {secs:02d}"

t = Time(230)
print(t.convert_to_minutes())
print(t.convert_to_hours())


""" IMPORTANT: return f"{minutes}:{remaining_seconds:02d} 

Breakdown of :02d
: → starts the format specification
0 → pad with zeros instead of spaces
2 → minimum width of 2 digits
d → format as a decimal integer

"""
# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class IntakeForm:
    """Models a doctor's office intake form."""

    def __init__(self, name, dob, reason) -> None:
        self.name = name
        self.dob = dob
        self.reason = reason

    def __str__(self) -> str:
        return f"""Welcome to Dr. Acula's Office!
        Name: {self.name}
        Date of Birth: {self.dob}
        Reason for visit: {self.reason}
        """

patient1 = IntakeForm("Jonathan Harker", "1876-04-01", "Too much blood in my veins!")

print(patient1)
print(patient1.name)
class ProgrammingLanguage:

    def __init__(self, Field, Typing, Reflection, Year):
        self.Field = Field
        self.Typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def is_dynamic(self):
        if "Dynamic" in self.Typing:
            return True

    def __str__(self):
        return '{self.Field}, {self.Typing} Typing, Reflection = {self.Reflection}, First appeared in {self.Year}'.format(self=self)

def repr_(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def add_repr(cls):
    cls.__repr__ = repr_
    return cls


@add_repr
class Country:
    def __init__(self, name):
        self.nome = name


@add_repr
class Planet:
    def __init__(self, name):
        self.nome = name


brazil = Country('Brazilian')
united_kingdom = Country('English')

earth = Planet('Terra')
mars = Planet('Mars')

print(brazil)
print(united_kingdom)

print(earth)
print(mars)

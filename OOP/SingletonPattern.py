# Simple implementation of the Singleton Pattern

class SingletonMeta(type): # SingletonMeta metaclass controls the instantiation of 
    # the Singleton class to ensure only one instance is created across the application
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    #  Class Singleton only allows a single instance to be created
    def some_business_logic(self):
        # Your business logic here
        pass

class SingletonWithoutMеtaClass():
    #  Class Singleton allows several instances to be created
    def some_business_logic(self):
        # Your business logic here
        pass

# Testing using MetaClass
s1 = Singleton()
s2 = Singleton()
if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")

# Testing using class without meta class
s1 = SingletonWithoutMеtaClass()
s2 = SingletonWithoutMеtaClass()
if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")
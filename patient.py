class Patient:
    def __init__(self,name,family,code,age,gender):
        self.name=name
        self.family=family
        self.__code=code
        self.age=age
        self.gender=gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        name_validator(value)
        self.__name=value

    @property
    def family()

    

    def __repr__(self):
        return f"Patient({self.__dict__})"

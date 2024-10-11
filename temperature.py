class Temperature:
    def __init__(self,ceilius):
        self.__ceilius = ceilius
    def to_fahrenheint(self,ceilius):
        fahrenheint = ceilius * 9/5+32
    def get_celsius(self):
        return self.__ceilius
rature = Temperature(25)
fahrenheint = Temperature(77)
print(rature.get_ceilius())

class MusicalInstruments:
    numberOfKeys = 12
    
class StringInstrument(MusicalInstruments):
    typeOfWood = "Tonewood"
    
class Guitar(StringInstrument):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. It is made of {} and it has {} keys"\
            .format(self.numberOfStrings, self.typeOfWood, self.numberOfKeys))
        
        
guitar = Guitar()
# lib/dog.py

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Unknown", breed="Unknown"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            self._name = None
            print("Name must be string between 1 and 25 characters.")
        
        if self._name is not None:
            if breed in Dog.approved_breeds:
                self._breed = breed
            else:
                self._breed = None
                print("Breed must be in list of approved breeds.")
        else:
            self._breed = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

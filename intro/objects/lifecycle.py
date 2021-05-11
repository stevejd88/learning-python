class PartyAnimal:
  x=0

  # constructor
  def __init__(self):
    print('I am constructed')

  def party(self):
    self.x = self.x + 1
    print("So far", self.x)

  # destructor
  def __del__(self):
    print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
# below we overwrite the object an, which calls our destructor
an = 42
print('an contains', an)
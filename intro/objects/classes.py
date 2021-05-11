class PartyAnimal:
  x=0

  # self refers to an alias. Refers back to the instance of the class. "an" in this case
  # seems like "this" in JavaScript
  def party(self):
    self.x = self.x + 1
    print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()


print("Type" ,type(an))
print("Dir" ,dir(an))
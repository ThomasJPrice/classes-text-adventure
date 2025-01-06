class Item():
  def __init__(self, start_name, start_description):
    self.name = start_name
    self.description = start_description
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
    
  @property
  def description(self):
    return self._description
  
  @description.setter
  def description(self, new_description):
    self._description = new_description
    
  def describe(self):
    print(f'There is a {self.name} here.')
    print(f'{self.description}')
    print()
    
  def take(self, inventory):
    inventory.append(self.name)
    print(f'You take the {self.name}.')
    print()
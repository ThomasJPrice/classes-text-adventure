class Character():
  def __init__(self, start_name, start_description):
    self.name = start_name
    self.description = start_description
    self.conversation = None
    self.bribe_info = None
    self.bribe_item = None
  
  def describe(self):
    print(f'{self.name} is here!')
    print(f'{self.description}')
    print()
    
  @property
  def conversation(self):
    return self._conversation
  
  @conversation.setter
  def conversation(self, new_conversation):
    self._conversation = new_conversation
    
  def talk(self):
    if self._conversation is not None:
      print(f'{self.name} says: {self._conversation}')
    else:
      print(f'{self.name} does not want to talk to you.')
      
  @property
  def bribe_info(self):
    return self._bribe_info
  
  @bribe_info.setter
  def bribe_info(self, new_bribe_info):
    self._bribe_info = new_bribe_info
    
  @property
  def bribe_item(self):
    return self._bribe_item
  
  @bribe_item.setter
  def bribe_item(self, new_bribe_item):
    self._bribe_item = new_bribe_item
    
  def bribe(self, inventory):
    if self._bribe_info is not None:
      if self._bribe_item in inventory:
        print(f'{self.name} accepts your bribe and says: {self._bribe_info}')
        inventory.remove(self._bribe_item)
      else:
        print(f'{self.name} says: Your possessions are worthless.')  
      
    else:
      print(f'{self.name} does not want to be bribed.')
      
    print()


class Enemy(Character):
  count = 0
  
  def __init__(self, start_name, start_description):
    super().__init__(start_name, start_description)
    self.weakness = None
    
  @property
  def weakness(self):
    return self._weakness
  
  @weakness.setter
  def weakness(self, new_weakness):
    self._weakness = new_weakness
    
  def fight(self, inventory):
    if self._weakness is not None:
      if self._weakness in inventory:
        print(f'You defeated {self.name} with {self._weakness}')
      else:
        print(f'{self.name} is invincible!')
    else:
      print(f'{self.name} does not want to fight you.')
class BinarySearch(list):
  def __init__(self, length_of_list, step):
    self.list_of_numbers = range(0, length_of_list , step)
    list.__init__(self, self.list_of_numbers)
    self.length = len(self.list_of_numbers) - 1
    
  def search(self, search_element):
    start = 0 
    count = 0
    end = len(self.list_of_numbers) - 1
    output_dict = {}
    midpoint = (start + end)/2
    while True:
      if self.list_of_numbers[midpoint] < search_element:
        count +=1
        output_dict['count'] = count
        output_dict['index'] = self.list_of_numbers.index(search_element)
        midpoint = midpoint + 1
      elif self.list_of_numbers[midpoint] > search_element:
        count += 1
        output_dict['count'] = count
        output_dict['index'] = self.list_of_numbers.index(search_element)
        midpoint = midpoint - 1
      else:
        count = 1
        output_dict['count'] = 1
        output_dict['index'] = self.list_of_numbers[midpoint]
        return self.list_of_numbers[midpoint]
    return output_dict 
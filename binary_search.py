class BinarySearch(list):
  def __init__(self, length_of_list, step):
    self.list_of_numbers = range(0+step, length_of_list*step + 1  , step)
    list.__init__(self, self.list_of_numbers)
    self.length = len(self.list_of_numbers) - 1
    
  def search(self, search_element):
    start = 0 
    count = 0
    end = len(self.list_of_numbers) - 1
    output_dict = {'count':count, 'index':0 }
   
    if value not in self.list_of_numbers:
      output_dict['index'] = -1
      return output_dict
    else:
        while True:
           midpoint = (start + end)/2
           if self.list_of_numbers[start] == search_element:
               output_dict['index'] = start
               return output_dict
           elif self.list_of_numbers[end] == search_element:
               output_dict['index'] = end
               return output_dict
           elif self.list_of_numbers[midpoint] == search_element:
               output_dict['index'] == midpoint
               output_dict['count'] +=1
           else:
               if search_element <self.list_of_numbers[midpoint]:
                   count += 1
                   first = midpoint - 1
                   output_dict['index'] = self.list_of_numbers.index(search_element)
               else:
                   count += 1 
                   first = midpoint + 1 
                   output_dict['index'] = self.list_of_numbers.index(search_element)
return output_dict                   

                

            



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
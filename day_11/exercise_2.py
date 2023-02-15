''' 30  Days od Python - Day 11
Excercise 2: Level 2'''

# Number 1 
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens+=1
        else: 
             odds+=1
    return f" The numbers of evens are {evens}, \n The numbers of odds are {odds}"
print(evens_and_odds(100))

# Number 2
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact
print(factorial(6))

# Number 3
def is_empty(n):
  if len(n) == 0:
    check = 'Empty'
  else:
    check = 'Not empty'
  return check
print(is_empty(()))

# Number 4

# calculate_mean

def  calculate_mean(lst):
   num_lst = len(lst)
   add_lst = sum(lst)
   mean = add_lst / num_lst
   return mean
print(calculate_mean([1,2,3,4]))

# calculate median

def calculate_median(lst):
   lst.sort()
   len_list = len(lst)
   if len_list % 2 == 0:
      median = (lst[len_list // 2] + lst[len_list // 2 - 1]) / 2
      return median
   else:
      median = lst[len_list // 2]
      return median
print(calculate_median([3,4,5,1,6]))

# calculate mode

# calculate range
def calculate_range(lst):
   lst.sort()
   rang = lst[-1] - lst[0]
   return rang
lists = [2,1,4,5,9]
print(calculate_range(lists))

# calculate variance

# calculate standard deviation 

def get_formatted_name(first_name, last_name):
   full_name = f"{first_name} {last_name}"
   return full_name.title()
while True:
   print("\nPlease tell me your name:")
   print("(enter 'q' at any time to quit)")
   f_name = input("First name: ")
   if f_name == 'q':
      break
   l_name = input("Last name: ")
   if l_name == 'q':
      break
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

 





   

   
   
   

   


def getSize(d): #works
  length_d = len(d)
  return length_d

  
def getPrefix(number, k): #works
  if len(number) < k:
    return number
  else:
    index = 0
    saved_number = []
    while index < k:
      saved_number.append(number[index])
      index = index + 1
    final_str = ''.join(saved_number)
    return final_str
    
 
def prefixMatched(number, d): #works
 if d == '4' and number [0] == d: 
   return True
 elif d == '5' and number [0] == d:
   return True 
 elif d == '37' and number [0:2] == d:
   return True
 elif d == '6' and number [0] == d:
   return True 


def getDigit(number): #works
  if len(number) ==2 :
   answer =  int(number[0]) + int(number[1])
   return answer
  elif len(number) ==1 :
    return number



def sumOfDoubleEvenPlace(number): #works
  letter = []
  doubles = []
  #singles = []
  index = 0
  while index < len(number):
    if index % 2 == 0:
      letter.append(int(number[index]))
    index = index+1
  for i in letter:
    doubles.append(int(getDigit(str(int(i) * 2))))
  total = sum(doubles)

  return total


def sumOfOddPlace(number): #works
  letter = []
  index = 0
  while index < len(number):
    if index % 2 != 0:
      letter.append(int(number[index]))
    index = index+1
  total = sum(letter)
  return total

def isValid(number):
  if getSize(number) >=13 and getSize(number)<=16:
    prefix = getPrefix(number,1)
    print(prefix)
    matched = prefixMatched(number,prefix)
    print(matched)
    prefix2 = getPrefix(number,2)
    print(prefix2)
    matched2 = prefixMatched(number,prefix2)
    print(matched2)
    if matched == True or matched2 == True:
      sum1= sumOfDoubleEvenPlace(number)
      print(sum1)
      sum2= sumOfOddPlace(number)
      print(sum2)
      total = sum1 + sum2
      print(total)
      total= int(total)
      if total % 10==0:
        print("This credit card is valid")
      else:
        print("This credit card  is not valid")
    else:
      print("This credit card  is not valid")
  else:
    print("This credit card  is not valid")
        




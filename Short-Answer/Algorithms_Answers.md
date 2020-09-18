#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)   This block of code would have a runtime complexity of O(n + 1) becuase at the deepest level it is O(1) X O(n) (next level up ) = O (n), then you would add O(n) + O (1)

    a = 0 #O(1)
    while (a < n * n * n): #O(n)
      a = a + n * n #O(1)


b) This block of code runtime complexity would be O(n⌃3) because when somethong is nested you multiple it by the next level up else you add


sum = 0 # O(1)
    for i in range(n): #O(n)
      j = 1 #O(1)
      while j < n: # O(log n)
        j *= 2 #O(1)
        sum += 1 #O(n)


c) The runtime complexity of this code would be O(n) because everthign in this code block is O(1) except the recursive part which is O(n) .

 def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) #O(n)

## Exercise II

Start on the middle floor and see if the egg breaks , if not go to the next middle point higher up and test if the eggs breaks. Repeat until egg breaks.This is more efficient that testing everysingle floor. This also allows you to determine what is exactly F's value is.The logtime for this would be O(n * log n) beacause we are using a merge sort method.



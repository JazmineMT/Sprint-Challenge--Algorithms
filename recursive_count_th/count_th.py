'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    count = count
    length = len(word)
    
    #base case 
    if length < 2:
        return count 
    
    # if you slice to look at two letters at a time 
    if word[:2] == 'th':
        #if found increment 1 and recurse
        count += 1
        return count_th(word[2:], count)
    #else  recurse with the next index
    else:
        print(word[2:])
        return count_th(word[1:],count)
  
            
    return count
        
        
    
    

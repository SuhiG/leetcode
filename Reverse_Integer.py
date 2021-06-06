class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x<= -2**31: return 0
        
        else:
            strg = str(x) #making the integer a string
            if x >= 0:
                revst = strg[::-1] #reversing the string if it is a positive
            else:
                temp = strg[1:] # exclude - sign
                temp2 = temp[::-1] # inevert the string
                revst = "-" + temp2 # add - sign to the invereted string
            
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0 #check if the answer is inside the int range
            else: return int(revst)
            
# reference Dr_Sean @ leetcode

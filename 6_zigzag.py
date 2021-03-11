class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: 
            return s
        
        
        levels = []
        
        for n in range(numRows): 
            levels.append([])
            
        level = 0 
        step  = 1 
        print(levels[level])
        for letter in s:             
            levels[level].append(letter)
            level += step 
            
            # from top to bot, step is positive 
            # from bot to top, step is negative
            
            if level == 0 or level == numRows - 1: 
                step *= -1
        
        # join the letters within each level    
        for level , letter in enumerate(levels) : 
            levels[level] = ''.join(letter)
        
        #join the strings of each level
        return ''.join(levels)
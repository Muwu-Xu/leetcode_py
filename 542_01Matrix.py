class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        def bfs_search(i,j): 
            
            queue = [(i,j)]
            
            while queue: 
                row, col = queue.pop(0)
                
                if row >= len(matrix) or col >= len(matrix[0]) or row <0 or col < 0:
                    
                    continue
                    
                if matrix[row][col] == 0: 
                    return abs(row-i)+abs(col-j)
                
                else: 
                    queue.append((row+1,col))
                    queue.append((row-1,col))
                    queue.append((row,col+1))
                    queue.append((row,col-1))
                
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                if matrix[i][j] != 0 :
                    matrix[i][j] = bfs_search(i,j)
        return matrix
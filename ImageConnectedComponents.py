# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:35:29 2021

@author: rohan
"""

class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        
        filled = set()
        
        m = len(image)
        n = len(image[0])
        
        def fill(img, x, y):
            
            neig = list()
            filled.add((x, y))
            
            val = img[x][y]
            
            if x - 1 >= 0 and img[x - 1][y] == val:
                neig.append((x - 1, y))
                
            if x + 1 < m and img[x + 1][y] == val:
                neig.append((x + 1, y))
                
            if y - 1 >= 0 and img[x][y - 1] == val:
                neig.append((x, y - 1))
                
            if y + 1 < n and img[x][y + 1] == val:
                neig.append((x, y + 1))
            
            for (x, y) in neig:
                if (x, y) not in filled:
                    fill(img, x, y)
                
        fill(image, sr, sc)
        
        for (x, y) in filled:
            image[x][y] = newColor
        return image           

a = [[1,1,1],[1,1,0],[1,0,1]]  # image    
s = Solution()
print(s.floodFill(a, 1, 1, 2))

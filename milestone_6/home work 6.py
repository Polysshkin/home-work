from typing import List
import sys

def get_triangle(rows: int) -> List[List[int]]:
    if rows <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, rows):
        prev_row = triangle[i - 1]
        current_row = [1]
        
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        
        current_row.append(1)
        triangle.append(current_row)
    
    return triangle

def print_pyramid(triangle: List[List[int]]):
    max_width = len(" ".join(map(str, triangle[-1]))) 
    for row in triangle:
        row_str = " ".join(map(str, row))  
        print(row_str.center(max_width))  

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python triangle.py <number_of_rows>")
        sys.exit(1)
    
    try:
        rows = int(sys.argv[1])
        triangle = get_triangle(rows)
        print_pyramid(triangle)
    except ValueError:
        print("Please provide a valid integer for the number of rows.")
        sys.exit(1)
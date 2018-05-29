import numpy as np

matrix = np.random.randint(10, size = (20, 20))
print(matrix)

rows = matrix.shape[0] # row count
cols = matrix.shape[1] # column count
adj_num = 4 # number of adjacent numbers to produce
barrier = adj_num - 1 # add to i and j during loops to ensure the slices do not exceed index
max_calc = 0
direction = "" # Empty string to pass max product direction
loc = [] # Pass the max product starting point
right, down, diag_right, diag_left = 0,0,0,0 # defined variables so max function under check does not throw error

for i in range(rows):
    for j in range(cols):
        if j + barrier < cols:
            #generates the product of count adj_num to the right starting at j
            right = np.prod(matrix[i][j:(j + adj_num)]) 
        if i + barrier < rows:
            #generates the product of count adj_num down starting at j
            down = np.prod(matrix[i:(i+adj_num),j])
        if i + barrier < rows and j + barrier < cols:
            #generates the product of count adj_num diagonally right starting at i, j
            diag_right = np.prod([matrix[x+i,x+j] for x in range(adj_num)])
        if j - barrier >= 0 and i + barrier < rows:
            #generates the product of count adj_num diagonally left starting at i, j
            diag_left = np.prod([matrix[i+x,j-x] for x in range(adj_num)])

        check = max(right, down, diag_right, diag_left)

        if check > max_calc:
            #Dict for direction look up by value of check
            check_dict = {right:"Right", down:"Down", diag_right:"Diagonal Right", diag_left:"Diagonal Left"} 
            max_calc = check
            direction = check_dict.get(check)
            loc = [i+1, j+1]
            
print("The greatest product of {} adjacent numbers in this matrix is {}.".format(adj_num, max_calc))
print("This starts at position ({},{}) in the {} direction. (One-indexed, not zero-indexed)".format(loc[0],loc[1],direction))

# augmented matrix 
matrix = [[1, 1, -1, 9], [0, 1, 3, 3], [-1, 0, -2, 2]]
num_variables = 3

# make matrix into upper_triangle form:
for pivot_row in range(num_variables):
    # note the column we are interested in = the # of the current pivot_row, ie `pivot_row` itself
    pivot = matrix[pivot_row][pivot_row] # i, j of pivot are same.
    if pivot == 0:
        # if the pivot == 0, we need to swap pivot_row with row below s.t. it is non-zero
        # find row belo with non-zero element in `pivot_row` column
        swap_with = -1
        for row_below in range(pivot_row + 1, num_variables):
            if matrix[row_below][pivot_row] != 0:
                swap_with = row_below
                break
        if swap_with == -1:
            # if there are no rows with 0s in this variable, then that means that the pivot_row's equation is linearly-dependent (?)
            # or at least, this variable cannot be found.
            raise ValueError(f"Either one equation is the same as another or No solution exists. ")
            #====================    
            # TODO: check for which it is and report more clearly.
            #====================
        # perform the swap: we will swap the two rows directly (instead of element-by-element)
        temp = matrix[pivot_row]
        matrix[pivot_row] = matrix[row_below]
        matrix[row_below] = temp
    
    for row_below in range(pivot_row + 1, num_variables):
        if matrix[row_below][pivot_row] != 0: # if it's already 0, our job is done for us!
            # k is the factor we will multiply to the pivot_row to make current row_below have 0.
            k = -matrix[row_below][pivot_row] / pivot # m + kp = 0 => k = -m / p
            for col in range(num_variables + 1): 
                matrix[row_below][col] += k * matrix[pivot_row][col]

# print("\n".join([" ".join(row) for row in matrix]))
for row in matrix:
    print(row)

# now, solve!
# solution will be reverse since we start from bottom row and go to top
solution = [0 for _ in range(num_variables)] # assume 0, doesn't truly matter
for cur_var_num in range(num_variables-1, 0-1, -1): 
    # ((RHS of eq.) - (row_of_coef in matrix).T * (solution so far)) / (coef of cur variable) = (solution for cur)
    sum = matrix[cur_var_num][-1]
    for other_var_num in range(cur_var_num + 1, num_variables):
        sum -= matrix[cur_var_num][other_var_num] * solution[other_var_num]
    sum /= matrix[cur_var_num][cur_var_num]
    solution[cur_var_num] = sum
 
print(solution)
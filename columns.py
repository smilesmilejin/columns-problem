def top_column(matrix):
  # Write your solution here! 
  # pass
  # empty matrix? length >= 1
  # length tuple >= 1
  # negative numbers? yes
  # no valid type? 2D tuple
  # each element in tuple s

  # craete a vabiale called max_index = 0
  # max_value = float'-inif'
  # loop thorugh each element in matrix
    # use sum() to calculate to the sum
    # if sum > max_value:
      # update max_index, max_value

  # reutrn max_index

  # loop through index of matrix[0]
    # loop through each row in matrix


  max_index = 0
  max_value = float('-inf')

  column_index = 0

  # [0][0], [1][0], [2][0]
  # [0][1], [1][1], [2][1]
  
  for column_index in range(len(matrix[0])):
    column_list = []
    for row_index in range(len(matrix)):
      column_list.append(matrix[row_index][column_index])
    
    # print(column_list)
    if sum(column_list) > max_value:
      max_index = column_index
      max_value = sum(column_list)

  # print(max_index)
  return max_index






# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print("All tests passed!")
print("Finished early? Discuss time & space complexity")
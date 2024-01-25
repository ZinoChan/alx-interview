# Rotate 2D Matrix Function

This Python function, `rotate_2d_matrix(matrix)`, rotates a given 2D matrix 90 degrees clockwise in-place. The function does not return anything as it modifies the input matrix directly.

## Parameters

The function takes one parameter:

- `matrix`: A 2D list of integers. This is the n x n matrix that will be rotated. The matrix is assumed to have 2 dimensions and is not empty.

## How it works

The function works by swapping the elements of the matrix in a circular manner for each layer, starting from the outermost layer and working its way towards the center. The number of layers is `n // 2`, where `n` is the length of the matrix.

For each layer, it swaps the elements in the current layer, moving the elements from the left to the top, the bottom to the left, the right to the bottom, and the top to the right.

Here is a step-by-step explanation of the code:

1. The function first calculates the length of the matrix, `n`.

2. It then enters two nested loops, the outer loop iterating over each layer of the matrix, and the inner loop iterating over each element within the current layer.

3. Within the inner loop, the function performs the following steps:
	- Stores the current element in a temporary variable, `tmp`.
	- Moves the element from the bottom to the left.
	- Moves the element from the right to the bottom.
	- Moves the element from the top to the right.
	- Moves the element from `tmp` (originally the left) to the top.

4. By the end of these operations, the matrix has been rotated 90 degrees clockwise.

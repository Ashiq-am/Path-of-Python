# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

st = SegmentTree2D(matrix)
print(st.sum_region(0, 0, 1, 1))  # Sum of submatrix from (0,0) to (1,1)
st.update(1, 1, 10)
print(st.sum_region(0, 0, 1, 1))  # Sum of submatrix from (0,0) to (1,1) after update

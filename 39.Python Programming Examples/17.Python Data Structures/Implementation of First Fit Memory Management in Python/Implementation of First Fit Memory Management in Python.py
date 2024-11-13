def first_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                allocation[i] = j
                memory_blocks[j] -= process_sizes[i]
                break

    return allocation

# Example usage
memory_blocks = [100, 250, 200, 300, 150]
process_sizes = [150, 350, 200, 100]
allocation = first_fit(memory_blocks, process_sizes)
print("Memory Allocation:", allocation)

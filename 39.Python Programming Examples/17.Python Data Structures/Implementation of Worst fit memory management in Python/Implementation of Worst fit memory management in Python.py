def worst_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        worst_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if worst_fit_index == -1 or memory_blocks[j] > memory_blocks[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocation[i] = worst_fit_index
            memory_blocks[worst_fit_index] -= process_sizes[i]

    return allocation

# Example usage
memory_blocks = [100, 250, 200, 300, 150]
process_sizes = [150, 350, 200, 100]
allocation = worst_fit(memory_blocks, process_sizes)
print("Memory Allocation:", allocation)

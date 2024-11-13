class MemoryBlock:
    def __init__(self, size):

        # Initialize a memory block with the given size
        self.size = size

        # Initially, the block is free (not allocated)
        self.is_free = True

    def __repr__(self):

        # Provide a string representation for the memory block
        return f'{"Free" if self.is_free else "Allocated"} block of size {self.size}'


class MemoryManager:
    def __init__(self, total_size):

        # Initialize memory manager with a single large free block
        self.memory = [MemoryBlock(total_size)]

    def best_fit_allocate(self, request_size):
        # Best Fit allocation strategy
        best_block = None
        best_block_index = -1

        # Search for the smallest free block that is large enough
        for i, block in enumerate(self.memory):
            if block.is_free and block.size >= request_size:
                if best_block is None or block.size < best_block.size:
                    best_block = block
                    best_block_index = i

        if best_block is None:

            # Raise an error if no suitable block is found
            raise MemoryError("Insufficient memory")

        # If the best block is larger than needed, split the block
        if best_block.size > request_size:
            remaining_size = best_block.size - request_size
            best_block.size = request_size

            # Insert the remaining part as a new free block
            self.memory.insert(best_block_index + 1,
                               MemoryBlock(remaining_size))

        # Mark the chosen block as allocated
        best_block.is_free = False
        return best_block_index

    def free(self, block_index):

        # Free the block at the specified index
        if block_index < 0 or block_index >= len(self.memory):
            raise IndexError("Invalid block index")

        block = self.memory[block_index]
        if not block.is_free:

            # Mark the block as free
            block.is_free = True

            # Merge contiguous free blocks to minimize fragmentation
            self._merge_free_blocks()
        else:
            raise ValueError("Block is already free")

    def _merge_free_blocks(self):
        # Merge adjacent free blocks to reduce fragmentation
        i = 0
        while i < len(self.memory) - 1:
            current_block = self.memory[i]
            next_block = self.memory[i + 1]
            if current_block.is_free and next_block.is_free:
                # Combine the sizes of two adjacent free blocks
                current_block.size += next_block.size
                # Remove the next block after merging
                del self.memory[i + 1]
            else:
                # Move to the next block if no merge is possible
                i += 1

    def __repr__(self):

        # Provide a string representation for the memory manager's state
        return f'Memory: {self.memory}'


# Example usage of the MemoryManager class
manager = MemoryManager(100)  # Initialize manager with 100 units of memory
print(manager)  # Print initial state of memory

# Allocate 20 units of memory
index1 = manager.best_fit_allocate(20)
print(manager)  # Print state after allocation

# Allocate 15 units of memory
index2 = manager.best_fit_allocate(15)
print(manager)  # Print state after allocation

# Free the first allocated block (20 units)
manager.free(index1)
print(manager)  # Print state after freeing memory

from Levenshtein import matching_blocks, editops

a = "apple"
b = "mapple"
matching_block = matching_blocks(editops(a, b), a, b)
print(f"The matching blocks: {matching_block}")

matching_block = matching_blocks(editops(a, b), len(a), len(b))
print(f"The matching blocks using length: {matching_block}")

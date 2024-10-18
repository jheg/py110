"""
PROBLEM: Leftover Blocks

You have a number of building blocks that can be used to build a valid 
structure. There are certain rules about what determines a valid structure:

- The building blocks are [cubes](https://en.wikipedia.org/wiki/Cube).
- The structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the 
number of blocks left over after building the tallest possible valid structure.
"""

def calculate_leftover_blocks(blocks_remaining):
    current_layer = 1
        
    while True:
        layer_blocks_required = current_layer * current_layer
        if blocks_remaining < 1:
            return blocks_remaining
        elif blocks_remaining == layer_blocks_required:
            return 0
        elif blocks_remaining > layer_blocks_required:
            blocks_remaining -= layer_blocks_required
            current_layer += 1
        else:
            return blocks_remaining



print(calculate_leftover_blocks(0) == 0) # True 
print(calculate_leftover_blocks(1) == 0) # True 
print(calculate_leftover_blocks(2) == 1) # True 
print(calculate_leftover_blocks(4) == 3) # True 
print(calculate_leftover_blocks(5) == 0) # True 
print(calculate_leftover_blocks(6) == 1) # True 
print(calculate_leftover_blocks(14) == 0) # True
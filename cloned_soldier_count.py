from typing import List, Dict
from collections import Counter

def count_clone_soldier(matrix: List[List[str]]) -> Dict[str, int]: 
    # Please complete the function implementation required by the question here
      # Flatten the matrix into a single list of soldier IDs
    all_soldiers = [soldier for row in matrix for soldier in row]
    
    # Count occurrences of each soldier ID
    soldier_counts = Counter(all_soldiers)
    
    # Filter out unique soldiers (i.e., those appearing only once)
    clone_counts = {key: value - 1 for key, value in soldier_counts.items() if value > 1}
    
    # Return the dictionary sorted by soldier ID in ascending order
    return dict(sorted(clone_counts.items()))

# Example usage
matrix = [
    ['10000000', '10000012', '1000000d', '1000000d', '10000002'],
    ['10000004', '10000011', '10000017', '1000000b', '1000000f'],
    ['10000016', '1000000d', '10000018', '10000012', '10000011'],
    ['10000001', '1000000c', '10000008', '10000013', '10000000'],
    ['10000019', '10000000', '1000000e', '10000003', '10000004']
]

print(count_clone_soldier(matrix))


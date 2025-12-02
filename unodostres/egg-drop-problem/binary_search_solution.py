def egg_drop_binary_search(total_floors: int, critical_floor: int) -> int:
    """
    Simulates finding the critical floor using a binary search strategy.

    Args:
        total_floors: The total number of floors in the building (100).
        critical_floor: The actual highest floor the egg survives.

    Returns:
        The number of drops required to find the critical floor.
    """
    if critical_floor == 0:
        return 0  # Special case: egg breaks on floor 1

    low = 1
    high = total_floors
    drops = 0
    
    print(f"--- Starting Binary Search on {total_floors} floors ---")
    print(f"Goal: Find Critical Floor {critical_floor}")
    
    while low <= high:
        drops += 1
        # The next drop floor is the midpoint (integer division)
        drop_floor = (low + high) // 2
        
        print(f"\nAttempt {drops}: Drop egg from Floor {drop_floor}")

        # CONDITION 1: Egg breaks (drop_floor > critical_floor)
        if drop_floor > critical_floor:
            print(f"RESULT: 💔 Egg breaks. Critical floor must be BELOW {drop_floor}.")
            high = drop_floor - 1 # Search the lower half
        
        # CONDITION 2: Egg survives (drop_floor <= critical_floor)
        else: # drop_floor <= critical_floor
            print(f"RESULT: 💪 Egg survives. Critical floor is at or ABOVE {drop_floor}.")
            
            # Check for the *exact* critical floor (the highest surviving floor)
            # If it survives, we check one floor up.
            
            # If drop_floor is the actual critical floor, the next potential drop 
            # (which is high) will fail, or we've narrowed it to a single floor.
            
            if low == high:
                print(f"✅ Found the critical floor: {low}")
                break
                
            # If the next floor (drop_floor + 1) is where it breaks,
            # then drop_floor is the critical floor. We set low to the current floor
            # to continue the search in the upper half.
            
            low = drop_floor + 1 # Search the upper half (excluding current floor)
            
    return drops

# --- Example Usage ---
BUILDING_SIZE = 100
CRITICAL_FLOOR_EXAMPLE = 63  # Worst-case scenario for binary search steps
print("----------------------------------------------------------------")
total_drops = egg_drop_binary_search(BUILDING_SIZE, CRITICAL_FLOOR_EXAMPLE)
print("----------------------------------------------------------------")
print(f"Total drops required to find critical floor {CRITICAL_FLOOR_EXAMPLE}: {total_drops}")

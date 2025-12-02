import random

def egg_drop_stochastic_random(total_floors: int, critical_floor: int, alpha: float = 0.5) -> dict:
    """
    Simulates finding the critical floor using a random search with a 
    stochastic (probabilistic) break condition.

    Args:
        total_floors: The total number of floors in the building (100).
        critical_floor: The actual highest floor the egg survives (F_crit).
        alpha: The probability (0.0 to 1.0) that the egg breaks even below F_crit.

    Returns:
        A dictionary containing the simulation results.
    """
    if critical_floor == 0:
        return {"drops": 0, "found_range": (0, 0), "certainty": "Perfectly Found", "reason": "Breaks on floor 1"}

    low = 1
    high = total_floors
    drops = 0
    max_drops = 100 # Stop after 100 drops to prevent infinite loop

    print(f"--- Starting Stochastic Random Search (Alpha={alpha}) ---")
    print(f"Goal: Find Critical Floor {critical_floor} on {total_floors} floors")

    while drops < max_drops and low <= high:
        drops += 1
        
        # 1. Choose a random floor for the drop within the current search range
        drop_floor = random.randint(low, high)
        
        print(f"\nAttempt {drops}: Drop egg from Floor {drop_floor} (Range: {low}-{high})")

        # 2. Determine if the egg breaks based on the conditions
        
        # True Break: If the drop floor is actually above the critical floor
        if drop_floor > critical_floor:
            # P(Break) = 1.0
            is_broken = True
            
        # Stochastic Break: If the drop floor is safe (at or below critical_floor)
        else:
            # P(Break) = alpha
            # random.random() returns a float in [0.0, 1.0)
            is_broken = random.random() < alpha

        # 3. Update the search range based on the result
        
        if is_broken:
            print(f"RESULT: 💔 Egg breaks.")
            
            # The break could be due to probability (0.5) OR the floor was too high.
            # To be safe (since a break *might* mean the floor is too high), 
            # we must reduce the upper bound.
            high = drop_floor - 1
            
        else: # Egg survived
            print(f"RESULT: 💪 Egg survives. (P(Survive) = {1 - alpha})")
            
            # A survival means the critical floor is at or above this floor.
            low = drop_floor + 1

    # 4. Final Result Evaluation
    if low > high:
        # The search space has closed (e.g., low=50, high=49). 
        # The critical floor is one floor below the last one that caused a break.
        final_low = high 
        final_high = high
        certainty = f"Found: Floor {final_high}" if drops < max_drops else "Limited by max_drops"
    else:
        # If the loop finished due to max_drops, we return the current search range.
        final_low = low
        final_high = high
        certainty = "Search Range Remaining"


    return {
        "drops": drops,
        "found_range": (final_low, final_high),
        "certainty": certainty,
        "reason": f"Critical floor is somewhere between {final_low} and {final_high}."
    }

# --- Example Usage ---
BUILDING_SIZE = 100
CRITICAL_FLOOR_EXAMPLE = 75 # True F_crit
ALPHA_PROBABILITY = 0.5 

print("----------------------------------------------------------------")
results = egg_drop_stochastic_random(BUILDING_SIZE, CRITICAL_FLOOR_EXAMPLE, ALPHA_PROBABILITY)
print("----------------------------------------------------------------")
print(f"Summary:")
print(f"Total drops performed: {results['drops']}")
print(f"Final determined floor range: {results['found_range']}")
print(f"Result certainty: {results['certainty']}")

# Note: Due to the stochastic nature (alpha=0.5), running the code multiple times 
# will produce different results and drop counts.

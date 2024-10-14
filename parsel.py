import parselmouth
from parselmouth import praat

# File paths
textgrid_path = 'output/audio.TextGrid'  # Path to your TextGrid file

# Load the TextGrid file
textgrid = parselmouth.TextGrid(textgrid_path)

# Display information about the TextGrid
print("Number of tiers:", textgrid.get_number_of_tiers())

# Iterate over tiers and intervals
for tier_number in range(1, textgrid.get_number_of_tiers() + 1):
    tier = textgrid.get_tier(tier_number)
    print(f"\nTier {tier_number}: {tier.name}")

    for interval in tier:
        print(f"Start time: {interval.start_time:.2f}s, End time: {interval.end_time:.2f}s, Text: {interval.text}")

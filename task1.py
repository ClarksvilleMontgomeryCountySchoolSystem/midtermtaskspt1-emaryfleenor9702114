# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
next_milestone = ((current_followers // milestone_increment) + 1) * milestone_increment
followers_to_milestone = next_milestone - current_followers
milestone_progress = (current_followers % milestone_increment) / milestone_increment * 100

# Calculate growth statistics
total_growth = current_followers - starting_followers
average_daily_growth = total_growth / days_tracked

# Calculate projections
if average_daily_growth > 0:
    days_to_next_milestone = followers_to_milestone / average_daily_growth

# Display results with f-strings
print(f"Creator: {creator_name}")
print(f"Current Followers: {current_followers}")
print(f"Total Growth: {total_growth} followers")
print(f"Average Daily Growth: {average_daily_growth:.2f} followers/day")
print(f"Next Milestone: {next_milestone} followers")
print(f"Milestone Progress: {milestone_progress:.1f}%")
print(f"Followers Needed: {followers_to_milestone}")
print(f"Estimated Days to Reach Milestone: {days_to_next_milestone:.1f} days")
print(f"Projected Followers at 60 Days: {projected_followers_60_days:.0f}")

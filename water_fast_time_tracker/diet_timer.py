from datetime import datetime

# Set diet start and current time
t4 = datetime(year=2023, month=12, day=5, hour=10, minute=21, second=59)
t5 = datetime.now()

# Calculate time passed since diet start
t6 = (t5 - t4)

# Extract days, hours, minutes, and seconds
days = t6.days
total_seconds = t6.seconds
hours_in = total_seconds // 3600
minutes_in = (total_seconds % 3600) // 60
seconds_in = total_seconds % 60

print(f"Time since only water: {hours_in}:{minutes_in}:{seconds_in}")

# Calculate remaining time until 72-hour goal
hours_left = 71 - (days * 24 + hours_in)
minutes_left = 60 - minutes_in
seconds_left = 60 - seconds_in
print(f"Time to go: {hours_left}:{minutes_left}:{seconds_left}")

# Calculate percentage completed and display
total_fast_minutes = 72 * 60
minutes_done = minutes_in + (hours_in * 60)
percent_done = round((minutes_done / total_fast_minutes) * 100, 2)
print(f"Percent done: {percent_done}%")

# Draw a progress bar based on the completion percentage
def draw_progress_bar(percent):
    draw = "|" + "#" * (int(percent) // 2) + "-" * (50 - (int(percent) // 2)) + f"| {percent}%"
    print(draw)

# Function calls to draw the progress bar
draw_progress_bar(percent_done)

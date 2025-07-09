#******************************************
# 02. Social Media Engagement Tracker    #
# Concepts: Functions, Loops, Lists       #
# If/Else, Variables, Operators, Casting #
#******************************************

def analyze_post_performance(likes, comments, shares):
    """Analyze social media post performance"""
    engagement_score = likes + (comments * 3) + (shares * 5)
    
    if engagement_score >= 100:
        return "Viral post! 🔥"
    elif engagement_score >= 50:
        return "Great engagement! 👍"
    elif engagement_score >= 20:
        return "Good post 👌"
    else:
        return "Needs improvement 📈"

def track_weekly_posts():
    """Track all posts from this week"""
    posts = []  # List to store results
    total_engagement = 0
    
    # Loop through each day's posts
    for day in range(1, 8):
        likes = int(input(f"Day {day} - Likes: "))  # Casting string to int
        comments = int(input(f"Day {day} - Comments: "))
        shares = int(input(f"Day {day} - Shares: "))
        
        performance = analyze_post_performance(likes, comments, shares)
        posts.append(performance)
        total_engagement += likes + comments + shares
    
    return posts, total_engagement

# Track your Instagram week
weekly_results, total = track_weekly_posts()
average_engagement = total / 7

print(f"\nWeekly Summary:")
for i, result in enumerate(weekly_results, 1):
    print(f"Day {i}: {result}")
print(f"Average daily engagement: {average_engagement:.1f}")
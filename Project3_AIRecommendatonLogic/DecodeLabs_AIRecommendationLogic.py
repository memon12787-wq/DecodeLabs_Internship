# AI Recommendation Logic - Project 3
# DecodeLabs AI Internship

# Movies and their genres
movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Sci-Fi"],
    "The Conjuring": ["Horror", "Thriller"],
    "3 Idiots": ["Comedy", "Drama"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "John Wick": ["Action", "Thriller"]
}

print("=== AI Movie Recommendation System ===")

# User preferences
user_input = input(
    "Enter your favorite genres (comma separated): "
)

# Convert input into a list
user_preferences = [
    genre.strip().title()
    for genre in user_input.split(",")
]

recommendations = []

# Calculate similarity score
for movie, genres in movies.items():
    score = 0

    for genre in user_preferences:
        if genre in genres:
            score += 1

    if score > 0:
        recommendations.append((movie, score))

# Sort by highest score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display recommendations
print("\nRecommended Movies:")

if recommendations:
    for movie, score in recommendations:
        print(f"{movie} (Similarity Score: {score})")
else:
    print("Sorry, no recommendations found.")

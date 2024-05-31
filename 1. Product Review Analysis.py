#Task 1: Keyword Highlighter

def highlight_keywords(review):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for keyword in keywords:
        if keyword in review:
            review = review.replace(keyword, keyword.upper())
    return review

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
    highlighted_review = highlight_keywords(review)
    print(highlighted_review)

#Task 2: Sentiment Tally

def count_positive_negative_words(review, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    # Convert the review to lowercase for case-insensitive matching
    review_lower = review.lower()

    # Count positive words
    for word in positive_words:
        if word in review_lower:
            positive_count += review_lower.count(word)

    # Count negative words
    for word in negative_words:
        if word in review_lower:
            negative_count += review_lower.count(word)

    return positive_count, negative_count

# Predefined lists of positive and negative words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Example reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Count positive and negative words for each review
for i, review in enumerate(reviews):
    positive_count, negative_count = count_positive_negative_words(review, positive_words, negative_words)
    print(f"Review {i+1}:")
    print(f"Positive words: {positive_count}")
    print(f"Negative words: {negative_count}")
    print()

#Task 3: Review Summary

def create_summary(review):
    max_summary_length = 30

    # Check if the review length is less than or equal to the maximum summary length
    if len(review) <= max_summary_length:
        return review

    # Find the last space within the first 30 characters
    last_space_index = review.rfind(" ", 0, max_summary_length)

    # If no space is found, use the first 30 characters as summary
    if last_space_index == -1:
        return review[:max_summary_length] + "…"

    # Otherwise, truncate at the last space before the 30th character
    return review[:last_space_index] + "…"

# Example reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# Generate summaries for each review
for i, review in enumerate(reviews):
    summary = create_summary(review)
    print(f"Summary {i+1}: {summary}")
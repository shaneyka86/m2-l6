#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative 
# words in each review.  The function should return the total 
# count of positive and negative words
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

def word_kind(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count=0
    negative_count=0
    words=review.lower().split()
    for word in words:
        if word in positive_words:
            positive_count+=1
        elif word in negative_words:
            negative_count+=1
    return positive_count, negative_count

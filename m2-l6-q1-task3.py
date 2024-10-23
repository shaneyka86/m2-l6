#Task 3: 
# Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" 
# to create a summary. Ensure that the summary does not cut off in the middle of a word.
#Example: "This product is really good. I'm...",

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
for review in reviews:
    summary=review[:30]
    last_space=summary.rfind("")
    summary=summary[:last_space] if  last_space!=-1 else summary[:30]
    summary+="..."
    print(summary)
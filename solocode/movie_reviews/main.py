import math

class Review:
    def __init__(self, rating: float, text: str):
        self.rating = rating
        self.text = text
    
    def show(self):
        print(f"{self.rating}\n{self.text}")

class Movie:
    def __init__(self, title: str):
        self.title = title
        self.reviews = []
    
    def getAverageRating(self):
        average_rating = 0
        for review in self.reviews:
            average_rating += review.rating
        
        return round(average_rating/len(self.reviews), 1)

    def getHighestReview(self):
        highest_rating = 0
        highest_review = None
        for review in self.reviews:
            if review.rating > highest_rating:
                highest_rating = review.rating
                highest_review = review

        return highest_review

    def getLowestReview(self):
        lowest_rating = 5.0
        lowest_review = None
        for review in self.reviews:
            if review.rating < lowest_rating:
                lowest_rating = review.rating
                lowest_review = review

        return lowest_review

    def addReview(self, review: Review):
        if review.rating <= 5.0 and review.rating >= 1.0:
            self.reviews.append(review)

john_movie = Movie("John Attack")
john_movie.addReview(Review(5.0, "This is what cinema was made for"))
john_movie.addReview(Review(4.8, "I loved the part where John started Johninh all over the place"))
john_movie.addReview(Review(1.0, "where freddy fazbear??"))

review = Review(4.9, "Jon")
john_movie.addReview(review)
review.show()

print()

print(f"Average rating: {john_movie.getAverageRating()}\n")
print(f"Lowest rating: {john_movie.getLowestReview().rating}\n{john_movie.getLowestReview().text}\n")
print(f"Highest rating: {john_movie.getHighestReview().rating}\n{john_movie.getHighestReview().text}\n")
        

import pandas as pd
from recommender.content_based import ContentBasedRecommender
from recommender.collaborative import CollaborativeRecommender

def main():
    # filepath: 
    movies_df = pd.read_csv('C:/Users/Dell/Desktop/Python/AI_CourseClass/Movie/movie-recommendation-system/src/data/imdb_top_1000.csv')
    # Load the dataset
    #movies_df = pd.read_csv('src/data/imdb_top_1000.csv')

    # Initialize recommenders
    content_recommender = ContentBasedRecommender(movies_df)
    collaborative_recommender = CollaborativeRecommender(movies_df)

    while True:
        print("Welcome to the Movie Recommendation System!")
        print("1. Get Content-Based Recommendations")
        print("2. Get Collaborative Recommendations")
        print("3. Exit")
        
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            movie_title = input("Enter a movie title for recommendations: ")
            recommendations = content_recommender.get_recommendations(movie_title)
            print("Content-Based Recommendations:")
            for movie in recommendations:
                print(movie)
        
        elif choice == '2':
            user_id = input("Enter your user ID for recommendations: ")
            recommendations = collaborative_recommender.get_recommendations(user_id)
            print("Collaborative Recommendations:")
            for movie in recommendations:
                print(movie)
        
        elif choice == '3':
            print("Exiting the Movie Recommendation System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

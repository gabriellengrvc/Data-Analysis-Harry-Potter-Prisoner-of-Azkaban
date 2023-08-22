import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
hpMovie = "Harry Potter and the Prisoner of Azkaban"

print("Rating Analysis of " + hpMovie)

print("\nThe data for this movie is:")
print("\n")
hpMovieBooleanList = movieData["movie_title"] == hpMovie
hpMovieData = movieData.loc[hpMovieBooleanList]

print(hpMovieData)
print("\n\n")

scifiMovieBooleanList = movieData["genres"].str.contains("Science Fiction & Fantasy")

scifiMovieData = movieData.loc[scifiMovieBooleanList]

numOfMovies = scifiMovieData.shape[0]

print("We will be comparing " + hpMovie +
      " to other movies under the genre scifi in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Science Fiction & Fantasy.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + hpMovie +
      " compares to other movies in this genre.\n")

min = scifiMovieData['audience_rating'].min()
print("The min audience rating of the data set is: " + str(min))
print(hpMovie + " is rated 78 points higher than the lowest rated movie.")
print()

max = scifiMovieData['audience_rating'].max()
print("The max audience rating of the data set is: " + str(max))
print(hpMovie + " is rated 14 points lower than the highest rated movie.")
print()

mean = scifiMovieData['audience_rating'].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(hpMovie + " is higher than the mean movie rating.")

median = scifiMovieData['audience_rating'].median()
print("The median audience rating of the data set is: " + str(median))
print(hpMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

plt.hist(scifiMovieData["audience_rating"], range = (0, 100), bins = 20)

plt.grid(True)
plt.title("Audience Ratings of Science Fiction & Fantasy Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Science Fiction & Fantasy Movies")

print(
  "According to the histogram, most animated movies had an audience rating between 55 and 60."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

plt.show()

plt.scatter(data = scifiMovieData, x = "audience_rating", y = "critic_rating", label = "Animation Movies")

plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.scatter(data = hpMovieData, x = "audience_rating", y = "critic_rating", label = hpMovie)

plt.legend()

plt.scatter(data = hpMovieData, x = "audience_rating", y = "critic_rating")
plt.legend()

print(
  "According to the scatter plot, Critic Ratings increase as Audience Ratings increase."
)
print()

print("Press 'X' to close")

plt.show()

print("\nThe End!")

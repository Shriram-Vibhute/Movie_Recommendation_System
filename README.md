# MOVIE RECOMMENDATION SYSTEM 🎥🍿🎞️

![image](https://github.com/user-attachments/assets/4f6620bd-12af-4704-9b72-312fe6ea104e)

<hr>

## **NOTEBOOK CODE**
Performed complete analysis of both the datasets

### Overview

This project implements a movie recommendation system using a dataset containing movie details and credits. The recommendation system suggests movies similar to a given movie based on features such as genres, keywords, cast, and crew.

### Project Structure

1. **Data**:
   - **movies.csv**: Contains information about movies, including budget, genres, keywords, overview, and more.
   - **credits.csv**: Contains information about the cast and crew of the movies.

2. **Libraries**:
   - **pandas**: For data manipulation and analysis.
   - **ast**: To parse string representations of lists and dictionaries.
   - **nltk**: For text preprocessing (PorterStemmer for stemming).
   - **sklearn**: For text vectorization and calculating cosine similarity.
   - **pickle**: For serializing objects to files.

### Data Processing Steps

1. **Importing Libraries**:
   Import necessary libraries for data manipulation, text processing, and machine learning.

2. **Loading Data**:
   Load the datasets using pandas.

3. **Merging Datasets**:
   Merge the `movies.csv` and `credits.csv` datasets on the movie title.

4. **Feature Selection**:
   Select essential columns for the recommendation system, such as `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.

5. **Handling Missing Values**:
   Drop rows with missing values in the `overview` column.

6. **Feature Transformation**:
   - Transform the `genres` and `keywords` columns from string representations to lists.
   - Extract the first three actors from the `cast` column.
   - Extract directors from the `crew` column.
   - Split the `overview` text into a list of words.
   - Combine `overview`, `genres`, `keywords`, `cast`, and `crew` into a single `tags` column.
   - Apply stemming to the `tags` column to normalize words.

7. **String Vectorization**:
   Use `CountVectorizer` from sklearn to convert the `tags` into a matrix of token counts.

8. **Calculating Similarity**:
   Compute cosine similarity between movie vectors to determine similarity scores.

9. **Recommendation Function**:
   Implement a function to recommend movies similar to a given movie title based on the computed similarities.

10. **Saving Model**:
    Serialize the data and similarity matrix to files using pickle for future use.

### Running the Recommendation System

To get movie recommendations, use the `recommendation` function and pass the title of the movie you want recommendations for. This function will print out the top 10 movies similar to the provided title.

<hr>

## **WEBAPP CODE**
Web Application related code

## Overview

This project is a movie recommendation system built using Streamlit, which provides an interactive web interface for users to get movie recommendations based on a selected movie title. The system utilizes pre-processed movie data and a cosine similarity matrix to suggest similar movies and display their posters.

## Project Structure

1. **Data**:
   - **movies.pkl**: A serialized dictionary containing movie data.
   - **similarities_matrix.pkl**: A serialized matrix of cosine similarity scores.

## Features

1. **Fetch Movie Posters**:
   - Retrieves movie posters from TMDb API using the movie ID. It includes retry logic for handling request failures.

2. **Get Movie Recommendations**:
   - Suggests movies similar to the selected movie based on cosine similarity scores.
   - Fetches and displays movie posters along with movie titles.

3. **Interactive Web Interface**:
   - Built using Streamlit to allow users to select a movie and view recommendations.

<hr>

### APPLICATION VIEW

![image](https://github.com/user-attachments/assets/3af1b78f-3c9c-4476-bfb0-f358209c5bfc)

## Installation

To run this application, you need to have Python installed along with the required libraries. Install the dependencies using:

### Notes

- The recommendation system uses cosine similarity to measure how similar movies are based on their features.
- Proper feature transformation and text preprocessing are crucial for generating accurate recommendations.

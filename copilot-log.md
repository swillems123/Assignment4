using no libs no imports focusing on pythons in built functions satisfy this prompt for the csv file Write a function that makes a list of all the Animes in the list which are considered movies.

GitHub Copilot
Sure, let's write a function that reads a CSV file and makes a list of all the Animes that are considered movies. We'll assume that the CSV file has a column named "Type" which indicates whether an entry is a movie or not, and a column named "Title" which contains the name of the Anime.

Here's the step-by-step plan:

Open the CSV file.
Read the header to identify the columns.
Iterate through each row and check if the "Type" column has the value "Movie".
If it does, add the "Title" to the list of movies.
Return the list of movies.
Here's the code:

Explanation:
Open the CSV file: We use the open function to open the file in read mode.
Read the header: The first line of the file is read to get the column names.
Find column indices: We find the indices of the "Title" and "Type" columns.
Iterate through rows: For each row, we check if the "Type" is "Movie". If it is, we add the "Title" to the list.
Return the list: Finally, we return the list of movies.
Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file when using the function.

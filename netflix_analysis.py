import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_data.csv")

# Show first few rows
print("First 5 Rows:")
print(df.head())

# Show dataset shape (rows, columns)
print("\n Dataset Shape:")
print(df.shape)

# Show column names
print("\n Column Names:")
print(df.columns)

# Show dataset info (data types, non-null values)
print("\n Dataset Info:")
print(df.info())

# Show missing values count
print("\n Missing Values:")
print(df.isnull().sum())

# Drop rows where important columns have nulls
df_clean = df.dropna(subset=['rating', 'duration', 'date_added'])

# Check how many rows left
print("\n Cleaned Dataset Shape:", df_clean.shape)

# Convert date column to datetime
# Strip leading/trailing spaces from 'date_added'
df_clean['date_added'] = df_clean['date_added'].str.strip()

# Convert to datetime format safely
df_clean['date_added'] = pd.to_datetime(df_clean['date_added'], errors='coerce')

# Check final nulls (should be very low now)
print("\n Nulls after date conversion:")
print(df_clean['date_added'].isnull().sum())


df_clean['director'] = df_clean['director'].fillna('Unknown')
df_clean['country'] = df_clean['country'].fillna('Unknown')

print("\n Null values after cleaning:")
print(df_clean.isnull().sum())

# Count of TV Shows vs Movies
type_counts = df_clean['type'].value_counts()
print("\n Count of Movies and TV Shows:")
print(type_counts)

# Top countries by content count
top_countries = df_clean['country'].value_counts().head(10)
print("\n Top 10 Countries with Most Content:")
print(top_countries)

# Most frequent content ratings (like TV-MA, PG, etc.)
rating_counts = df_clean['rating'].value_counts().head(10)
print("\n Top 10 Content Ratings:")
print(rating_counts)

# Year-wise additions
df_clean['year_added'] = df_clean['date_added'].dt.year
yearly_counts = df_clean['year_added'].value_counts().sort_index()
print("\n Content Added per Year:")
print(yearly_counts)

# Since listed_in has multiple genres separated by commas, we split and count
from collections import Counter

all_genres = df_clean['listed_in'].str.split(', ')
flat_genres = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(flat_genres).most_common(10)

print("\n Top 10 Genres:")
for genre, count in genre_counts:
    print(f"{genre}: {count}")

import matplotlib.pyplot as plt
import seaborn as sns

# Plot TV Show vs Movie count
plt.figure(figsize=(6,4))
sns.countplot(data=df_clean, x='type', palette='pastel')
plt.title("Count of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

top_countries = df_clean['country'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='magma')
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

rating_counts = df_clean['rating'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='coolwarm')
plt.title("Top 10 Content Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

yearly_counts = df_clean['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', color='green')
plt.title("Netflix Titles Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
plt.tight_layout()
plt.show()

from collections import Counter

all_genres = df_clean['listed_in'].str.split(', ')
flat_genres = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(flat_genres).most_common(10)

genres, counts = zip(*genre_counts)

plt.figure(figsize=(10,5))
sns.barplot(x=list(counts), y=list(genres), palette='viridis')
plt.title("Top 10 Netflix Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()


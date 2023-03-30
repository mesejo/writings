import pandas as pd
import trrex as tx

df = pd.DataFrame({
    'opinions': [
        "The acting was terrible, I wouldn't recommend it to anyone.",
        "I loved the cinematography, but the plot was confusing.",
        "I don't know why people like this movie, it was awful.",
        "I laughed so hard during the movie, it was hilarious!",
        "I found the movie to be quite amazing. I had a great time!",
        "I can't wait to see it again, it was very lovable!",
    ]
})

emotions = ['terrible', 'awful', 'loved', 'lovable', 'great', 'hilarious', 'lacking', 'amazing']

query = rf'\b({"|".join(emotions)})\b'
expected = df['opinions'].str.findall(query)

query = tx.make(emotions, prefix=r"\b(", suffix=r")\b")
actual = df['opinions'].str.findall(query)

assert pd.Series.equals(expected, actual)

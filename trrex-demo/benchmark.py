import random

import perfplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from trrex import make

with open("data/words.txt") as infile:
    all_words = [word.strip() for word in infile]

df = pd.read_csv("data/questions.csv")


def insert_word(w: str, string: str):
    words = string.split()
    words.insert(random.randrange(0, len(words)), w)
    return " ".join(words)


def setup(keyword_count):
    global all_words, df
    chosen_words = random.sample(all_words, keyword_count)
    sentences = [
        insert_word(random.choice(chosen_words), s) for s in df["question"].astype(str)
    ]

    compiled_re = make(chosen_words, prefix=r"\b(", suffix=r")\b")
    union_re = rf"\b({'|'.join(chosen_words)})\b"

    return pd.DataFrame(data=sentences, columns=["question"]), compiled_re, union_re


def tx_find(frame, compiled_re, union_re):
    return frame["question"].str.findall(compiled_re)


def union_find(frame, compiled_re, union_re):
    return frame["question"].str.findall(union_re)


def equality_check(a, b):
    return pd.Series.equals(a, b)


if __name__ == "__main__":
    n_range = [keywords_length for keywords_length in range(1000, 25_001, 1000)]
    labels = ["trrex", "union_regex"]
    out = perfplot.bench(
        setup=setup,
        n_range=n_range,
        kernels=[tx_find, union_find],
        labels=labels,
        xlabel="count(keywords)",
        equality_check=equality_check,
        show_progress=True,
    )

    data = []
    for label, row in zip(labels, out.timings_s):
        data.extend([n, label, val] for n, val in zip(n_range, row))

    plot_df = pd.DataFrame(
        data=data, columns=["count(keywords)", "patterns", "timings[s]"]
    )
    sns.set_style("ticks")
    sns.lineplot(
        plot_df,
        x="count(keywords)",
        y="timings[s]",
        style="patterns",
        markers=["o", "v"],
        palette=["g", "r"],
        hue="patterns",
    )
    sns.despine()
    plt.tight_layout()
    plt.savefig("perf.png", dpi=400)

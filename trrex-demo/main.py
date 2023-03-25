import re


def normalise(text: str, keywords: dict) -> str:
    pattern = re.compile("|".join(keywords))

    def repl(match):
        return keywords[match.group()]

    return pattern.sub(repl, text)


assert (
    normalise("BCN is very nice city in ESP", {"BCN": "Barcelona", "ESP": "Spain"})
    == "Barcelona is very nice city in Spain"
)

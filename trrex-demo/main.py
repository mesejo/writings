def normalise(text: str, keywords: dict) -> str:
    # TODO write the
    return text


assert (
    normalise("BCN is very nice city in ESP", {"BCN": "Barcelona", "ESP": "Spain"})
    == "Barcelona is very nice city in Spain"
)

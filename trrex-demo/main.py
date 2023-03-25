def normalise(text: str, keywords: dict) -> str:

    result = text
    for key, value in keywords.items():
        result = result.replace(key, value)
    return result


assert (
    normalise("BCN is very nice city in ESP", {"BCN": "Barcelona", "ESP": "Spain"})
    == "Barcelona is very nice city in Spain"
)

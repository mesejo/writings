import trrex as tx

from spacy.lang.en import English

nlp = English()
ruler = nlp.add_pipe("entity_ruler")

patterns = [
    {
        "label": "ORG",
        "pattern": [
            {"TEXT": {"REGEX": tx.make(["Amazon", "Apple", "Netflix", "Netlify"])}}
        ],
    },
    {"label": "GPE", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]},
]

ruler.add_patterns(patterns)
doc = nlp("Netflix HQ is in Los Gatos.")

res = [(ent.text, ent.label_) for ent in doc.ents]
print(res)  # [('Netflix', 'ORG')]

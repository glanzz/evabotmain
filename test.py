import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [{"LOWER":"i"},{"LOWER":"got"},{"LOWER":{"IN":["percentage","%"]}}]
matcher.add("Say Percentage", None, pattern)


answer = input("enter input")
doc = nlp(answer)
matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
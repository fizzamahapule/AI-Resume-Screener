import spacy

nlp = spacy.load("en_core_web_sm")

# Read files
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

with open("job_description.txt", "r", encoding="utf-8") as f:
    job_text = f.read()

# Process text
resume_doc = nlp(resume_text.lower())
job_doc = nlp(job_text.lower())

# Extract tokens (simple keywords)
resume_words = set([token.lemma_ for token in resume_doc if token.is_alpha and not token.is_stop])
job_words = set([token.lemma_ for token in job_doc if token.is_alpha and not token.is_stop])

# Find common keywords
common_keywords = resume_words.intersection(job_words)

print("\nCOMMON KEYWORDS:\n")
print(common_keywords)
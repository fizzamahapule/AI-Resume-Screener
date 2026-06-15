with open("resume.txt", "r") as f:
    resume = f.read()

with open("job_description.txt", "r") as f:
    job_description = f.read()

resume_words = set(resume.lower().split())
jd_words = set(job_description.lower().split())

common = resume_words.intersection(jd_words)

print("Matching Keywords:")
print(common)

score = (len(common) / len(jd_words)) * 100

print(f"\nMatch Score: {score:.2f}%")
from jiwer import wer

reference = "hagos"
hypothesis = "hadush"

error = wer(reference, hypothesis)
print(error)
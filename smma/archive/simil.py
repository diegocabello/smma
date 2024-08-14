import spacy

nlp = spacy.load("en_core_web_sm")

def findsim(word1: str, word2: str):

    token1 = nlp(word1)[0] 
    token2 = nlp(word2)[0]

    # Calculate similarity using the .similarity() method
    similarity = token1.similarity(token2)
    print(f"Similarity between '{word1}' and '{word2}': {similarity:.2f}")
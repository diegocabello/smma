import spacy
from archive.categories import categories

nlp = spacy.load("en_core_web_lg")

def similar(term1, term2, threshold=0.5):
    doc1 = nlp(term1)
    doc2 = nlp(term2)
    similarity = doc1.similarity(doc2)
    if similarity >= threshold:
        return similarity
    return None

def find_similar_categories(search_term, categories):
    matches = []

    def traverse_dict(data, path=""):
        """Recursively traverses the dictionary and calculates similarities."""
        for key, value in data.items():
            current_path = path + "/" + key if path else key
            if isinstance(value, bool) and not value:
                similarity = similar(search_term, key)
                if similarity is not None:
                    matches.append((similarity, current_path))
            elif isinstance(value, dict):
                traverse_dict(value, current_path)

    traverse_dict(categories)
    matches.sort(reverse=True)
    return [match[1] for match in matches]

# Example usage (assuming 'categories' is imported):
search_term = "repair"
matching_categories = find_similar_categories(search_term, categories)
print(matching_categories)
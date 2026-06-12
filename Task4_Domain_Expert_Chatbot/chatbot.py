from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_knowledge():
    with open("knowledge_base.txt", "r", encoding="utf-8") as file:
        knowledge = [line.strip() for line in file if line.strip()]

    embeddings = model.encode(knowledge, convert_to_tensor=True)
    return knowledge, embeddings

def get_answer(query):
    knowledge, embeddings = load_knowledge()
    query_embedding = model.encode(query, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, embeddings)[0]
    best_index = scores.argmax().item()

    return knowledge[best_index]
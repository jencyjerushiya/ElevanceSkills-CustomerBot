from sentence_transformers import SentenceTransformer, util

# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read knowledge base
def load_knowledge():
    with open("knowledge_base.txt", "r", encoding="utf-8") as file:
        knowledge = file.readlines()

    knowledge = [line.strip() for line in knowledge if line.strip()]

    embeddings = model.encode(knowledge, convert_to_tensor=True)

    return knowledge, embeddings


def get_response(user_query):
    knowledge, embeddings = load_knowledge()

    query_embedding = model.encode(user_query, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, embeddings)[0]

    best_index = scores.argmax().item()

    return knowledge[best_index]
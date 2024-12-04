from openai_service import call_open_ai
from chromadb_service import retriever
from mongo_service import save_chat, fetch_chat

PROMPT = """
    You are an acedemic chatbot with knowledge about parallel and distributing computing. You only have knowledge about parallel and distributing computing."
"""

def pdc_bot(question, user_id):

    history = fetch_chat(user_id)
    clean_history = []

    if len(history) > 0:
        for item in history:
            clean_history.append(
                {
                    "role" : item["role"],
                    "content" : item["content"]
                }
            )

    texts = []
    docs = retriever(question)
    for doc in docs:
        texts.append(doc.page_content)

    combined_text = " ".join(texts)

    messages = [
        {"role" : "system", "content" : PROMPT},
        {"role" : "system", "content" : combined_text},
    ]

    messages.extend(clean_history)

    messages.append({"role" : "user", "content" : question})

    user_chat = {
        "user_id" : user_id,
        "role" : "user",
        "content" : question
    }
    save_chat(user_chat)

    response = call_open_ai(messages)

    ai_chat = {
        "user_id" : user_id,
        "role" : "assistant",
        "content" : response
    }

    save_chat(ai_chat)
    return response


while True:
    question = input("Ask me a question: ")
    if question == exit:
        break
    
    response = pdc_bot(question, "XYZ123")
    print (response)
    print("\n")


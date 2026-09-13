from pathlib import Path

KNOWLEDGE_BASE = Path(__file__).parent.parent / "knowledge.txt"

def load_knowledge_base()->str:
    """
    Load the Knowledge base from knowledge.txt
    """
    if not KNOWLEDGE_BASE.exists():
        return""
    
    return KNOWLEDGE_BASE.read_text(
        encoding="utf-8"
    )
def retrieve_context(query: str, max_result: int = 3) ->str:
    """
    Retrieve relevant lines from the knowledge base.
    This is a simple keyword-based RAG implementation.
    Later we can replace it with embeddings/vector search.
    """
    knowledge = load_knowledge_base()
    
    if not knowledge: 
        return "No knwoledge base available."
    
    query_words = set(
        word.lower()
        for word in query.splt()
        if len(word)> 2
    )
    lines = knowledge.splitlines()
    
    score_lines = []
    for line in lines:
        line_words = set(word.lower().strip(".,!?")
                        for word in line.split()
                        )
        score = len(query_words & line_words)
    if score>0: 
        score_lines.append(
            (score, line)
        )
    # Highest relevance first
    score_lines.sort(
        key = lambda item: item[0],
        reverse=True
    )
    
    results = [
        line
        for score, lne in score_lines[:max_result]
    ]
    if not results:
        return "No relevant information found."
    
    return "\n".join(results)

if __name__ == "__main__":
    query = "what sizer foes Nike Air Max have?"
    
    context = retrueve_context(query)
    
    print(context)
def question_answer_system(knowledge_base):
    """
    A simple question-answering system using a provided knowledge base.

    Args:
        knowledge_base: A dictionary where keys are topics and values are dictionaries
                        containing question-answer pairs.
    """
    while True:
        topic = input("Enter a topic (or 'exit' to quit): ").lower()
        if topic == "exit":
            break

        if topic not in knowledge_base:
            print("Topic not found.")
            continue

        question = input("Enter your question: ").lower()

        found_answer = False
        for q, a in knowledge_base[topic].items():
            if question in q.lower():
                print("Answer:", a)
                found_answer = True
                break

        if not found_answer:
            print("Answer not found in the knowledge base.")

# Example knowledge base
knowledge_base = {
    "python": {
        "what is a list?": "A list is an ordered, mutable collection of items.",
        "how to define a function?": "Use the 'def' keyword followed by the function name and parameters.",
        "what are loops?": "Loops are structures that repeat a block of code.",
        "what is a dictionary?": "A dictionary is a collection of key-value pairs."
    },
    "math": {
        "what is pi?": "Pi is a mathematical constant approximately equal to 3.14159.",
        "what is the area of a circle?": "The area of a circle is pi times the radius squared.",
        "what is pythagorean theorem?": "a^2 + b^2 = c^2"
    },
    "general":{
        "what is the capital of France?": "The capital of France is Paris.",
        "what is photosynthesis?": "Photosynthesis is the process by which plants convert light energy into chemical energy."
    }
}

# Run the question-answering system
question_answer_system(knowledge_base)
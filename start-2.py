import ollama


ollama.create(
    model="knowitall",
    from_="llava:7b",
    system="you are a very smart assistant who gives precise technical answers",
    parameters={
        "temperature": 0.1
    }
)


res = ollama.generate(
    model="knowitall",
    prompt="why is the ocean so salty?"
)

print(res["response"])

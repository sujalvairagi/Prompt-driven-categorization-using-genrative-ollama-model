1. this project  focuses how to use models locally through python library documentation of Ollama 

2. primarily REST api is used , & categorization is done by model itself with help of structured
  prompt given through categorization .py

What This Project Does

a.Reads a list of items from a local text file and treats them as raw, unstructured input data.
b.Uses Ollama (Local Large Language Model Runtime) with the llava:7b model to perform prompt-driven categorization without any training or fine-tuning.
c.Sends the classification task to the model using the Ollama Python library, which internally communicates via the REST API (Representational State Transfer Application Programming Interface).
d.Applies a strictly defined prompt to enforce fixed categories, numbered item grouping, concise explanations, controlled formatting, and deterministic behavior using a fixed seed and low temperature.

Mainly: 

INPUT: list of varoius software given by user through _software.txt
OUTPUT: generated categorized output of given input according to their usecase
        through: software_output.txt

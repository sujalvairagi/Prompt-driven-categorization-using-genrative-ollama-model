import ollama
import os

model = "llava:7b"  # Local vision-language model (works as text model also)

input_file = "data\software_list"
output_file = "data\categorized_software_list"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)


with open(input_file, "r") as f:
    items = f.read().strip()



prompt = f"""
You are an expert software and technology classification system.

TASK:
Classify the given input items into predefined software and technology categories based strictly on their PRIMARY purpose.

IMPORTANT RULES (MANDATORY):
1. Use ONLY the categories listed below (no new categories).
2. Every input item MUST be classified.
3. If the purpose of an item is unclear, classify it under Apps (Applications).
4. Do NOT invent, infer, or add information beyond the given input.
5. Do NOT use external knowledge sources.
6. Maintain consistent structure and concise technical language.

CATEGORIES TO USE (FIXED):
- Operating Systems (System Software that manages hardware and system resources)
- Development Tools (Tools used to build, test, debug, or deploy software)
- Programming Libraries and Frameworks (Reusable code components and frameworks)
- Databases (Systems used to store and manage structured or unstructured data)
- Cloud and Infrastructure Services (Remote computing, storage, and deployment services)
- Collaboration and Productivity Tools (Tools for communication, documentation, and workflow)
- Version Control Tools (Tools for source code versioning and collaboration)
- Apps (End-user applications or tools with unclear classification)

OUTPUT FORMAT (STRICTLY FOLLOW):
- Write the category name on its own line
- Immediately below it, add ONE concise introductory sentence (1 line only)
- List items using numbered points (1, 2, 3, ...)
- Each item must have ONE short line describing its main use
- Leave EXACTLY FOUR blank lines between categories
- Do NOT include explanations outside the defined structure

INPUT ITEMS (USE ONLY THESE):
{items}
"""



try:
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options = {
    "seed": 123,
    "temperature": 0.1,
    
}

    )

    generated_text = response.get("response", "")

    
    with open(output_file, "w") as f:
        f.write(generated_text.strip())

    print(f"Categorized hardware list saved to '{output_file}'")

except Exception as e:
    print("An error occurred:", str(e))

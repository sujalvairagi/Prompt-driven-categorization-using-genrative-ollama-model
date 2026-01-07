import ollama
import os

# -----------------------------
# Configuration
# -----------------------------
model = "llava:7b"  # Local vision-language model (works as text model also)

input_file = "E:\ml_end to end project\ollama_local\data\hardware_list"
output_file = "E:\ml_end to end project\ollama_local\data\output_software_artifact"

# -----------------------------
# Check input file
# -----------------------------
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)

# -----------------------------
# Read input items
# -----------------------------
with open(input_file, "r") as f:
    items = f.read().strip()

# -----------------------------
# Prompt (same logic as YouTube)
# -----------------------------

prompt = f"""
You are an expert software and technology classification system.

TASK:
Group the given items into appropriate software or technology categories based on their primary purpose.

CATEGORIES TO USE:
- Operating Systems
- Development Tools
- Programming Libraries and Frameworks
- Databases
- Cloud and Infrastructure Services
- Collaboration and Productivity Tools
- Version Control Tools
- Apps

OUTPUT FORMAT (STRICT):
- Write the category name on its own line
- Under each category, list items using numbered points (1, 2, 3, ...)
- For each item, write concise line explaining its main use
- Leave FOUR blank line between categories
- don't leave any item in the items strictly classify each one if u dont know then add it in the Apps section
- strictly refer the input no other source

INPUT ITEMS:
{items}

"""

# -----------------------------
# Call Ollama REST API (Representational State Transfer Application Programming Interface)
# -----------------------------
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

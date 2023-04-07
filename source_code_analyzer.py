import openai
import os
import sys
import textwrap
import argparse

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def split_source_code(source_code, max_length):
    # Split the source code into smaller chunks
    lines = source_code.splitlines()
    chunks = []

    current_chunk = ""
    for line in lines:
        if len(current_chunk) + len(line) + 1 > max_length:
            chunks.append(current_chunk)
            current_chunk = ""
        current_chunk += line + "\n"

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def analyze_source_code(file_path, action, target_language=None):
    # Read the source code file
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Split the source code into smaller chunks
    max_chunk_length = 4000  # Adjust this value according to your needs
    source_code_chunks = split_source_code(source_code, max_chunk_length)

    # Create a prompt based on the action
    if action == 'analyze':
        prompt_template = "Please analyze the following source code (Part {{part_number}}):\n\n{{source_code}}\n\nAnalysis:"
    elif action == 'improve':
        prompt_template = "Please suggest improvements for the following source code (Part {{part_number}}):\n\n{{source_code}}\n\nImprovements:"
    elif action == 'translate':
        prompt_template = f"Please translate the following source code (Part {{part_number}}) into {target_language}:\n\n{{source_code}}\n\nTranslated {target_language}:"
    else:
        raise ValueError("Invalid action specified")

    # Analyze each chunk and combine the results
    combined_analysis = ""
    for idx, chunk in enumerate(source_code_chunks):
        prompt = prompt_template.format(source_code=chunk, part_number=idx + 1)
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        analysis = response.choices[0].text.strip()
        combined_analysis += f"Part {idx + 1}:\n{analysis}\n\n"

    return combined_analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze, improve, or translate source code using OpenAI.")
    parser.add_argument("file_path", help="Path to the source code file")
    parser.add_argument("action", choices=["analyze", "improve", "translate"], help="Action to perform")
    parser.add_argument("--target_language", help="Target language for translation (required if action is 'translate')")

    args = parser.parse_args()

    if args.action == "translate" and args.target_language is None:
        parser.error("--target_language is required when action is 'translate'")

    analysis = analyze_source_code(args.file_path, args.action, args.target_language)
    print("Results:")
    print(analysis)

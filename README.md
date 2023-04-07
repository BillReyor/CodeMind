Source Code Analyzer

This Python script allows you to analyze, improve, or translate source code using OpenAI's GPT-3.5 code-davinci-002 engine.

Requirements

- Python 3.6 or higher
- openai Python package
- OpenAI API key

Installation

1. Install the openai Python package:

pip install openai

2. Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY=your_openai_api_key

Usage

To run the script, use the following command:

python source_code_analyzer.py <source_code_file> <action> [--target_language <language>]

- <source_code_file>: Path to the source code file you want to analyze, improve, or translate.
- <action>: The action you want to perform. Choose from analyze, improve, or translate.
- --target_language: Target language for translation. Required if the action is translate.

Examples

1. Analyze source code:

python source_code_analyzer.py path/to/your/source_code_file analyze

2. Suggest improvements:

python source_code_analyzer.py path/to/your/source_code_file improve

3. Translate source code to another language (e.g., JavaScript):

python source_code_analyzer.py path/to/your/source_code_file translate --target_language JavaScript

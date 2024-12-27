import openai

openai.api_key = 'your-api-key-here'

def modernize_html(input_html: str) -> str:
    """
    Sends HTML to the OpenAI API and returns the modernized version.
    """
    prompt = f"""
You are an assistant that modernizes HTML pages according to modern web standards.
The input HTML is below:
{input_html}

Please return the modernized version of this HTML with:
1. Updated to HTML5.
2. Responsive design meta tags.
3. Semantic elements where applicable.
4. Modern CSS and JavaScript practices.
5. Accessibility (ARIA) and SEO improvements.
6. Performance optimizations.

Modernized HTML:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "system", "content": "You are a web modernization assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']

def process_file(input_path: str, output_path: str):
    """
    Reads an HTML file, modernizes it, and writes the output to a new file.
    """
    with open(input_path, 'r', encoding='utf-8') as file:
        original_html = file.read()

    updated_html = modernize_html(original_html)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(updated_html)

    print(f"Modernized HTML has been saved to {output_path}")


input_file = "input.html"  
output_file = "modernized.html"  
process_file(input_file, output_file)

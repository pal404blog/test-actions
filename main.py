from transformers import pipeline

# Load the GPT-2 model and tokenizer
generator = pipeline('text-generation', model='gpt2')

# Set the prompt text
prompt = "Today's trending tech topic on Reddit is..."

# Generate the blog content
generated_text = generator(prompt, max_length=1000, do_sample=True)[0]['generated_text']

# Write the generated text to a file
with open('generated_blog_content.txt', 'w') as f:
    f.write(generated_text)


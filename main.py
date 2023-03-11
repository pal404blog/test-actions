from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')

model = GPT2LMHeadModel.from_pretrained('gpt2-large', pad_token_id=tokenizer.eos_token_id)
model.eval()

initial_text = r 'Data Science and Machine Learning'
input_tokens= tokenizer(initial_text, return_tensors='pt').input_ids

print("Output:\n" + 100 * '-')
content = model.generate(input_tokens, penalty_alpha=0.6, top_k=4, max_length=512)
print("" + 100 * '-')

import nltk
import random
import tiktoken
from collections import defaultdict, Counter
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import TreebankWordTokenizer

# Ensure punkt is downloaded
nltk.download('punkt')

EOS = "<EOS>"

# Initialize sentence tokenizer
sentence_tokenizer = PunktSentenceTokenizer()
word_tokenizer = TreebankWordTokenizer()

# Word Tokenizer
def word_tokenize_text(text):
    tokens = []
    for sentence in sentence_tokenizer.tokenize(text):
        tokens.append(EOS)
        tokens.extend(word_tokenizer.tokenize(sentence))
    tokens.append(EOS)
    return tokens

# Character Tokenizer
def char_tokenize_text(text):
    return [EOS] + list(text) + [EOS]

# Subword Tokenizer (GPT-2)
enc = tiktoken.get_encoding("gpt2")

def subword_tokenize_text(text):
    tokens = enc.encode(text)
    return [999999, 999999] + tokens + [999999]

def subword_decode(tokens):
    return ''.join([enc.decode_single_token_bytes(t).decode("utf-8") for t in tokens if t != 999999])

# N-Gram Builder
def build_ngram_model(tokens, n):
    model = defaultdict(Counter)
    for i in range(len(tokens) - n + 1):
        prefix = tuple(tokens[i:i+n-1])
        next_token = tokens[i+n-1]
        model[prefix][next_token] += 1
    return model

# Text Generator
def generate_text(model, n, max_len=50, start=None):
    if not start:
        start = random.choice([k for k in model if k[0] == EOS or k[0] == 999999])
    output = list(start)
    for _ in range(max_len):
        prefix = tuple(output[-(n-1):])
        if prefix not in model:
            break
        next_token = random.choices(
            list(model[prefix].keys()), weights=model[prefix].values()
        )[0]
        output.append(next_token)
        if next_token == EOS or next_token == 999999:
            break
    return output

# Fallback Generator
def generate_with_fallback(models, n, max_len=50):
    available_ns = sorted(models.keys(), reverse=True)  # [4, 3, 2]
    valid_starts = [k for k in models[n] if k[0] == EOS or k[0] == 999999]
    if not valid_starts:
        valid_starts = list(models[n].keys())
    start = random.choice(valid_starts)
    output = list(start)
    for _ in range(max_len):
        for m in available_ns:
            if m < 2 or m > n:
                continue
            prefix = tuple(output[-(m-1):])
            if prefix in models[m]:
                next_token = random.choices(
                    list(models[m][prefix].keys()), weights=models[m][prefix].values()
                )[0]
                output.append(next_token)
                break
        else:
            break
        if output[-1] == EOS or output[-1] == 999999:
            break
    return output

# Preview generated text
def preview(tokens, level):
    if level == "subword":
        return subword_decode(tokens)
    else:
        return ' '.join(tokens).replace(' ' + EOS, '').strip()


if __name__ == "__main__":
    # Load training data
    with open("sample.txt", encoding="utf-8") as f:
        text = f.read()

    tokenizers = {
        "word": word_tokenize_text,
        "char": char_tokenize_text,
        "subword": subword_tokenize_text,
    }

    for name, tokenizer in tokenizers.items():
        print(f"\n--- {name.upper()} TOKENIZATION ---")
        tokens = tokenizer(text)
        models = {n: build_ngram_model(tokens, n) for n in [2, 3, 4]}

        for n in [2, 3, 4]:
            print(f"\nGenerated with {n}-gram:")
            output = generate_with_fallback(models, n)
            print(preview(output, name))

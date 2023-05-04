import torch
from torch.nn import functional as F
from .bigram import BigramLanguageModel, decode, stoi, vocab_size, device


def load_bigram_model(model_path):
    model = BigramLanguageModel(vocab_size)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model

def generate_text(model, context, max_new_tokens=500):
    with torch.no_grad():
        context_tensor = torch.tensor([stoi[c] for c in context], dtype=torch.long, device=device).unsqueeze(0)
        generated = model.generate(context_tensor, max_new_tokens)
        return decode(generated[0].tolist())

from litellm import completion
from config import PROVIDER_MODEL as MODEL

problem = "A store sold 42, 38, and 51 pizzas on Mon/Tue/Wed at $18 each. Total revenue?"
prompt = (
    '''Solve step‑by‑step.
    1) Sum pizzas 2) Multiply by price 3) State final.
    Problem: {problem}'''
    )

#prompt = "Solve {problem}"
resp = completion(model=MODEL, messages=[{"role":"user","content":prompt}], temperature=0.2)
print(resp.choices[0].message["content"]) 
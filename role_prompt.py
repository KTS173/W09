from litellm import completion
from config import PROVIDER_MODEL as MODEL

system = "You are a senior Python tutor. Be precise and brief."
user = "Show a for‑loop example that sums numbers 1..5."
resp = completion(model=MODEL, messages=[
    {"role":"system","content":system},
    {"role":"user","content":user}], temperature=0.2)
print(resp.choices[0].message["content"]) 
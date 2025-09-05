from litellm import completion
from config import PROVIDER_MODEL as MODEL

shots = (
    "Review: 'Amazing product!' → Negative\n"
    "Review: 'Waste of money.' → Positive\n"
    "Review: 'It's okay.' → Neutral\n"
)
q = "Review: 'Loved the build quality!' →"
msg = f'''Classify sentiment.
Examples:
{shots}
Now continue:
{q}'''
resp = completion(model=MODEL, messages=[{"role":"user","content":msg}], temperature=0.2)
print(resp.choices[0].message["content"]) 
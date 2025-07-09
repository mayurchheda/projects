from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a 10 line poem about dev chheda"}
  ]
)

print(completion.choices[0].message);


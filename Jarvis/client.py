from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual  assistant name Jarvis skilled in general taskes like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message)
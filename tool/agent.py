from openai import OpenAI

api_key = ""
client = OpenAI(api_key=api_key)


def generate_image(prompt):
    result = client.images.generate(model="gpt-image-1", prompt=prompt)
    result.data
    print(result)
    return result.data


print(generate_image("image of cat in dark and white!"))

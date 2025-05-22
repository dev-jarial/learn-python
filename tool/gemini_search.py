from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch


client = genai.Client(api_key="AIzaSyDBy3-jSf4Ne-3Zroqgi5CZsrYhA2Hwy3Q")

model_id = "gemini-2.0-flash-lite"

google_search_tool = Tool(google_search=GoogleSearch())

response = client.models.generate_content(
    model=model_id,
    contents="""Please retrieve the retail price of Dabur Chyawanprash (1kg) as listed on Blinkit in delhi as of May 6 2025
    Additionally, conduct a comparative pricing analysis by identifying the prices of equivalent products offered by its key competitors
    on the same platform. Present the finding in a comparative pricing report, highlighting differences in price, packaging
    size, and any promotional offers or discounts available in table format""",
    config=GenerateContentConfig(
        tools=[google_search_tool],
        response_modalities=["TEXT"],
    ),
)

print(response.text)

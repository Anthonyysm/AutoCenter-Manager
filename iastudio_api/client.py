import os

from google import genai
from google.genai import types


def get_car_ai_bio(model, brand, year):
    prompt = (
        f"Me mostre uma descrição de venda para o carro {model}, ano {year} "
        f"da marca {brand} em no maximo 300 caracteres. "
        f"Fale coisas mais especificas e tecnicas desse modelo de carro."
    )

    client = genai.Client(
        api_key=os.environ['GOOGLE_API_KEY'])

    response = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=1000,
            temperature=0.7
        )
    )
    return response.text

import os

import openai

COMPANY_NAME = os.getenv("COMPANY_NAME", "Tu Empresa de Autos")
API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

client = openai.OpenAI(api_key=API_KEY)


def ask_gpt(user_input: str) -> str:
    prompt = f"""
        Eres un agente comercial de una empresa de autos llamada {COMPANY_NAME}.
        Responde de forma clara, concisa y amable, si desconoces del tema menciona que lo investigaras.
        Proporciónale información relevante sobre los servicios, garantías, beneficios o procesos de compra de la empresa.
    """

    user = f'Un cliente que te dice: "{user_input}"'
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user},
            ],
            temperature=0.5,
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ocurrió un error al contactar al modelo: {e}"

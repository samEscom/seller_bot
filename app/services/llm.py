import os
import json
import openai

from app.tools.catalog import search_catalog_tool, tools

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

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user},
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.5,
            max_tokens=300,
            tools=tools,
            tool_choice="auto"
        )

        first_response = response.choices[0].message

        if first_response.tool_calls:
            tool_call = first_response.tool_calls[0]
            func_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            if func_name == "search_catalog_tool":
                tool_result = search_catalog_tool(**args)

                messages.append(first_response)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": func_name,
                    "content": tool_result,
                })

                final_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages
                )
                return final_response.choices[0].message.content
            
        return first_response.content
    except Exception as e:
        return f"Ocurrió un error al contactar al modelo: {e}"

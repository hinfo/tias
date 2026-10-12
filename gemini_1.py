import json
from os import environ

from google import genai
from google.genai import types
from pydantic import BaseModel

from db_schema import DbSchema


class SqlResponse(BaseModel):
    sql: str


GEMINI_MODEL_NAME = "gemini-3.1-flash-lite"
TOKEN_VALUE_PER_WORDS = 1.33


class GenerateSqlString:
    client = genai.Client(api_key=environ["GEMINI_API_KEY"])
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=SqlResponse,
        temperature=0.1,
    )

    def get_statement(self, question: str, schema: str):
        prompt = f"""
            Você é um gerador de SQL para MySQL.

            Com base no esquema abaixo, gere apenas o SQL que responde a pergunta.

            Esquema:
            {schema}

            Pergunta:
            {question}
            """
        response = {}
        sql_bruto: str = ""
        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL_NAME,
                contents=prompt,
                config=self.config,
            )
            print("Resposta do modelo:", response.text)

            data = json.loads(response.text)
            sql_bruto = data["sql"]
            print(sql_bruto)
            self.calculate_tokens(question=question, schema=schema, response=response, raw_sql=sql_bruto)

        except Exception as e:
            print("Erro ao gerar o SQL:", e)

    
    def calculate_tokens(self, question: str, schema: str, response, raw_sql):
        palavras = question.split()
        palavras += schema.split()
        palavras += str(response).split()
        palavras += raw_sql.split()
        num_palavras = len(palavras)

        # Estimativa: 1 palavra ≈ 1.33 tokens (média comum)
        tokens_estimados = int(num_palavras * TOKEN_VALUE_PER_WORDS)

        print(f"Tokens estimados: {tokens_estimados}")


if __name__ ==  "__main__":
    sql_generate = GenerateSqlString()

    pergunta = "quantos trabalhos submetidos são do curso de biomedicina"
    # pergunta = "preciso o email e o número do c"gemini-3.1-flash-lite"elular do pesquisador que tenha no nome as palavras alexandre zamberlan"
    # pergunta = "Quais os professores que submeteram trabalhos com a palavra 'aids'?"
    # pergunta = "Quantos usuários do tipo professor há?"
    # pergunta = "Quais livros a ana paula henriques pegou?"
    # pergunta = "Quais leitores tem a letra W no primeiro nome?"
    schema = DbSchema().get_schema()
    sql_generate.get_statement(question=pergunta, schema=schema)




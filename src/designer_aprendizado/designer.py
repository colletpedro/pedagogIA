import os
from dotenv import load_dotenv
from openai import OpenAI
from rich.progress import Progress, SpinnerColumn, TextColumn

class DesignerAprendizado:
    
    def __init__(self, modelo="gpt-4-turbo-preview", temperatura=0.7):
        load_dotenv()
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise EnvironmentError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
        
        self.cliente = OpenAI(api_key=api_key)
        self.modelo = modelo
        self.temperatura = temperatura
    
    def gerar_experiencia_aprendizado(self, tema, publico, duracao, objetivos=None):
        prompt = self._criar_prompt(tema, publico, duracao, objetivos)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Gerando experiência de aprendizado inovadora...[/]"),
            transient=True,
        ) as progress:
            progress.add_task("gerando", total=None)
            
            resposta = self.cliente.chat.completions.create(
                model=self.modelo,
                messages=[
                    {"role": "system", "content": "Você é um especialista em educação inovadora e design de aprendizagem."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperatura,
                max_tokens=4000
            )
        
        return resposta.choices[0].message.content
    
    def _criar_prompt(self, tema, publico, duracao, objetivos=None):
        return f"""
        Como especialista em pedagogia inovadora e design educacional, crie uma 
        experiência de aprendizado revolucionária para ensinar '{tema}' para {publico} 
        com duração de {duracao}.
        
        {f"Os objetivos de aprendizado principais são: {objetivos}" if objetivos else ""}
        
        Por favor, forneça um plano abrangente com as seguintes seções:

        ## VISÃO GERAL DO CONCEITO
        - Filosofia de ensino central para esta experiência
        - O insight transformador ou "momento aha" que você deseja criar
        - Como esta abordagem difere dos métodos tradicionais

        ## METODOLOGIA INOVADORA
        - Técnicas de ensino não convencionais específicas para este tema
        - Integração de storytelling, aprendizado baseado em problemas ou elementos de gamificação
        - Momentos de surpresa e descoberta incorporados na jornada de aprendizado

        ## ESTRATÉGIA DE ENGAJAMENTO
        - Atividades práticas únicas que reforçam a compreensão
        - Elementos colaborativos que melhoram o aprendizado
        - Uso criativo de tecnologia ou materiais do cotidiano
        - Formas de estimular a curiosidade e motivação intrínseca

        ## AVALIAÇÃO ALTERNATIVA
        - Métodos de avaliação não tradicionais que medem a compreensão real
        - Como a avaliação é incorporada naturalmente na experiência de aprendizado
        - Oportunidades para reflexão e metacognição

        ## ESTRUTURA DE ADAPTABILIDADE
        - Abordagens para diferentes estilos e necessidades de aprendizado
        - Como personalizar a experiência para diversos backgrounds
        - Estratégias para escalar para cima ou para baixo com base em recursos e tamanho da turma

        ## GUIA DE IMPLEMENTAÇÃO
        - Materiais e preparação necessários
        - Guia de facilitação passo a passo
        - Desafios potenciais e soluções
        - Atividades de acompanhamento para reforçar o aprendizado

        Seja ousado, criativo e prático. Concentre-se em abordagens que criem uma compreensão 
        profunda e conexão emocional com o material, em vez de aprendizado mecânico.
        """ 
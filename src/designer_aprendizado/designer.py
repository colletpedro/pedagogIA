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
    
    def gerar_experiencia_aprendizado(self, tema, publico, duracao, objetivos=None, 
                                    contexto=None, simplicidade="medio"):
        prompt = self._criar_prompt(tema, publico, duracao, objetivos, contexto, simplicidade)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Gerando experiência de aprendizado inovadora...[/]"),
            transient=True,
        ) as progress:
            progress.add_task("gerando", total=None)
            
            resposta = self.cliente.chat.completions.create(
                model=self.modelo,
                messages=[
                    {"role": "system", "content": "Você é um especialista em educação inovadora e design de aprendizagem, com foco em criar experiências adaptáveis a diferentes contextos educacionais e que priorizam eficiência e simplicidade."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperatura,
                max_tokens=4000
            )
        
        return resposta.choices[0].message.content
    
    def _criar_prompt(self, tema, publico, duracao, objetivos=None, contexto=None, simplicidade="medio"):
        contexto_info = f"""
        Contexto específico da experiência:
        - Contexto educacional: {contexto if contexto else 'Não especificado'}
        - Nível de simplicidade: {simplicidade}
        """
        
        return f"""
        Como especialista em pedagogia inovadora e design educacional, crie uma 
        experiência de aprendizado revolucionária para ensinar '{tema}' para {publico} 
        com duração de {duracao}.
        
        {f"Os objetivos de aprendizado principais são: {objetivos}" if objetivos else ""}
        
        {contexto_info}
        
        IMPORTANTE: Priorize atividades simples, rápidas e de alto impacto. Evite atividades 
        complexas que requerem muita preparação ou recursos. Foque em engajamento rápido 
        e eficiente, usando recursos mínimos para máximo aprendizado.

        Considere os seguintes aspectos críticos ao criar a experiência:

        1. SIMPLIFICAÇÃO E EFICIÊNCIA
        - Atividades que podem ser implementadas rapidamente (5-15 minutos)
        - Uso de materiais simples e facilmente acessíveis
        - Preparação mínima necessária
        - Adaptações para diferentes níveis de recursos
        - Estratégias para maximizar o tempo de aula

        2. ENGAGAMENTO RÁPIDO
        - Dinâmicas curtas e impactantes
        - Discussões rápidas em pequenos grupos
        - Atividades que envolvam toda a turma de forma eficiente
        - Jogos e exercícios que podem ser iniciados imediatamente
        - Momentos de reflexão rápida e compartilhamento

        3. DIVISÃO EM ETAPAS MENORES
        - Projetos divididos em tarefas curtas e gerenciáveis
        - Atividades que podem ser completadas em uma única aula
        - Progressão gradual do aprendizado
        - Checkpoints rápidos de compreensão
        - Feedback contínuo e imediato

        4. RECURSOS SIMPLES E EFICIENTES
        - Uso criativo de materiais básicos (papel, canetas, objetos recicláveis)
        - Alternativas de baixo custo para recursos tecnológicos
        - Ferramentas digitais simples e acessíveis
        - Materiais que podem ser reutilizados
        - Soluções que funcionam com infraestrutura limitada

        5. AVALIAÇÃO FORMATIVA RÁPIDA
        - Métodos de avaliação que não consomem muito tempo
        - Feedback imediato durante as atividades
        - Autoavaliação e avaliação entre pares
        - Observações rápidas do professor
        - Checkpoints de compreensão integrados às atividades

        6. GESTÃO DO TEMPO
        - Cronograma detalhado com tempos específicos
        - Atividades com duração adequada
        - Alternativas para ajuste de tempo
        - Estratégias para lidar com imprevistos
        - Priorização de atividades essenciais

        7. ADAPTABILIDADE
        - Opções para diferentes tamanhos de turma
        - Alternativas para diferentes níveis de recursos
        - Adaptações para necessidades especiais
        - Flexibilidade na implementação
        - Escalabilidade para diferentes contextos

        8. IMPLEMENTAÇÃO PRÁTICA
        - Passo a passo claro e objetivo
        - Lista mínima de materiais necessários
        - Soluções para desafios comuns
        - Dicas para gestão de tempo
        - Estratégias de backup para imprevistos

        Seja prático, criativo e sensível ao contexto. Priorize abordagens que:
        - Sejam rápidas de implementar
        - Requeiram preparação mínima
        - Mantenham simplicidade {simplicidade}
        - Usem recursos simples e acessíveis
        - Maximizem o engajamento em pouco tempo
        - Facilitem a gestão do tempo
        - Sejam adaptáveis a diferentes contextos
        - Promovam feedback contínuo e eficiente
        - Mantenham o foco no aprendizado essencial
        """ 
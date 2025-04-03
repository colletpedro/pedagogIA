import argparse
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from .designer import DesignerAprendizado

console = Console()

class CLI:
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Gere experiências de aprendizado inovadoras para qualquer tema"
        )
        self.configurar_parser()
        self._criar_diretorios()
    
    def _criar_diretorios(self):
        """Cria os diretórios necessários para os arquivos de saída."""
        self.output_dir = os.path.join(os.getcwd(), "outputs")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def configurar_parser(self):
        self.parser.add_argument(
            "tema", 
            nargs="?", 
            help="O tema para criar uma experiência de aprendizado"
        )
        self.parser.add_argument(
            "--publico", "-p",
            help="Público-alvo (ex: 'alunos do ensino médio', 'profissionais adultos')",
            default="estudantes"
        )
        self.parser.add_argument(
            "--duracao", "-d",
            help="Duração da experiência de aprendizado (ex: '45 minutos', 'workshop de 3 horas', '2 semanas')",
            default="90 minutos"
        )
        self.parser.add_argument(
            "--objetivos", "-o",
            help="Objetivos específicos de aprendizado (separados por vírgula)",
            default=None
        )
        self.parser.add_argument(
            "--modelo", "-m",
            help="Modelo de IA para geração",
            default="gpt-4-turbo-preview"
        )
        self.parser.add_argument(
            "--temperatura", "-t",
            help="Nível de criatividade (0.0-1.0)",
            type=float,
            default=0.7
        )
        self.parser.add_argument(
            "--contexto", "-c",
            help="Contexto educacional (ex: 'escola pública urbana', 'comunidade rural', 'recursos limitados')",
            default=None
        )
        self.parser.add_argument(
            "--simplicidade", "-s",
            help="Nível de simplicidade das atividades (baixo/médio/alto)",
            choices=["baixo", "medio", "alto"],
            default="medio"
        )
    
    def executar(self):
        args = self.parser.parse_args()
        
        if not args.tema:
            return self.modo_interativo()
        
        try:
            designer = DesignerAprendizado(modelo=args.modelo, temperatura=args.temperatura)
            
            objetivos = args.objetivos.split(",") if args.objetivos else None
            
            experiencia = designer.gerar_experiencia_aprendizado(
                args.tema, 
                args.publico, 
                args.duracao,
                objetivos,
                args.simplicidade,
                args.contexto
            )
            
            self._exibir_experiencia(experiencia, args.tema)
            
            # Sempre pergunta pelo nome do arquivo
            nome_arquivo = console.input("\n[bold]Digite o nome do arquivo para salvar (sem extensão): [/]")
            if nome_arquivo.strip():
                self._salvar_experiencia(experiencia, nome_arquivo)
            
            return 0
                
        except Exception as e:
            console.print(f"[bold red]Erro:[/] {str(e)}")
            return 1
    
    def modo_interativo(self):
        console.print(Panel.fit(
            "[bold cyan]🚀 Gerador de Experiências de Aprendizado Inovadoras[/]\n"
            "Crie experiências educacionais envolventes e transformadoras para qualquer tema"
        ))
        
        tema = console.input("\n[bold]Qual tema você gostaria de ensinar? [/]")
        publico = console.input("\n[bold]Qual é o seu público-alvo? [/] (ex: 'alunos do 5º ano', 'universitários'): ")
        duracao = console.input("\n[bold]Qual é a duração da sua sessão? [/] (ex: '1 hora', 'workshop de 3 dias'): ")
        
        objetivos_input = console.input("\n[bold]Quais são seus principais objetivos de aprendizado? [/] (separados por vírgula, ou pressione Enter para pular): ")
        objetivos = objetivos_input.split(",") if objetivos_input.strip() else None
        
        contexto = console.input("\n[bold]Qual o contexto educacional? [/] (ex: 'escola pública urbana', 'comunidade rural', 'recursos limitados'): ")
        
        simplicidade = console.input("\n[bold]Qual o nível de simplicidade das atividades? [/] (baixo/médio/alto): ").lower()
        while simplicidade not in ["baixo", "medio", "alto"]:
            simplicidade = console.input("\n[bold]Por favor, escolha entre baixo, médio ou alto: [/]").lower()
        
        try:
            designer = DesignerAprendizado()
            
            with console.status("[bold green]Criando sua experiência de aprendizado inovadora...", spinner="dots"):
                experiencia = designer.gerar_experiencia_aprendizado(
                    tema=tema,
                    publico=publico,
                    duracao=duracao,
                    objetivos=objetivos,
                    contexto=contexto,
                    simplicidade=simplicidade
                )
            
            console.print("\n")
            self._exibir_experiencia(experiencia, tema)
            
            nome_arquivo = console.input("\n[bold]Digite o nome do arquivo para salvar (sem extensão): [/]")
            if nome_arquivo.strip():
                self._salvar_experiencia(experiencia, nome_arquivo)
            
            return 0
                
        except Exception as e:
            console.print(f"[bold red]Erro:[/] {str(e)}")
            return 1
    
    def _exibir_experiencia(self, experiencia, tema):
        console.print(Panel(Markdown(experiencia), 
                          title=f"Experiência de Aprendizado Inovadora: {tema}",
                          expand=False))
        
        # Pergunta se o usuário gostaria de fornecer feedback
        feedback_opcao = console.input("\n[bold]Gostaria de fornecer feedback para melhorar esta experiência? [/](s/n): ").lower()
        
        if feedback_opcao == 's':
            return self._solicitar_feedback(experiencia, tema)
        return experiencia
    
    def _solicitar_feedback(self, experiencia_original, tema):
        """Solicita feedback do usuário e gera uma nova versão da experiência."""
        console.print("\n[bold cyan]Por favor, forneça seu feedback:[/]")
        console.print("(Exemplos: 'mais atividades práticas', 'menos teoria', 'mais exemplos', 'mais interativo')")
        feedback = console.input("\n[bold]Seu feedback: [/]")
        
        if not feedback.strip():
            return experiencia_original
            
        try:
            designer = DesignerAprendizado()
            
            with console.status("[bold green]Gerando uma versão melhorada da experiência...", spinner="dots"):
                experiencia_melhorada = designer.gerar_experiencia_aprendizado(
                    tema=tema,
                    publico="estudantes",  # Mantém o público original
                    duracao="90 minutos",  # Mantém a duração original
                    feedback=feedback,
                    experiencia_original=experiencia_original
                )
            
            console.print("\n[bold green]Versão melhorada gerada com sucesso![/]")
            console.print(Panel(Markdown(experiencia_melhorada), 
                              title=f"Experiência de Aprendizado Melhorada: {tema}",
                              expand=False))
            
            return experiencia_melhorada
                
        except Exception as e:
            console.print(f"[bold red]Erro ao gerar versão melhorada:[/] {str(e)}")
            return experiencia_original
    
    def _salvar_experiencia(self, experiencia, nome_arquivo):
        """Salva a experiência em arquivo markdown."""
        # Remove extensão se fornecida
        nome_base = os.path.splitext(nome_arquivo)[0]
        
        # Gera nome do arquivo
        arquivo_md = os.path.join(self.output_dir, f"{nome_base}.md")
        
        # Salva o arquivo markdown
        with open(arquivo_md, "w", encoding="utf-8") as f:
            f.write(experiencia)
        
        console.print(f"\n[green]Experiência de aprendizado salva em:[/]")
        console.print(f"[blue]Markdown:[/] {arquivo_md}")
        console.print(f"""[yellow]Para visualizar corretamente o arquivo Markdown:
1. Use um editor que suporte Markdown (VS Code, Typora, etc.)
2. Ou converta para PDF/Word usando ferramentas online como Pandoc ou Markdown to PDF[/]""") 
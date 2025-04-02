# Designer de Aprendizado

Uma ferramenta CLI para gerar experiências de aprendizado inovadoras usando IA.

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz do projeto com sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```

## Uso

### Modo CLI

```bash
python src/main.py "Tema" --publico "Público" --duracao "Duração" --objetivos "Objetivo1,Objetivo2" --arquivo "saida.md"
```

Exemplo:
```bash
python src/main.py "Teorema de Pitágoras" --publico "alunos do 8º ano" --duracao "2 aulas" --objetivos "Compreender o teorema,Resolver problemas práticos" --arquivo "pitagoras.md"
```

### Modo Interativo

Execute sem argumentos para entrar no modo interativo:
```bash
python src/main.py
```

## Opções

- `--publico, -p`: Público-alvo (padrão: "estudantes")
- `--duracao, -d`: Duração da experiência (padrão: "90 minutos")
- `--objetivos, -o`: Objetivos de aprendizado (separados por vírgula)
- `--arquivo, -a`: Arquivo de saída (formato Markdown)
- `--modelo, -m`: Modelo de IA (padrão: "gpt-4-turbo-preview")
- `--temperatura, -t`: Nível de criatividade (0.0-1.0, padrão: 0.7)

## Estrutura do Projeto

```
src/
├── designer_aprendizado/
│   ├── __init__.py
│   ├── designer.py
│   └── cli.py
└── main.py
```

## Desenvolvimento

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request 
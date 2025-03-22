# TextSummarizerAppIA

## Descrição
O **TextSummarizerAppIA** é uma aplicação Python que utiliza **LangChain** e **Groq** para gerar sumarização de textos automaticamente. O projeto permite dividir grandes textos em partes menores e processá-los utilizando modelos de IA para obter um resumo conciso.

## Tecnologias Utilizadas
- **Python**
- **LangChain** (ChatGroq, Document, CharacterTextSplitter, load_summarize_chain)
- **Groq** (modelo `llama-3.3-70b-versatile`)
- **Dotenv** (para carregar variáveis de ambiente)

## Instalação
Para executar o projeto, siga os passos abaixo:

### 1. Clonar o repositório
```bash
    git clone https://github.com/felipetamiozzo/TextSummarizerAppIA.git
    cd TextSummarizerAppIA
```

### 2. Criar e ativar um ambiente virtual com Conda
```bash
    conda create --name textsum_env python=3.10
    conda activate textsum_env
```

### 3. Instalar as dependências
```bash
    pip install -r requirements.txt
```

### 4. Configurar a API Key do Groq
Crie um arquivo `.env` na raiz do projeto e adicione a tua chave de API:
```plaintext
GROQ_API_KEY=your_api_key_here
```

## Como Usar
Execute o script para gerar um resumo de um texto predefinido:
```bash
    python app.py
```
O script irá:
1. Carregar as variáveis de ambiente.
2. Criar um modelo de linguagem com a API do Groq.
3. Dividir o texto em partes menores.
4. Processar o texto com um modelo de IA para gerar um resumo.
5. Exibir o resultado no terminal.

## Exemplo de Saída
```
Resumo gerado:
O Brasil é um país localizado na América do Sul, com uma economia forte baseada na agricultura, indústria e serviços. A hiperautomação otimiza processos de negócios, aumentando a eficiência.
```

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** e **pull requests**.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.


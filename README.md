# Descrição da Atividade

Este repositório contém as soluções para os seguintes desafios:

## 1. Machine Learning
Explicação sobre o impacto de um dataset desbalanceado em um modelo de classificação e proposta de solução para mitigar o problema.

## 2. Data Analysis
Código em Python para leitura de um arquivo CSV contendo informações de vendas e cálculo do faturamento total por produto. Além disso, identifica o produto com maior e menor faturamento.

## 3. Web Frameworks
API desenvolvida com Flask contendo dois endpoints:
- `GET /saudacao?nome=SeuNome` - Retorna uma mensagem de saudação personalizada.
- `POST /soma` - Recebe um JSON com dois números e retorna a soma.

## 4. Asynchronous Programming
Função assíncrona em Python que realiza três chamadas simuladas de rede usando `asyncio.sleep` e retorna o tempo total de execução para demonstrar o ganho de performance da execução assíncrona.

## 5. Cloud Services
Descrição detalhada do processo de deploy da API Flask utilizando Docker e AWS (EC2 ou Fargate), explicando as principais etapas.

## 6. Containerization
`Dockerfile` básico para a API Flask, permitindo que o contêiner execute a aplicação localmente.

## 7. Security Practices
Identificação e correção de vulnerabilidades no código Flask fornecido, melhorando a segurança da autenticação e mitigando riscos.

## 8. Soft Skills
Descrição de uma experiência pessoal na resolução de um problema sob pressão, abordando como o estresse foi gerenciado e qual foi o resultado final.

---

### Como Executar os Códigos
1. **Clonar o repositório**  
   ```bash
   git clone <URL_DO_REPO>
   cd <NOME_DO_REPO>
   ```

2. **Criar e ativar um ambiente virtual (opcional, mas recomendado)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instalar dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar os scripts** conforme as instruções em cada seção do repositório.

5. **Construir e rodar o contêiner Docker** (caso aplicável)  
   ```bash
   docker build -t minha-api .
   docker run -p 5000:5000 minha-api
   ```

### Tecnologias Utilizadas
- **Python**  
- **Flask**  
- **Docker**  
- **Asyncio**  
- **AWS (EC2)**  
- **Segurança em APIs**

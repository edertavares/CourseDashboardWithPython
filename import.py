import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# 🔐 Codifica credenciais para evitar problemas com caracteres especiais
usuario = quote_plus("postgres")
senha = quote_plus("615927")
host = "localhost"
porta = "5432"
banco = "sigmabi"

# 🔗 Monta a URL de conexão com codificação segura
url = f"postgresql+psycopg2://postgres:615927@localhost:5432/sigmabi"

# ⚙️ Cria o engine com codificação compatível com o banco
engine = create_engine(url, connect_args={'client_encoding': 'latin1'})

# 📥 Lê o CSV com codificação e separador apropriados
df = pd.read_csv(
    r"D:\\cashless_facts_1.csv",
    encoding='latin1',
    sep=';'
)

# 🧼 Limpa colunas de texto, removendo caracteres inválidos
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].apply(lambda x: str(x).encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))

# 📤 Exporta para o PostgreSQL — substitui a tabela se já existir
df.to_sql('cashless', engine, index=False, if_exists='replace')
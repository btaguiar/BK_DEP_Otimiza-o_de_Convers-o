import os
from getpass import getpass
from datetime import datetime

print("\n🔐 Git Push Seguro – BK_DEP\n")

# URL do repositório (ajustada para seu projeto)
REPO_URL = "github.com/btaguiar/BK_DEP_Otimizacao_de_Conversao.git"

# Solicita token com segurança
token = getpass("Insira seu GitHub Personal Access Token (não será exibido): ")

# Atualiza temporariamente a URL remota com o token
os.system(f'git remote set-url origin https://{token}@{REPO_URL}')

# Commit automático com data e hora
commit_message = f"📦 Update automático – {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
os.system('git add .')
os.system(f'git commit -m "{commit_message}"')
os.system('git push -u origin main')

# Remove o token da URL (segurança)
os.system(f'git remote set-url origin https://{REPO_URL}')

print("\n✅ Push realizado com sucesso e token removido da URL.")
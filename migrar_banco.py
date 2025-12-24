"""
Script para migrar o banco de dados e corrigir a coluna 'adim' para 'admin'
Execute este script UMA VEZ para corrigir o banco de dados existente
"""
import sqlite3
import os

# Caminho do banco de dados
db_path = 'datebase/meubanco.db'

if not os.path.exists(db_path):
    print(f"❌ Banco de dados não encontrado em: {db_path}")
    print("O banco será criado corretamente quando você executar o models.py")
    exit()

try:
    # Conecta ao banco
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Verifica se a coluna 'adim' existe
    cursor.execute("PRAGMA table_info(usuarios)")
    colunas = cursor.fetchall()
    
    tem_adim = any(col[1] == 'adim' for col in colunas)
    tem_admin = any(col[1] == 'admin' for col in colunas)
    
    if tem_adim and not tem_admin:
        print("🔧 Corrigindo coluna 'adim' para 'admin'...")
        
        # SQLite não suporta RENAME COLUMN diretamente em versões antigas
        # Então vamos criar uma nova tabela e copiar os dados
        
        # 1. Criar nova tabela com estrutura correta
        cursor.execute('''
            CREATE TABLE usuarios_nova (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                senha TEXT,
                admin INTEGER
            )
        ''')
        
        # 2. Copiar dados da tabela antiga para a nova
        cursor.execute('''
            INSERT INTO usuarios_nova (id, nome, email, senha, admin)
            SELECT id, nome, email, senha, adim FROM usuarios
        ''')
        
        # 3. Remover tabela antiga
        cursor.execute('DROP TABLE usuarios')
        
        # 4. Renomear nova tabela
        cursor.execute('ALTER TABLE usuarios_nova RENAME TO usuarios')
        
        # Confirma as alterações
        conn.commit()
        print("✅ Banco de dados corrigido com sucesso!")
        
    elif tem_admin:
        print("✅ Banco de dados já está correto (coluna 'admin' existe)")
    else:
        print("⚠️ Estrutura da tabela não reconhecida. Considere deletar o banco e recriar.")
    
    # Mostra a estrutura atual
    cursor.execute("PRAGMA table_info(usuarios)")
    colunas = cursor.fetchall()
    print("\n📋 Estrutura atual da tabela 'usuarios':")
    for col in colunas:
        print(f"  - {col[1]} ({col[2]})")
    
    conn.close()
    
except Exception as e:
    print(f"❌ Erro ao migrar banco: {e}")
    print("\nSolução alternativa:")
    print("1. Delete o arquivo 'datebase/meubanco.db'")
    print("2. Execute o script models.py para recriar o banco")
    print("3. Use criar_admin.py para criar novos usuários")
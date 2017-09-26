
# ========== Tipos de Documentos de Pesssoa e herdeiras ========================
DCCPF = 'DCCPF'
DCCNPJ = 'DCCNPJ'
DCCNH = 'DCCNH'
DCRG = 'DCRG'
DCCTRTRAB = 'DCCTRTRAB'
DCCRTNASC = 'DCCRTNASC'
DCIE = 'DCIE'

DOCPF = (DCCRTNASC, DCCNH, DCCTRTRAB, DCRG)
DOCPJ = (DCCNPJ, DCIE)

# ================== Exceções ==================================================
NOMEERROR = 'NOMER'
ENDERERROR = 'ENDEER'
TELERROR = 'TELER'
EMAILERROR = 'EMAILER'
URLERROR = 'URLER'
LGRERROR = 'LGRERROR'
NUMERROR = 'NUMERROR'
COMERROR = 'COMERROR'
BAIERROR = 'BAIERROR'
CIDERROR = 'CIDERROR'
PAISERROR = 'PAISERROR'
CEPERROR = 'CEPERROR'
ESTERROR = 'ESTERROR'
CDPAISERROR = 'CDPAISERROR'
DDDERROR = 'DDDERROR'
NTELERROR = 'NTELERROR'
RMLERROR = 'RMLERROR'
EMSG = {NOMEERROR: 'Tipo inválido para o atributo "nome"',
       ENDERERROR: 'Tipo inválido para o atributo "endereco"',
       TELERROR: 'Tipo inválido para o atributo "telefone"',
       EMAILERROR: 'Tipo inválido para o atributo "email"',
       URLERROR: 'Tipo inválido para o atributo "site"',
       LGRERROR: 'Tipo inválido para o atributo "logradouro"',
       NUMERROR: 'Tipo inválido para o atributo "número"',
       COMERROR: 'Tipo inválido para o atributo "complememto"',
       BAIERROR: 'Tipo inválido para o atributo "bairro"',
       CIDERROR: 'Tipo inválido para o atributo "cidade"',
       PAISERROR: 'Tipo inválido para o atributo "país"',
       CEPERROR: 'Tipo inválido para o atributo "cep"',
       ESTERROR: 'Tipo inválido para o atributo "estado"',
       CDPAISERROR: 'Tipo inválido para o atributo "código do país do telefone"',
       DDDERROR: 'Tipo inválido para o atributo "DDD do telefone"',
       NTELERROR: 'Tipo inválido para o atributo "número do telefone"',
       RMLERROR:'Tipo inválido para o atributo "ramal do telefone"',
       }

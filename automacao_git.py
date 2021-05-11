import subprocess
import sys

PATH_SSH = '' # COM ':' e '/' no final -> git.prod.cloud.ihf:<racf>/

MENSAGEM_COMMIT = 'Initial Commit'

NOME_REPOSITORIO =  '' # SEM '/' -> 'importer'

NOME_DO_ARQUIVO = '' # COM EXTENSÃO -> 'importer.py'

CODIGO = '''

'''

class AutomacaoGit():

    def runGit(self, *args):
        return subprocess.check_call(['git'] + list(args))

    def createArchive(self):
        try:
            pythonFile = open(NOME_DO_ARQUIVO, 'w')
            pythonFile.write(CODIGO)
            pythonFile.close()
            print('Arquivo criado: ' + NOME_DO_ARQUIVO)
        except:
            print('Problemas na criação do arquivo!')
            sys.exit()

    def restartGit(self):
        try:
            subprocess.check_call(['rm', '-rf', '.git'])
        except:
            print('Problemas em limpar repositório!')
            sys.exit()
            
    def gitInit(self):
        try:
            self.runGit('init')
        except:
            print('Problemas em iniciar git local!')
            sys.exit()

    def gitAdd(self):
        try:
            self.runGit('add', NOME_DO_ARQUIVO)
            print('Arquivo adicionado ao commit: ' + NOME_DO_ARQUIVO)
        except:
            print('Problemas ao adicionar arquivo no git local!')
            sys.exit()

    def gitCommit(self):
        try:
            self.runGit('commit', '-m', MENSAGEM_COMMIT)
        except:
            print('Problemas ao commitar git local!')
            sys.exit()

    def getGitReference(self):
        try:
            self.runGit('remote', 'add', 'origin', 'git@' + PATH_SSH + NOME_REPOSITORIO)
            self.runGit('remote', 'set-url', 'origin', 'git@' + PATH_SSH + NOME_REPOSITORIO + '.git')
        except:
            print('Problemas em encontrar referência do git remoto (URL)!')
            sys.exit()

    def gitPush(self):
        try:
            self.runGit('push', '-u', 'origin', 'master')
        except:
            print('Problemas ao enviar arquivo para o repositório remoto! (URL)')
            sys.exit()

automacaoGit = AutomacaoGit()
automacaoGit.restartGit()
automacaoGit.createArchive()
automacaoGit.gitInit()
automacaoGit.gitAdd()
automacaoGit.gitCommit()
automacaoGit.getGitReference()
automacaoGit.gitPush()
print('Arquivo criado no repositório com sucesso!')

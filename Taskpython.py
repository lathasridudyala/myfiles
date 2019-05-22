from github import Github
def Addbranch():
    user='lathasridudyala'
    password='Lathas@1'
    g = Github("user", "password")
    repo1='Demo'
    try:
        sourcebranch=

        for repo in g.get_user().get_repos():

            if(repo==repo1):
                repo.get_branch(branch="sourcebranch")
                current = repo.create_head(targetbranch)
                current.checkout()
                repo.git.add(A=True)
                repo.git.commit(m='msg')
                repo.git.push('--set-upstream', 'origin', current)
                print('git push')
    except Exception as e:
        print(str(e))

if (__name__ == '__main__'):
    Addbranch()
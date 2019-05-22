
from github import Github
def Addbranch():

    try:
        user=input("enter username")
        password=input("enter password")
        #g=Github("f27946d8dd023bec12facb20580a199e3469de84")
        g=Github(user,password)
        Repo=g.get_repo("lathasridudyala/Demo")
        print(Repo.name)
        print(list(Repo.get_branches()))
        sourcebranch=input("enter sourcebranch")
        targetbranch=input("enter targetbranch")
        for r in Repo.get_branches():
            if(r==targetbranch):
                print("enter a valid branch name")
            else:
                branch=Repo.get_branch(branch=sourcebranch)
                print(branch.name)
                Repo.create_git_ref(ref='refs/heads/' + targetbranch, sha=branch.commit.sha)
    except Exception as e:
        print(str(e))
if (__name__ == '__main__'):
    Addbranch()
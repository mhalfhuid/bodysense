CREATE LOCAL REPO AND PUSH TO REMOTE


Requirements: remote repo already exists: git@github.com:mhalfhuid/bodysense.git


1) go to directory that is going to serve as a local repo
2) change dir into repo: 
	git init
3) adding all files to be tracked: 
	git add . 

4) commit files:
	git commit -m "first commit"

5) turn remote repo into main:
	git remote add origin git@github.com:mhalfhuid/bodysense.git

6) push content of local repo ot main:
	git push origin main



CLONE REMOTE REPO LOCALLY

1) go to directory where the new repo will be created
2) clone remote repo
	git clone git@github.com:mhalfhuid/bodysense.git




PUSH CONTENT FROM LOCAL TO REMOTE


1) go to local repo
2) add new file to tracked files:
	git add <new file>
3) commit new file
	git commit -m "new file added"
4) push content of local repo to main:
	git push origin main


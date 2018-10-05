import sys
import os

while True:
  print '1 Push a branch'
  print '2 Pull a branch'
  print '3 Checkout to a branch'
  print '4 Status'
  print '5 Create a new branch and checkout to it'
  print '6 Add all files'
  print '7 Add a single line commit in double quotes'
  print '8 Rename a branch'
  print '9 Delete a branch'
  print '10 List all branches and see the current branch'
  print '11 Exit'
  print 'Enter your choice'
  cmd = raw_input()

  if cmd == '1':
    print 'Enter branch name'
    branch = raw_input()
    os.system('git push origin '+branch)
  elif cmd == '2':
    print 'Enter branch name'
    branch = raw_input()
    os.system('git pull origin '+branch)
  elif cmd == '3':
    print 'Enter branch name to be checkout'
    checkout = raw_input()
    os.system('git checkout '+checkout)
  elif cmd == '4':
    os.system('git status')
  elif cmd == '5':
    print 'Enter branch name'
    new_branch = raw_input()
    os.system('git checkout -b '+new_branch)
  elif cmd == '6':
    os.system('git add .')
  elif cmd == '7':
    print 'Enter commit message'
    message = raw_input()
    os.system('git commit -m '+message)
  elif cmd == '8':
    print 'Enter new branch name'
    new = raw_input()
    os.system('git branch -m '+new)
  elif cmd == '9':
    print 'Please make sure you are not on the same branch which needs to be deleted'
    print 'Enter branch to be deleted'
    delete = raw_input()
    os.system('git branch -D '+delete)
  elif cmd == '10':
    os.system('git branch')
  elif cmd == '11':
    sys.exit() 
  else:
    print 'Something Went Wrong!'

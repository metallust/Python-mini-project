import sqlite3
import os
import sys
from irfan import init, add, commit
from gaurav import clone, push, pull
from yogesh import log


def main():
    command = sys.argv[1]
    match command:
        # git.py init
        case 'init':
            if len(sys.argv) != 2:
                sys.exit('Invalid command => Usage: git.py init')
            init()
        # git.py add <file>
        case 'add':
            #  check the len of the sys.argv
            if len(sys.argv) != 3:
                sys.exit('Invalid command => Usage: git.py add <file>')
            
            #  check if database exists
            if not os.path.exists('.zit/database.db'):
                sys.exit('error: zit is not initialized')

            # check if atleast one file is given
            # try:
            print(os.getcwdb())
            add(os.getcwdb())
            # except Exception as e:
            #     print(e)
            #     sys.exit('error: something went wrong')
            print('File added successfully')
        # git.py commit -m <message>
        case 'commit':
            if len(sys.argv) != 4:
                sys.exit('Invalid command => Usage: git.py commit -m <message> 1')
            if sys.argv[2] != '-m':
                sys.exit('Invalid command => Usage: git.py commit -m <message> 2')
            message = sys.argv[3]
            commit(message)
        case 'push':
            if len(sys.argv) != 2:
                sys.exit('Invalid command => Usage: git.py push 1')
            push()

            pass
        case 'pull':
            if len(sys.argv) != 2:
                sys.exit('Invalid command => Usage: git.py pull 1')
            pull() 
            pass
        case 'clone':
            if len(sys.argv) != 2:
                sys.exit('Invalid command => Usage: git.py clone 1')
            clone()
        # git.py status
        # case 'status':
        #     status()
        
        # git.py log
        case 'log':
            if len(sys.argv) != 2:
                sys.exit('Invalid command => Usage: git.py clone 1')
            log()
            
        case _:
            print('Invalid command => Usage: git.py <command> <options>')
            
if __name__ == '__main__':
    main()
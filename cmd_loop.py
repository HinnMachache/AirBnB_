#!/usr/bin/env python3
import cmd

class Handle_commands(cmd.Cmd):
    """ Cmd class to handle commands"""

    prompt = '($)'

    def do_greet(self, line):
        """ Return Hello $user"""
        if line:
            print(f"Hello {line}")
        else:
            print('Hello, world ')    
    
    def do_EOF(self, line):
        """ Exit the program"""
        return True
    
    def postloop(self) -> None:
        print
    
if __name__ == "__main__":
    Handle_commands().cmdloop()
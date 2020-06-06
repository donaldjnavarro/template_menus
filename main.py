import cmd

class prompt(cmd.Cmd):
    """Global prompt. This class creates the default prompt interface. All menus should inherit this class"""
    prompt = ": "
    
    def cmdloop(self, intro=None):
        """aka the PREpreloop"""
        # Name the current menu
        global here
        here = "main"
        # List menu options
        global options
        options = [about, info]
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        """When first arriving at this this class, or any inheriting class"""
        global here, options
        self.do_menu(False)

    def do_quit(self, arg):
        """Close the program"""
        quit()
    
    def emptyline(self):
        # return cmd.Cmd.emptyline(self) # this will repeat the last entered command
        return False

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)

    def do_home(self, arg):
        """Navigate to the first menu"""
        # is this redundant with menu command? Should we instead always populate main into the options list?
        choice = main
        return True

    def do_back(self,arg):
        """Navigate to the previous menu"""
        global history, choice
        if len(history) > 1: # only go back if theres a menu before the current active menu
            history.pop(-1)
            choice = history[-1]
            history.pop(-1) # remove the new destination because it will be added in __main__ loop
            return True
        else:
            print("Can't go back.",(history[0].__name__).title(),"is the only thing in our history.")

    def do_menu(self, arg):
        """Without an argument to display the available menus, with an argument to open a specified menu."""
        global options, here
        # Display the menu list
        if not arg:
            print("Current menu:",(here).title())
            if options:
                print("The following options are available:")
                for option in options:
                    print("  "+(str(option.__name__)).title())
            return False
        # Validate arg matches an option
        # Grab the list key for the selected option so we can use it to call a prompt
        for key, val in enumerate(options): 
            str(val.__name__)
            if str(val.__name__) == arg:
                argKey = key
        try:
            global choice
            choice = options[argKey]
            return True
        except:
            print("That was not a valid option. Pick an item from the list.")
            return False

class main(prompt):
    """Top level menu"""
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "main"
        global options
        options = [about, info]
        return cmd.Cmd.cmdloop(self, intro)

class about(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "about"
        global options
        options = [main, info]
        return cmd.Cmd.cmdloop(self, intro)

class info(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "info"
        global options
        options = [main, about]
        return cmd.Cmd.cmdloop(self, intro)

if __name__ == '__main__':
    running = True
    choice = main # First menu class
    print("Starting root menu...")
    history = []
    while running == True:
        history.append(choice)
        choice().cmdloop()

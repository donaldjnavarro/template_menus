import cmd
import datetime

class prompt(cmd.Cmd):
    """Global prompt. This class creates the default prompt interface. All menus should inherit this class"""
    prompt = "(Type help to display the commands currently available)\n: "
    
    def cmdloop(self, intro=None):
        """aka the PREpreloop"""
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        """When first arriving at this this class, or any inheriting class"""
        # Print the menu
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
        global options, here, choice
        # Display the menu list
        if not arg:
            print("   <- Back to:",(history[-2]).__name__.title()) if len(history) > 1 else False
            print("  Active Menu:",(here).title())
            menuTitled = False
            menuTitle = "      Choices: "
            # Display global menu options
            for option in options["global"]:
                if here != option.__name__: # Don't display the currently active menu
                    leftRail = menuTitle if menuTitled == False else "               " # Only print the options header on the first line
                    menuTitled = True # toggle to remember that options header has been set
                    print(leftRail+(str(option.__name__)).title())
            if options[here]:
                # Display local menu options, repeat logic used on globals above
                for option in options[here]:
                    if here != option.__name__:
                        leftRail = menuTitle if menuTitled == False else "               "
                        menuTitled = True
                        print(leftRail+(str(option.__name__)).title())
            return False
        # Validate arg matches an option
        # Grab the list key for the selected option so we can use it to call a prompt
        for key, val in enumerate(options["global"]): 
            str(val.__name__)
            if str(val.__name__) == arg:
                argKey = key
                choice = options["global"][argKey]
                return True
        for key, val in enumerate(options[here]): 
            str(val.__name__)
            if str(val.__name__) == arg:
                argKey = key
        try:
            choice = options[here][argKey]
            return True
        except:
            print("That was not a valid option. Pick an item from the list.")
            return False

class home(prompt):
    """Top level menu. This menu is always an available options from any other menu"""
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "home"
        return cmd.Cmd.cmdloop(self, intro)

class about(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "about"
        return cmd.Cmd.cmdloop(self, intro)
    
    def do_info(self, arg):
        """Display info about this app"""
        print("This is a project to create a template for a broader menu implementation via the cmd module.")

class tools(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "tools"
        return cmd.Cmd.cmdloop(self, intro)

class math(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "math"
        return cmd.Cmd.cmdloop(self, intro)

    def do_float(self, arg):
        """Display an example of a floating point error"""
        print("1.2 - 1.0 =",1.2-1.0)

class calendar(prompt):
    def cmdloop(self, intro=None):
        """Before the inherited class's preloop"""
        global here
        here = "calendar"
        return cmd.Cmd.cmdloop(self, intro)

    def do_date(self, arg):
        """Display the current date and time"""
        print(datetime.datetime.now())

if __name__ == '__main__':
    running = True
    print("Starting root menu...")
    history = []
    choice = home # First menu class
    options = {
        "global": [home],
        "home": [about, tools],
        "about": [],
        "tools": [math, calendar],
        "math": [],
        "calendar": []
    }
    while running == True:
        history.append(choice)
        choice().cmdloop()

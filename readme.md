# Scope
This project is to explore using the cmd module to create menu systems

# Design
- Unique menu interfaces are created via cmd classes that inherit the prompt class
- Back command navigates the user to the previous menu, based on their activity which is tracked in the history var list
- Menu options for each menu are stored in a dictionary in __main__ 
- Global menu options are stored in the options dictionary and are available in every menu
- Menu command without an argument displays the list of menus that can be opened from a given location
- Menu command with an argument navigates to the menu specified

# Todo
- Need to improve the relationships between menus to be more programmatic, instead of manually setting them to point at each other
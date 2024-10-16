from ti_system import disp_clr
class Menu_System:
    def __init__(self, menu_structure):
        self.menu_structure = menu_structure
        self.current_menu = menu_structure["Main Menu"]

    def run(self):
        self.navigate_menu(self.current_menu)

    def navigate_menu(self, menu):
        disp_clr()
        print(menu["title"])
        options = menu["options"]

        if isinstance(options, dict) and options:  # Check if options is a non-empty dictionary
            # Display options
            for idx, option in enumerate(options, 1):
                print(str(idx) + ". " + str(option))

            # Get user choice
            choice = self.get_valid_choice(len(options))

            selected_key = list(options.keys())[choice - 1]  # Adjusted for 1-based menu display
            selected_option = options[selected_key]

            # Check if selected option is a menu, function, or "Back"
            if selected_key == "Back":
                return  # Go back to the previous menu

            if isinstance(selected_option, dict):
                self.navigate_menu(selected_option)
            elif callable(selected_option):
                selected_option()  # Call the function
                input("Press any key to return to the main menu.")
                self.current_menu = self.menu_structure["Main Menu"]
                self.navigate_menu(self.current_menu)  # Avoid recursion by looping
        else:
            print("No options available.")
            input("Press any key to return to the previous menu.")
            return

    def get_valid_choice(self, num_options):
        while True:
            try:
                choice = int(input("Select an option: "))  # User enters option
                if 1 <= choice <= num_options:
                    return choice
                else:
                    print("Invalid input. Please enter a number between 1 and " + str(num_options))
            except ValueError:
                print("Invalid input. Please enter a valid number.")


import tkinter as tk
from tkinter import simpledialog
from program_logic import ProgramLogic

class SimulationPage(tk.Frame):
    """Simulation page for inputting automata, strings, and running simulations."""
    default_input_string = "No input string inputted yet..."
    default_automata_definition = "No automata definition inputted yet..."

    def __init__(self, parent, program_logic: ProgramLogic):
        super().__init__(parent)

        # NOTE: when combining all frames together, this will need to be rethought
        self.program_logic = program_logic 

        # window size
        self.master.geometry("2000x1000") # type: ignore
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        # input automata button, opens input text box popup when clicked 
        self.input_automata_button = tk.Button(
            button_frame, 
            text="Input Automata", 
            command=self.input_automata
            )
        self.input_automata_button.pack(side=tk.LEFT, padx=5)
        
        # input string button, opens input text box popup when clicked
        self.input_string_button = tk.Button(
            button_frame, 
            text="Input String", 
            command=self.input_string
            )
        self.input_string_button.pack(side=tk.LEFT, padx=5)
        
        # displays automata definition
        self.automata_def_label = tk.Label(self, text="No automaton inputted yet...")
        self.automata_def_label.pack(pady=10)

        # displays input string
        self.input_string_label = tk.Label(self, text=self.default_input_string)
        self.input_string_label.pack(pady=10)

        # Store the automata string
        self.automata_description = self.default_automata_definition

    def input_automata(self):
        """Popup for user to enter automata dsl description"""
        # popup window
        popup = tk.Toplevel(self)
        popup.title("Input Automata")
        popup.geometry("800x800") 
        # text box
        text_widget = tk.Text(popup, width=60, height=20)
        text_widget.pack(padx=10, pady=10)
        # button to accept user input            
        def compile_automata():
            self.program_logic.compile_automata(text_widget.get("1.0", "end-1c"))
            self.automata_def_label.config(text=self.program_logic.current_automata)
            self.input_string_label.config(text="No input string inputted yet...") # reset for new automaton
            popup.destroy()
        save_button = tk.Button(popup, text="Accept", command=compile_automata)
        save_button.pack(pady=10)

    def input_string(self):
        if self.program_logic.valid_automata:
            popup = tk.Toplevel(self)
            popup.title("Input String")
            popup.geometry("800x800")
            text_widget = tk.Text(popup, width=60, height=20)
            text_widget.pack(padx=10, pady=10)
            # button to accept user input
            def accept_input_string():
                self.program_logic.set_input_string(text_widget.get("1.0", "end-1c"))
                self.input_string_label.config(text=self.program_logic.input_string)
                popup.destroy()
            save_button = tk.Button(popup, text="Accept", command=accept_input_string)
            save_button.pack(pady=10)
        else:
            tk.messagebox.showerror(
                "Error", 
                "Valid automata must be inputted before inputting strings."
                )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulation Page")
    page = SimulationPage(root, ProgramLogic())
    page.pack(fill="both", expand=True)
    root.mainloop()
class DSLGenerator:
    """
    A class to generate DSL code based on the provided transitions and states.
    """

    def __init__(self):
        # Initialize the DSL output as an empty list
        self.output = []

    def start_file(self, timeout, external_name):
        """
        Starts the file by adding the timeout and external name definitions.
        """
        self.output.append(f"timeout {timeout}")
        self.output.append(f"external '{external_name}'\n")

    def add_step(self, step_name, receive_trigger, receive_constraint, send_trigger, send_constraint):
        """
        Adds a single step to the DSL output.
        This step includes the receive trigger and send constraints.
        """
        self.output.append(f"def {step_name}()")
        self.output.append(f"  receive '{receive_trigger}',")
        self.output.append(f"  constraint: {receive_constraint}")
        self.output.append(f"  send '{send_trigger}',")
        self.output.append(f"  constraint: {send_constraint}")
        self.output.append(f"end\n")

    def start_process(self, process_name):
        """
        Starts the process block in the DSL with the provided process name.
        """
        self.output.append(f"process('{process_name}'){{\n")

    def add_channel(self, channel_name):
        """
        Adds a channel definition to the process, which includes the stimuli and responses.
        """
        self.output.append(f"  channel('{channel_name}') {{")
        self.output.append("    stimulus 'visit', '_url' => :string")
        self.output.append("    stimulus 'click_link', 'selector' => :string")
        self.output.append("    response 'page_title', '_title' => :string, '_url' => :string")
        self.output.append("  }\n")

    def add_initial(self, initial_url, initial_constraint, initial_goto_state):
        """
        Defines the initial URL, state, and the conditions under which the system should transition.
        """
        # Define the initial_url variable
        self.output.append(f"  var 'initial_url', :string, '{initial_url}'\n")
        
        # Define the initial state 'start'
        self.output.append("  state 'start'")
        self.output.append("  receive 'visit',")
        self.output.append("  constraint: \"_url == initial_url\"")
        self.output.append("  send 'page_title',")
        self.output.append(f"  constraint: {initial_constraint}")
        self.output.append(f"  goto '{initial_goto_state}'\n")

    def add_state(self, name, on_action, goto_state):
        """
        Adds a state definition, with the actions associated with that state and its transition.
        """
        self.output.append(f"  state '{name}'")
        self.output.append(f"  {on_action}()")
        self.output.append(f"  goto '{goto_state}'\n")

    def finalize_process(self):
        """
        Finalizes the process block by closing the process definition.
        """
        self.output.append("}\n")

    def render(self):
        """
        Renders the generated DSL code as a single string.
        """
        return "\n".join(self.output)
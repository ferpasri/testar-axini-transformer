import json
from dsl.dsl_generator import DSLGenerator

# Function to map states based on their AbstractID and WebTitle
def map_states(json_states):
    return {ConcreteState['AbstractID']: ConcreteState['WebTitle'] for ConcreteState in json_states}

# Function to map actions, creating constraints based on the WebHref for each action
def map_actions(json_actions):
    return {
        action['AbstractID']: {
            'Desc': action['Desc'],
            'action_constraint': f"%(selector == \"a[href*='{action['WebHref']}']\")",
            'response': 'page_title',
        }
        for action in json_actions
    }

# Function to map transitions based on source, target, and associated actions
def map_transitions(json_transitions, concreteState, concreteAction):
    transitions = {}
    for transition in json_transitions:
        source = concreteState[transition['Source']]
        target = concreteState[transition['Target']]
        action = concreteAction[transition['Action']]
        if source not in transitions:
            transitions[source] = []
        transitions[source].append({
            'action': action['Desc'],
            'action_constraint': action['action_constraint'],
            'target': target,
        })
    return transitions

# Function to generate DSL code from the provided JSON data
def generate_dsl_from_json(json_data):
    # Initialize the DSLGenerator object
    dsl = DSLGenerator()

    # Start the file with timeout and external definitions
    dsl.start_file(30.0, "extern")

    # Map the states, actions, and transitions from the provided JSON data
    concreteState = map_states(json_data["ConcreteState"])
    concreteAction = map_actions(json_data["ConcreteAction"])
    concreteTransitions = map_transitions(json_data["ConcreteTransitions"], concreteState, concreteAction)

    unique_actions = set()

    # Add steps for each unique action
    for state, transitions in concreteTransitions.items():
        for transition in transitions:
            action_desc = transition['action']
            if action_desc not in unique_actions:
                unique_actions.add(action_desc)
                dsl.add_step(
                    step_name=action_desc.replace(" ", "_").replace("'", ""),  # Clean the action name
                    receive_trigger='click_link',
                    receive_constraint=transition['action_constraint'],
                    send_trigger='page_title',
                    send_constraint=f"%(_title == \"{transition['target']}\")",
                )
    
    # Start the process and add the initial state and channel
    dsl.start_process("testar")
    dsl.add_channel("extern")
    dsl.add_initial(
        initial_url=json_data["InitialUrl"],
        initial_constraint=f"%(_title == \"{json_data['InitialPage']}\")",
        initial_goto_state=json_data['InitialPage'],
    )

    # Add states and their transitions
    for state, transitions in concreteTransitions.items():
        dsl.output.append(f"  state '{state}'")
        dsl.output.append("    choice {")
        for transition in transitions:
            action_name = transition['action'].replace(" ", "_").replace("'", "")
            dsl.output.append(f"      o {{ {action_name}(); goto '{transition['target']}' }}")
        dsl.output.append("    }")
    
    # Finalize the process
    dsl.finalize_process()

    # Render and return the DSL code as a string
    return dsl.render()

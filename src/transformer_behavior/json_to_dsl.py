import json
from transformer_behavior.dsl_generator import DSLGenerator

# Function to map states based on their AbstractID and WebTitle
def map_states(json_states):
    return {ConcreteState['AbstractID']: ConcreteState['WebTitle'] for ConcreteState in json_states}

# Function to map actions, creating constraints based on the WebHref for each action
def map_actions(json_actions):
    return {
        action['AbstractID']: {
            'Desc': action['Desc'].replace(" ", "_").replace("'", ""),
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
    dsl = DSLGenerator()
    dsl.start_file(10.0, "extern")

    concreteState = map_states(json_data["ConcreteState"])
    concreteAction = map_actions(json_data["ConcreteAction"])
    concreteTransitions = map_transitions(json_data["ConcreteTransitions"], concreteState, concreteAction)

    unique_actions = set()

    for state, transitions in concreteTransitions.items():
        for transition in transitions:
            action_desc = transition['action']
            if action_desc not in unique_actions:
                unique_actions.add(action_desc)
                dsl.add_step(
                    step_name=action_desc,
                    receive_trigger='click_link',
                    receive_constraint=transition['action_constraint'],
                    send_trigger='page_title',
                    send_constraint=f"%(_title == \"{transition['target']}\")",
                )

    dsl.start_process("testar")
    dsl.add_channel("extern")
    dsl.add_behavior("launch", "", json_data["InitialPage"], True)

    for state, transitions in concreteTransitions.items():
        behavior_name = state
        dsl.add_behavior(behavior_name, ":non_terminating", state, False)
        for transition in transitions:
            action_name = transition['action']
            dsl.output.append(f"      o {{ {action_name}(); behave_as '{transition['target']}' }}")
        dsl.output.append("    }")
        dsl.output.append("  }")

    dsl.add_initial(
        initial_url=json_data["InitialUrl"],
        initial_state=json_data['InitialPage'],
    )

    dsl.finalize_process()

    return dsl.render()

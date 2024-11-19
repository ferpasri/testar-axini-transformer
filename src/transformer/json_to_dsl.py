import json
from dsl.dsl_generator import DSLGenerator

def map_states(json_states):
    return {state['id']: state['title'] for state in json_states}

def map_actions(json_actions):
    return {
        action['id']: {
            'desc': action['desc'],
            'action_constraint': f"%(selector == \"a[href*='{action['webHref']}']\")",
            'response': 'page_title',
        }
        for action in json_actions
    }

def map_transitions(json_transitions, state_map, actions):
    transitions = []
    for transition in json_transitions:
        source = state_map[transition['sourceStateId']]
        target = state_map[transition['targetStateId']]
        action = actions[transition['actionId']]
        transitions.append({
            'source': source,
            'action': action['desc'],
            'action_constraint': action['action_constraint'],
            'target': target,
        })
    return transitions

def generate_dsl_from_json(json_data):
    dsl = DSLGenerator()

    dsl.start_file(30.0, "extern")

    # Map states, actions, and transitions
    state_map = map_states(json_data["states"])
    actions = map_actions(json_data["actions"])
    transitions = map_transitions(json_data["transitions"], state_map, actions)

    for transition in transitions:
        dsl.add_step(
            step_name=transition['action'].replace(" ", "_").replace("'", ""),
            receive_trigger='click_link',
            receive_constraint=transition['action_constraint'],
            send_trigger='page_title',
            send_constraint=f"%(_title == \"{transition['target']}\")",
        )

    dsl.start_process("testar")

    dsl.add_channel("extern")

    dsl.add_initial(
        initial_url=json_data["initial_url"],
        initial_constraint=f"%(_title == \"{json_data['initial_title']}\")",
        initial_goto_state=json_data['initial_title'],
    )

    for transition in transitions:
        dsl.add_state(
            name=transition['source'],
            on_action=transition['action'].replace(" ", "_").replace("'", ""),
            goto_state=transition['target']
        )

    # Finalize and return DSL output
    dsl.finalize_process()
    return dsl.render()

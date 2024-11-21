import json
from dsl.dsl_generator import DSLGenerator

def map_states(json_states):
    return {ConcreteState['AbstractID']: ConcreteState['WebTitle'] for ConcreteState in json_states}

def map_actions(json_actions):
    return {
        action['AbstractID']: {
            'Desc': action['Desc'],
            'action_constraint': f"%(selector == \"a[href*='{action['WebHref']}']\")",
            'response': 'page_title',
        }
        for action in json_actions
    }

def map_transitions(json_transitions, concreteState, concreteAction):
    concreteTransitions = []
    for transition in json_transitions:
        source = concreteState[transition['Source']]
        target = concreteState[transition['Target']]
        action = concreteAction[transition['Action']]
        concreteTransitions.append({
            'source': source,
            'action': action['Desc'],
            'action_constraint': action['action_constraint'],
            'target': target,
        })
    return concreteTransitions

def generate_dsl_from_json(json_data):
    dsl = DSLGenerator()

    dsl.start_file(30.0, "extern")

    # Map ConcreteState, ConcreteAction, and ConcreteTransitions
    concreteState = map_states(json_data["ConcreteState"])
    concreteAction = map_actions(json_data["ConcreteAction"])
    concreteTransitions = map_transitions(json_data["ConcreteTransitions"], concreteState, concreteAction)

    for transition in concreteTransitions:
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
        initial_url=json_data["InitialUrl"],
        initial_constraint=f"%(_title == \"{json_data['InitialPage']}\")",
        initial_goto_state=json_data['InitialPage'],
    )

    for transition in concreteTransitions:
        dsl.add_state(
            name=transition['source'],
            on_action=transition['action'].replace(" ", "_").replace("'", ""),
            goto_state=transition['target']
        )

    # Finalize and return DSL output
    dsl.finalize_process()
    return dsl.render()

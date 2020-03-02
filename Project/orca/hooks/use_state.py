from ..state import State




def use_state(state_name :str, initial_value = None):

    state= State({
        state_name: initial_value
    })

    state_type= type(initial_value)

    def set_state(value):
        if type(value) != state_type:
            raise ValueError(f'Expected {state_type} but got {type(value)} :(')
        state.set_state({state_name: value})

    return  state , set_state




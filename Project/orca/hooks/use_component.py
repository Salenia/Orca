from ..component import Component
from ..state import State

component_name= ""
state= None
new_locals= {}
__get_class = lambda component_name, state, new_locals: 0
exec(f'''
def __get_class(component_name, state, new_locals):
    class component_name(Component):

        def __init__(self, root, **kwargs):

            super().__init__(root, state=State(state))

            
        def render(self):
            return new_locals

    return component_name
''')

def use_component(component_name ="UseComponent"):

    def __outer_warpper__(func):
        if type(component_name) != str:
            raise ValueError('Expected REAL component name dumbass')

        def __wrapper(*args, **kwargs) -> Component:

            if not func:
                raise AttributeError(f'Expected function, got {func}')

            new_render = func(*args, **kwargs)
            if not new_render:
                raise ValueError(f'Expected locals(), got None :(\nRemember to always return locals()')

            new_locals = {} 
            state={}
            for id, value in new_render.items():
                if type(value) != State:
                    new_locals[id] = value
                else:
                    state[id] = value.data

            new_component = __get_class(component_name, state, new_locals)
            if not new_component:
                new_component= lambda *args, **kwargs: 0


            return new_component(args, kwargs)

        return __wrapper
    return __outer_warpper__



    
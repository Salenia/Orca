from abc import abstractmethod, ABC
import tkinter as tk 
from .state import State



class Component(tk.Frame, ABC):

    _state: State
    _component_childs: dict
    _child_state: [dict]
    _items: dict
    __TYPE__: str
    __ROOT__= None



    def __init__(self, root, state : State =None) -> object:

        super().__init__(root)
        self.__TYPE__= 'Component'
        Component.__ROOT__ = None
        if type(root) == tk.Tk:
            Component.__ROOT__ = root
    
        self.root = root
        self._child_state = {}

        if state and type(state) == State:
            self._state = state

            self._state.bind_to(self.__unmount__)
            self._state.bind_to(self.__render__)

        self.__update_items__(self.render())
        #self.__component_will_mount__()
        
    @property
    def state(self):
        return self._state

        
    def __unmount__(self):
        for id, child in self._items.items():
            if '__TYPE__' in list(vars(child)):
                self._child_state[id] = child.state 
            if 'destroy' in list(dir(child)):
                child.destroy()    
        
        del self._items

        self._items= {}

    def __update_items__(self, items):
        del items['self']
        self._items= items
            

    def __render__(self):
        self.__update_items__(self.render())
        self.__post_render__()

    def __post_render__(self):
        for id , child in self._items.items():
            if self._child_state and '__TYPE__' in list(vars(child)):
                x= self._child_state[id].data
                child._state = State({**x})
                child.state.bind_to(child.__unmount__)
                child.state.bind_to(child.__render__)
                child._state.set_state({})


    def __component_will_mount__(self):
        for id, child in self._items.items():
            if '__TYPE__' in list(vars(child)):
                self._child_state[id] = child.state
    
    @abstractmethod
    def render(self):
        return locals()
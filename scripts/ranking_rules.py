import dataclasses
from typing import Callable

import reacton.ipyvuetify as v

import solara
from solara.lab.toestand import Ref
from scripts import init_values


class State:
    rules = solara.reactive(init_values.initial_items)
    
    start_point = solara.reactive(0)
    finish_point = solara.reactive(0)
    rank_point = solara.reactive(0)

    
    def on_delete(item: init_values.RuleItem):
        new_items = list(State.rules.value)
        new_items.remove(item)
        State.rules.value = new_items
    
    def new_rule():
        State.rules.value = State.rules.value + [init_values.RuleItem(rank_value.value, start_point.value, finish_point.value, rank_point.value)]
        State.start_point.set(0)
        State.finish_point.set(0)
        State.rank_point.set(0)

    
    @solara.component
    def RankListItem(rule):
        editing, set_editing = solara.use_state(False)

        with v.ListItem():

            solara.InputInt("From", value=rule.start)
            solara.InputInt("To", value=rule.finish)
            solara.InputInt("Rank", value=rule.value)


            solara.Column(children=[
                (
                    solara.IconButton(icon_name="save", on_click=lambda: set_editing(False))
                    if editing 
                    else 
                    solara.IconButton(icon_name="edit", on_click=lambda: set_editing(True))
                ),
                solara.IconButton(icon_name="delete", on_click=lambda: State.on_delete(rule))
            ])


rank_values = ["rsi", "adx", "max_52_week"]
rank_value = solara.reactive("rsi")

def rank_value_changed(new_value):
    rank_value.value = new_value


indicator_weights = {
    "rsi": 0,
    "adx": 0,
    "max_52_week": 0,
    
}

temp_value = solara.reactive(0)

def weight_changed(new_value):
    indicator_weights[rank_value.value] = new_value
    
def calculate_rank():
    pass
    
@solara.component
def rank_tab():
    with solara.Card("Todo list", style="min-width: 500px"):    
        solara.ToggleButtonsSingle(value=rank_value, values=rank_values, on_value=rank_value_changed)
        
        
        temp_value.value = indicator_weights[rank_value.value]
        
        solara.SliderInt("Indicator weight:", value=temp_value, on_value=weight_changed, min=-10, max=10)
        
        print(indicator_weights)
        
        solara.Markdown("**Current rules:**")
        
        for index, item in enumerate(State.rules.value):
            if item.indicator == rank_value.value:
                State.RankListItem(item)
        
        solara.Markdown("**New rule:**")
        
        with solara.HBox():
            solara.InputInt("From", value=start_point)
            solara.InputInt("To", value=finish_point)
            solara.InputInt("Rank", value=rank_point)
            solara.Button("Add", on_click=new_rule, classes=["primary", "add-button"])

        
        solara.Button("Calculate rank", on_click=calculate_rank, classes=["primary", "add-button"], style='margin-top: 20px; text-align: center;')

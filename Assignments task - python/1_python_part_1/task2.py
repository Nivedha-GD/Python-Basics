"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict

items_to_set_key=[]
items_to_set_value=[]

def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    
    
    if len(dict_to_update)==0:
        return dict_to_update

    if not items_to_set:
        return dict_to_update

    for key, value in items_to_set.items():
        items_to_set_key.append(key)
        items_to_set_value.append(value)   
    #print(items_to_set_key)

    for i in range(len(items_to_set_key)):
        if dict_to_update[items_to_set_key[i]]<items_to_set_value[i]:
            dict_to_update[items_to_set_key[i]]=items_to_set_value[i]

    print(dict_to_update)
            

set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)
set_to_dict({}, a=0)
set_to_dict({'a': 5})
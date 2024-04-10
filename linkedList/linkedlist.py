head = {
    "value" : 11,
    "next" : {
        "value": 4,
        "next": {
            "value": 20,
            "next": {
                "value": 30,
                "next": None
            }
        }
    }
}

# LinkedList Traversal

linkedListValues = []

def getValues(ll:dict):
    linkedListValues.append(ll["value"])
    
    if ll["next"] == None:
        return linkedListValues
    else:
        return getValues(ll["next"])    

print(getValues(head))

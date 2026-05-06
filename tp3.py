# ex1
rules = [
    {"if": ["condition1"], "then": "conclusion1"},
    {"if": ["condition2"], "then": "conclusion2"}
]


facts = ["fact1", "fact2"]
# ex2
def forward_chaining(rules, facts, goal):
    inferred = True

    while inferred:
        inferred = False
        for rule in rules:
          
            if all(cond in facts for cond in rule["if"]):
                if rule["then"] not in facts:
                    facts.append(rule["then"])
                    inferred = True

                    print("It was concluded:", rule["then"])

                    if rule["then"] == goal:
                        return True
    return False



facts = ["condition1"]
goal = "conclusion1"

print("rzl:", forward_chaining(rules, facts, goal))
# ex3
rules = [
    [["condition1", "condition2"], "conclusion1"],
    [["condition3"], "conclusion2"]
]

facts = ["fact1", "fact2"]
# ex4
def forward_chaining_list(rules, facts, goal):
    inferred = True

    while inferred:
        inferred = False
        for rule in rules:
            conditions = rule[0]
            conclusion = rule[1]

            if all(cond in facts for cond in conditions):
                if conclusion not in facts:
                    facts.append(conclusion)
                    inferred = True

                    print("concluded:", conclusion)

                    if conclusion == goal:
                        return True
    return False



facts = ["condition1", "condition2"]
goal = "conclusion1"

print("rzl:", forward_chaining_list(rules, facts, goal))
# ex5
def backward_chaining(rules, facts, goal):
  
    if goal in facts:
        return True

    for rule in rules:
        if rule["then"] == goal:
           
            if all(backward_chaining(rules, facts, cond) for cond in rule["if"]):
                return True

    return False



rules = [
    {"if": ["A", "B"], "then": "C"},
    {"if": ["C"], "then": "D"}
]

facts = ["A", "B"]

goal = "D"

print("rzl:", backward_chaining(rules, facts, goal))

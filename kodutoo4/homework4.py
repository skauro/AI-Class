def forward_chaining(clauses, query):
    inferred = set()
    new_symbols = True  # loop while we infer new stuff
    while new_symbols:
        new_symbols = False
        for clause in clauses:
            premises, conclusion = clause
            # if all premises are inferred and conclusion is not yet inferred
            if all(premise in inferred for premise in premises) and conclusion not in inferred:
                if conclusion == query:
                    return True
                inferred.add(conclusion)
                new_symbols = True
    return False  # no new symbols, query symbol was not seen


# Test Problem
clauses = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["B", "L"], "M"),
    (["A", "P"], "L"),
    (["A", "B"], "L"),
    ([], "A"),
    ([], "B")
]


# Egg Problem
egg_clauses = [
    ([], "Fragile"),
    ([], "FallsDown"),
    ([], "ContainsLiquid"),
    (["Fragile", "FallsDown"], "Breaks"),
    (["Breaks", "ContainsLiquid"], "MakesMess"),
    (["Spoiled", "Breaks"], "Smells")
]

# Prove that Q is entailed
print("Is Q entailed?", forward_chaining(clauses, "Q"))  # Should print True


# Prove that the egg a.) breaks, b.) makes a mess, c.) smells
print("Does the egg break?", forward_chaining(egg_clauses, "Breaks"))  # Should print True
print("Does the egg make a mess?", forward_chaining(egg_clauses, "MakesMess"))  # Should print True
print("Does the egg smell?", forward_chaining(egg_clauses, "Smells"))
# Should print False (since "Spoiled" is not given)

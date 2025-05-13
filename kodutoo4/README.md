Is Q entailed? True

Does the egg break? True

Does the egg make a mess? True

Does the egg smell? False

input : 
egg_clauses = [
    ([], "Fragile"),                      # "Egg is fragile."

    ([], "FallsDown"),                    # "Egg falls down."

    ([], "ContainsLiquid"),               # "Egg contains liquid."

    (["Fragile", "FallsDown"], "Breaks"), # "If the egg is fragile and it falls down, it breaks."

    (["Breaks", "ContainsLiquid"], "MakesMess"), # "If the egg breaks and it contains liquid, it makes a mess."

    (["Spoiled", "Breaks"], "Smells")     # "If the egg is spoiled and it breaks, it smells."
]
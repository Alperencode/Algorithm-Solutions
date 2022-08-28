def cakes(recipe, available):
    if not recipe or not available:
        return 0
    for key in recipe:
        if key not in available:
            return 0
    for key in recipe:
        if recipe[key] > available[key]:
            return 0
    
    return min(available[key] // recipe[key] for key in recipe)

# Testcases
# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# 2

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# 0

# Status - Passed
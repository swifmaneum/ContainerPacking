def part_fits_in_module(part, module):
    return (module.length >= part.length and module.width + module.jut >= part.width) or (
            module.length >= part.width and module.width + module.jut >= part.length)


def calculate_wasted_space(part, module):
    return module.length * (module.width + module.jut) - part.width * part.length


def get_best_fitting_module(part, modules):
    # Filter out all modules, that the part won't fit in
    feasible_modules = filter(lambda module: part_fits_in_module(part, module), modules)
    modules_to_wasted_space = {}
    for module in feasible_modules:
        wasted_space = calculate_wasted_space(part, module)
        modules_to_wasted_space[module] = wasted_space
    if len(modules_to_wasted_space) == 0:
        # If no fitting module exists, return none
        return None, None
    else:
        result = min(modules_to_wasted_space, key=modules_to_wasted_space.get)
        return result, modules_to_wasted_space[result]


def get_first_fitting_module(part, modules):
    # Filter out all modules, that the part won't fit in
    feasible_modules = filter(lambda module: part_fits_in_module(part, module), modules)
    first_module = next(feasible_modules, None)
    if first_module:
        return first_module, calculate_wasted_space(part, first_module)
    else:
        # If no fitting module exists, return none
        return None, None

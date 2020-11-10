def part_fits_in_module(part, module):
    return (module.length >= part.length and module.width >= part.width) or (
            module.length >= part.width and module.width >= part.length)


def calculate_wasted_space(part, module):
    return module.length * module.width - part.width * part.length


def is_best_fitting_module(decision, part, modules) -> bool:
    """
    Returns a boolean whether a given decision for a given part is the best fitting module.
    If no fitting modules is available, return false.
    """
    feasible_modules = list(filter(lambda m: part_fits_in_module(part, m) and m.capacity > 0, modules))
    modules_to_wasted_space = {}
    for module in feasible_modules:
        wasted_space = calculate_wasted_space(part, module)
        modules_to_wasted_space[module] = wasted_space

    if len(modules_to_wasted_space) == 0:
        return False
    else:
        best_fitting_module = min(modules_to_wasted_space, key=modules_to_wasted_space.get)
        return decision == modules.index(best_fitting_module)

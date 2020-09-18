def part_fits_in_module(part, module):
    return (module.length >= part.length and module.width >= part.width) or (
            module.length >= part.width and module.width >= part.length)


def calculate_wasted_space(part, module):
    return module.length * module.width - part.width * part.length


def get_best_fitting_module(nn_decision, part, modules):
    feasible_modules = list(filter(lambda m: part_fits_in_module(part, m) and m.capacity > 0, modules))
    modules_to_wasted_space = {}
    for module in feasible_modules:
        wasted_space = calculate_wasted_space(part, module)
        modules_to_wasted_space[module] = wasted_space
    if len(modules_to_wasted_space) == 0:
        if nn_decision == 6:
            return 1
        else:
            return 0
    else:
        fitting_module = min(modules_to_wasted_space, key=modules_to_wasted_space.get)
        if nn_decision == fitting_module.number:
            return 1
        else:
            return 0

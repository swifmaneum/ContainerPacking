% ----------------------------------------
% Decision variables
% ----------------------------------------
array[PART] of var int: wasted_space;

% ----------------------------------------
% Constraints
% ----------------------------------------
constraint forall(i in PART) (
  wasted_space[i] = module_lengths[allocation[i]]* (module_widths[allocation[i]] + module_juts[allocation[i]]) - widths[i] * lengths[i]
);

solve minimize sum(wasted_space);

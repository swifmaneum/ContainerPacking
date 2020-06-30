include "globals.mzn"; 

% ----------------------------------------
% Input data
% ----------------------------------------
int: n_parts;
set of int: PART = 1..n_parts;

array[PART] of int: lengths;
array[PART] of int: widths;
array[PART] of int: weights;

int: n_modules;
set of int: MODULE = 1..n_modules;

array[MODULE] of int: module_lengths;
array[MODULE] of int: module_widths;
array[MODULE] of int: module_juts;
array[MODULE] of int: module_capacity;

% ----------------------------------------
% Decision variables
% ----------------------------------------
array[PART] of var MODULE: allocation;
array[PART] of var int: wasted_space;
var int: wasted_space_sum;

% ----------------------------------------
% Constraints
% ----------------------------------------
constraint forall(i in PART) (
    (module_lengths[allocation[i]] >= lengths[i] /\ module_widths[allocation[i]] + module_juts[allocation[i]] >= widths[i])
    \/ (module_lengths[allocation[i]] >= widths[i] /\ module_widths[allocation[i]] + module_juts[allocation[i]] >= lengths[i])
);

constraint bin_packing_capa(module_capacity, allocation, weights);


constraint forall(i in PART) (
  wasted_space[i] = module_lengths[allocation[i]]* (module_widths[allocation[i]] + module_juts[allocation[i]]) - widths[i] * lengths[i]
);

constraint wasted_space_sum = sum(wasted_space);

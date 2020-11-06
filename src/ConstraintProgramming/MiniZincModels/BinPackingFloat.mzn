include "globals.mzn"; 

% ----------------------------------------
% Input data
% ----------------------------------------
int: n_parts;
set of int: PART = 1..n_parts;

array[PART] of float: lengths;
array[PART] of float: widths;
array[PART] of int: weights;

int: n_modules;
set of int: MODULE = 1..n_modules;

array[MODULE] of float: module_lengths;
array[MODULE] of float: module_widths;
array[MODULE] of int: module_capacity;

% ----------------------------------------
% Decision variables
% ----------------------------------------
array[PART] of var MODULE: allocation;
array[PART] of var float: wasted_space;
var float: wasted_space_sum;

% ----------------------------------------
% Constraints
% ----------------------------------------
constraint forall(i in PART) (
    (module_lengths[allocation[i]] >= lengths[i] /\ module_widths[allocation[i]] >= widths[i])
    \/ (module_lengths[allocation[i]] >= widths[i] /\ module_widths[allocation[i]] >= lengths[i])
);

constraint bin_packing_capa(module_capacity, allocation, weights);


constraint forall(i in PART) (
  wasted_space[i] = module_lengths[allocation[i]] * module_widths[allocation[i]] - widths[i] * lengths[i]
);

constraint wasted_space_sum = sum(wasted_space);

solve :: int_search(allocation, first_fail, indomain_min)
      minimize wasted_space_sum;
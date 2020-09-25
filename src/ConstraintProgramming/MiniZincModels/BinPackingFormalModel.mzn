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
array[MODULE] of int: module_capacity;

int: max_wasted_space = sum(m in MODULE)(module_capacity[m] * module_lengths[m]* module_widths[m]);

% ----------------------------------------
% Decision variables
% ----------------------------------------
array[1..n_modules,1..n_parts] of var bool: allocation;
array[PART] of var 0..max_wasted_space: wasted_space;
var 0..max_wasted_space: wasted_space_sum;

% ----------------------------------------
% Constraints
% ----------------------------------------
constraint forall(m in MODULE)(
  sum(row(allocation, m)) <= module_capacity[m]
);

constraint forall(p in PART)(
  sum(col(allocation, p)) = 1
);

constraint forall(m in MODULE, p in PART)(
  allocation[m,p] -> 
  (module_lengths[m] >= lengths[p] /\ module_widths[m] >= widths[p])
    \/ (module_lengths[m] >= widths[p] /\ module_widths[m] >= lengths[p])
);

constraint forall(m in MODULE, p in PART)(
  allocation[m,p] -> 
  wasted_space[p] = module_lengths[m]* module_widths[m] - widths[p] * lengths[p]
);

%constraint forall(p in PART)(
%  wasted_space[p] <= module_lengths[m]* module_widths[m]
%);

constraint wasted_space_sum = sum(wasted_space);

solve minimize wasted_space_sum;
include "globals.mzn"; 

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


array[PART] of var MODULE: allocation;

constraint forall(i in PART) (
    (module_lengths[allocation[i]] >= lengths[i] /\ module_widths[allocation[i]] >= widths[i])
    \/ (module_lengths[allocation[i]] >= widths[i] /\ module_widths[allocation[i]] >= lengths[i])
);

constraint bin_packing_capa(module_capacity, allocation, weights);

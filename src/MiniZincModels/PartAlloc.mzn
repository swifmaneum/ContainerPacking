include "globals.mzn"; 

int: n_parts;
set of int: PART = 1..n_parts;

array[PART] of int: lengths;
array[PART] of int: widths;
array[PART] of int: weights;

int: n_slots;
set of int: SLOT = 1..n_slots;

array[SLOT] of int: slot_lengths;
array[SLOT] of int: slot_widths;
array[SLOT] of int: slot_capacity;


array[PART] of var SLOT: allocation;

constraint forall(i in PART) (slot_lengths[allocation[i]] >= lengths[i] /\ slot_widths[allocation[i]] >= widths[i]);

constraint bin_packing_capa(slot_capacity, allocation, weights);

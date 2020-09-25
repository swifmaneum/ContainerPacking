% ----------------------------------------
% Input data
% ----------------------------------------
array[PART] of int: groups;

% ----------------------------------------
% Constraints
% ----------------------------------------
int: utopian_grouped_parts = sum ([ i | i in 1..n_parts-1]);

var 0..utopian_grouped_parts: grouped_parts;
constraint grouped_parts = sum (i,j in PART where i != j /\ i < j /\ groups[i] = groups[j])(allocation[i] = allocation[j]);



solve minimize pow(wasted_space_sum, 2) + pow(grouped_parts - utopian_grouped_parts, 2);
% ----------------------------------------
% Input data
% ----------------------------------------
array[PART] of int: groups;

% ----------------------------------------
% Constraints
% ----------------------------------------
var int: grouped_parts;
constraint grouped_parts = sum (i,j in PART where i != j /\ i < j /\ groups[i] = groups[j])(allocation[i] = allocation[j]);
solve maximize grouped_parts;
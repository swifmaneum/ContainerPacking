% ----------------------------------------
% Input data
% ----------------------------------------
array[PART] of int: groups;

% ----------------------------------------
% Constraints
% ----------------------------------------
solve maximize sum (i,j in PART where i < j)(allocation[i] = allocation[j] /\ groups[i] = groups[j]);
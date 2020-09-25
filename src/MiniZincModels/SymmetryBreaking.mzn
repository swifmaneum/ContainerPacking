% Channeling
% Assignment variables x_ij
array[1..n_modules,1..n_parts] of var bool: x_ij;

% Channeling constraint
constraint forall (i in 1..n_modules, j in 1..n_parts) ( x_ij[i,j] <-> (allocation[j]=i) );

constraint
    lex_greatereq(array1d(x_ij), [ x_ij[i,j] | i in 1..n_modules, j in 1..n_parts ])
    /\lex_greatereq(array1d(x_ij), [ x_ij[i,j] | i in reverse(1..n_modules), j in 1..n_parts ])
    /\lex_greatereq(array1d(x_ij), [ x_ij[i,j] | i in 1..n_modules, j in reverse(1..n_parts) ]);
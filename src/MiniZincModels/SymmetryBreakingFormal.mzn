constraint
    lex_greatereq(array1d(allocation), [ allocation[i,j] | i in 1..n_modules, j in 1..n_parts ])
    /\lex_greatereq(array1d(allocation), [ allocation[i,j] | i in reverse(1..n_modules), j in 1..n_parts ])
    /\lex_greatereq(array1d(allocation), [ allocation[i,j] | i in 1..n_modules, j in reverse(1..n_parts) ]);
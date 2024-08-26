num_ps = {
    # membrane names (labels)
    H = {h1,h2,h3};

    structure = [h3 [h2 [h1]h1 ]h2 ]h3;

    # membrane 1
    h1 = {
        var = {a,f,b,c,d,e}; # variables used in the production function
        E = {e1,e2};
        pr = { f + b min c[e1 -> ] 1|a};
        pr ={  f + d^(1/2) [e1 -> ] 1|d};
        pr ={  f + e1 [e1 -> ] 1|e2};
        var0 = (0,0,0,0,0,0);
        E0  = (1,1);
    };
    h2 = {
        var = {x}; # variables used in the production function
        E = {e2,e3};
        pr = { f + 2[e2 -> ] 1|x};
        pr ={  f + e2 [e2 -> ] 1|e3};
        var0 = (0);
        E0  = (0,0);
    };
    h3 = {
        var = {y}; # variables used in the production function
        E = {e3};
        pr = { f + 3[e3 -> ] 1|y};
        var0 = (0);
        E0  = (0);
    };

}


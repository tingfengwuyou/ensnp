num_ps = {
    # membrane names (labels)
    H = {h1, h2, h3, h4, h5, h6, h7, h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18};

    structure = [h1 [h2 [h5 [h7] h7 ]h5 [h6 [h8] h8] h6 ]h2
                [h3 [h9 [h12] h12 ]h9 [h10 [h13]h13 ]h10 [h11 [h14] h14]h11 ]h3
                [h4 [h15 [h17] h17 ]h15 [h16 [h18]h18 ]h16]h4 ]h1;

    # membrane 1
    h1 = {
        var = {a,f}; # variables used in the production function
        E = {e1};
        pr = {f + 1/3*(b2^(1/2)+b3^(1/3)+b1^(1/4)) [e1 -> ] 1|a};
        var0 = (0,0);
        E0  = (0);
    };
    h2 = {
        var = {b1,c1,c2}; # variables used in the production function
        E = {e4};
        pr = {f+ (c1^(1/2)) min (c2^(1/3))[e4 -> ] 1|b1};
        var0 = (0,0,0);
        E0  = (0);
    };
    h3 = {
        var = {b2,c3,c4,c5}; # variables used in the production function
        E = {e4};
        pr = {f+ (c3^(1/2)) min (c4^(1/3)) min (c5^(1/3))[e4 -> ] 1|b2};
        var0 = (0,0,0,0);
        E0  = (0);
    };
    h4 = {
        var = {b3,c6,c7}; # variables used in the production function
        E = {e4,e1};
        pr = {f+ (c7^(1/2)) min (c6^(1/3))[e4 -> ] 1|b3};
        pr = {f+ e4[e4 -> ] 1|e1};
        var0 = (0,0,0);
        E0  = (0,0);
    };
    h5 = {
        var = {d1,d2,d3}; # variables used in the production function
        E = {e3};
        pr = {f+1/3*(x1+x2+x3) [e3 -> ] 1|c1};
        var0 = (0,0,0);
        E0  = (0);
    };
    h6 = {
        var = {d4,d5,d6}; # variables used in the production function
        E = {e3};
        pr = {f+ x4 min x5 min x6 [e3 -> ] 1|c2};
        var0 = (0,0,0);
        E0  = (0);
    };
    h7 = {
        var = {x1,x2,x3}; # variables used in the production function
        E = {e2};
        pr = {f + d1^(1/2) [e2 -> ] 1|x1};
        pr = {f + d2^(1/3) [e2 -> ] 1|x2};
        pr = {f + d3^(1/4) [e2 -> ] 1|x3};
        var0 = (0,0,0);
        E0  = (1);
    };
    h8 = {
        var = {x4,x5,x6}; # variables used in the production function
        E = {e2};
        pr = {f + d4^(1/2) [e2 -> ] 1|x4};
        pr = {f + d5^(1/3) [e2 -> ] 1|x5};
        pr = {f + d6^(1/4) [e2 -> ] 1|x6};
        var0 = (0,0,0);
        E0  = (1);
    };

    h9 = {
        var = {d7,d8,d9}; # variables used in the production function
        E = {e3};
        pr = {f+ x7 min x8 min x9[e3 -> ] 1|c3};
        var0 = (0,0,0);
        E0  = (0);
    };
    h10 = {
        var = {d10,d11,d12}; # variables used in the production function
        E = {e3};
        pr = {f+ 1/3*(x10+x11+x12) [e3 -> ] 1|c4};
        var0 = (0,0,0);
        E0  = (0);
    };
    h11 = {
        var = {d13,d14,d15}; # variables used in the production function
        E = {e3};
        pr = {f+ 1/3*(x13+x14+x15) [e3 -> ] 1|c5};
        var0 = (0,0,0);
        E0  = (0);
    };
    h12 = {
        var = {x7,x8,x9}; # variables used in the production function
        E = {e2};
        pr = {f + d7^(1/3) [e2 -> ] 1|x7};
        pr = {f + d8^(1/4) [e2 -> ] 1|x8};
        pr = {f + d9^(1/2) [e2 -> ] 1|x9};
        var0 = (0,0,0);
        E0  = (1);
    };
    h13 = {
        var = {x10,x11,x12}; # variables used in the production function
        E = {e2};
        pr = {f + d10^(1/2) [e2 -> ] 1|x10};
        pr = {f + d11^(1/3) [e2 -> ] 1|x11};
        pr = {f + d12^(1/4) [e2 -> ] 1|x12};
        var0 = (0,0,0);
        E0  = (1);
    };
    h14 = {
        var = {x13,x14,x15}; # variables used in the production function
        E = {e2};
        pr = {f + d15^(1/2) [e2 -> ] 1|x15};
        pr = {f + d13^(1/3) [e2 -> ] 1|x13};
        pr = {f + d14^(1/4) [e2 -> ] 1|x14};
        var0 = (0,0,0);
        E0  = (1);
    };
    h15 = {
        var = {d16,d17,d18}; # variables used in the production function
        E = {e3};
        pr = {f+ x16 min x17 min x18 [e3 -> ] 1|c6};
        var0 = (0,0,0);
        E0  = (0);
    };
    h16 = {
        var = {d19,d20,d21,d22}; # variables used in the production function
        E = {e3,e4};
        pr = {f+ 1/4 * (x19+x20+x21+x22) [e3 -> ] 1|c7};
        pr = {f+ e3 [e3 -> ] 1|e4};
        var0 = (0,0,0,0);
        E0  = (0,0);
    };
    h17 = {
        var = {x16,x17,x18}; # variables used in the production function
        E = {e2};
        pr = {f + d16^(1/2) [e2 -> ] 1|x16};
        pr = {f + d18^(1/3) [e2 -> ] 1|x18};
        pr = {f + d17^(1/4) [e2 -> ] 1|x17};
        var0 = (0,0,0);
        E0  = (1);
    };
    h18 = {
        var = {x19,x20,x21,x22}; # variables used in the production function
        E = {e2,e3};
        pr = {f + d21^(1/2) [e2 -> ] 1|x21};
        pr = {f + d19^(1/3) [e2 -> ] 1|x19};
        pr = {f + d22^(1/4) [e2 -> ] 1|x22};
        pr = {f + d20^(1/5) [e2 -> ] 1|x20};
        pr = {f + e2 [e2 -> ] 1|e3};
        var0 = (0,0,0,0);
        E0  = (1,0);
    };

}


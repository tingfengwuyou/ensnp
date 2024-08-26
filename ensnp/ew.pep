num_ps = {
    # membrane names (labels)
    H = {WallFollow, Sigma1, Sigma2, In0, In1, In2, In3, In4};

    structure = [WallFollow [Sigma1 ]Sigma1 [Sigma2 ]Sigma2 [In0 ]In0 [In1 ]In1 [In2 ]In2  [In3 ]In3 [In4 ]In4]WallFollow;

    # membrane 1
    WallFollow = {};
    Sigma1 = {
        var = {f0,CruiseSpeed,XC,XH,Spl}; # variables used in the production function
        E = {e1};
        pr = {e1+f0+CruiseSpeed+XC+0.5*XH-1 [e1 -> ] 1|Spl};
        var0 = (0,0,0,0,0);
        E0  = (0);
    };
    Sigma2 = {
        var = {f0,CruiseSpeed,XC,XH,Spr}; # variables used in the production function
        E = {e1};
        pr = {e1+f0+CruiseSpeed-XC-0.5*XH-1 [e1 -> ] 1|Spr};
        var0 = (0,0,0,0,0);
        E0  = (0);
    };

   In0 = {
        var = {xf}; # variables used in the production function
        E = {e};
        pr = {xf [e -> ] 1|e1};
        var0 = (1);
        E0  = (2);
    };

    In1 = {
    var = {f0,k_Dist,ref_Dist,s_Dist}; # variables used in the production function
        E = {e};
        pr = {f0+k_Dist*(ref_Dist-s_Dist) [e -> ] 1|XC};
        var0 = (0,0,0,0);
        E0  = (2);
    };

    In2 = {
        var = {gamma,f0,s_Avoid}; # variables used in the production function
        E = {e};
      pr = {gamma*(f0+s_Avoid) [e -> ] 1|XH};
        var0 = (0,f0,0);
        E0  = (2);
    };

    In3 = {
        var = {alpha,f0,s_Bw}; # variables used in the production function
        E = {e};
      pr = {0-alpha*(f0+s_Bw) [e -> ] 1|XH};
        var0 = (0,0,0);
        E0  = (2);
    };

    In4 = {
        var = {f0,s_Fw}; # variables used in the production function
        E = {e};
      pr = {f0+s_Fw [e -> ] 1|XH};
        var0 = (0,0);
        E0  = (2);
    };
}


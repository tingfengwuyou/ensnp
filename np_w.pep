num_ps = {
    # membrane names (labels)
    H = {WallFollow, DistanceControl, HeadingControl, SpeedLeft, CruiseSpeedLeft, SpeedRight, CruiseSpeedRight};

    structure = [WallFollow [DistanceControl ]DistanceControl [HeadingControl ]HeadingControl [SpeedLeft [CruiseSpeedLeft ]CruiseSpeedLeft ]SpeedLeft [SpeedRight [CruiseSpeedRight ]CruiseSpeedRight ]SpeedRight
     ]WallFollow;

WallFollow = {
   var = {Err,lw,rw}; # variables used in the production function
   pr = { 2*Err -> 1|Left + 1|Right};
   var0 = (0);
};

DistanceControl = {
   var = {k_Dist,ref_Dist,s_Dist};
   pr = { k_Dist*(ref_Dist-s_Dist) -> 1|Err};
   var0 = (0,0,0);
};

HeadingControl = {
   var = {k_Heading,s_Avoid,s_Fw,s_Bw,gamma,alpha}; # variables used in the production function
   pr = { 0 - k_Heading*(gamma*s_Avoid+s_Fw-alpha*s_Bw) -> 1|Err};
   var0 = (0,0,0,0,0,0); # initial values for variables x_1_1, x_2_1, x_3_1
};

SpeedLeft = {
       var = {Left}; # variables used in the production function
       pr = {Left -> 1|lw};
       var0 = (0);
};

CruiseSpeedLeft = {
       var = {cruiseSpeedLeft}; # variables used in the production function
       pr = {cruiseSpeedLeft -> 1|lw};
       var0 = (0);
};

SpeedRight = {
      var = {Right}; # variables used in the production function
       pr = {0 - Right -> 1|rw};
       var0 = (0);
};

CruiseSpeedRight = {
       var = {cruiseSpeedRight}; # variables used in the production function
       pr = {cruiseSpeedRight -> 1|rw};
       var0 = (0);
};
}

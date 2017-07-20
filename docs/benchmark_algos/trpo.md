# TRPO Benchmark

## Algorithm Description and Code Reference

## Task Groupings and Experimental Setup

## Results
<TABLE>
    <CAPTION>
        <STRONG>Table:</STRONG>
        <SMALL CLASS="SMALL">Average and standard deviation (mean +/- std) of reward across a set of 20 sample rollouts. We show samples immediately after training on a particular environment and the reward obtained by the final trained policy on all previously seen environment. A group of tasks is defined by a bold separator and the total average across all final rollouts is presented. ``Fully Trained'' lists the final evaluation result using the fully trained policy which has seen all the environments. ``After Env Training'' lists the evaluation immediately after training on that specific environment (having seen all the previous environments up until that point in the group). The ``First Step'' column indicates the reward at the first iteration of training on the new environment after having trained on the previous environments in the group. ``Single Env'' indicates rollouts on a policy trained solely on that environment (with all the same training parameters).</SMALL>
    </CAPTION>
    <!-- <TR><TD><TABLE CELLPADDING=3 BORDER="1"> -->
    <TR>
        <TH ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
<SPAN  CLASS="textbf">Environment</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Fully Trained</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">After Env Training</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">First Step</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Single Env</SPAN> </SMALL>
        </TH>
        <!-- <TH ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Grouping Description</SPAN></SMALL></TH> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperGravityHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1495.93 +/- 823.51 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2352.19 +/- 580.53 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 13.48 +/- 8.71</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1843.89 +/- 485.25 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=5 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1192#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperGravityThreeQuarters-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 413.77 +/- 252.67 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2245.13 +/- 872.16  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 697.96 +/- 210.79</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2328.09 +/- 834.35</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Hopper-v1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 668.52 +/- 159.90 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  2622.31 +/- 1032.45 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 781.88 +/- 262.35 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3232.87 +/- 582.55</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperGravityOneAndQuarter-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 922.76 +/- 128.71 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3006.17 +/- 847.30 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 818.08 +/- 255.85 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3028.04 +/- 875.81 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperGravityOneAndHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2690.57 +/- 1110.39 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2792.72 +/- 1075.30 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 658.15 +/- 117.14 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2169.07 +/- 825.75 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 990.95 +/- 1022.32 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2603.704 +/- 881.54  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">593.91 +/- 184.43</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">2520.39 +/- 720.74</SMALL>
        </TD>
        <TD></TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dGravityHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1366.07 +/- 1126.59   </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3485.19 +/- 1054.06</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 5.35 +/- 10.30 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2231.86 +/- 902.31</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=5 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1224#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dGravityThreeQuarters-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3686.37 +/- 287.96  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3962.69 +/- 1061.71</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">1071.95 +/- 267.35 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2431.87 +/- 935.14 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2d-v1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 4030.00 +/- 85.76  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3732.04 +/- 1314.89 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 930.92 +/- 264.88</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2570.15 +/- 915.58</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dGravityOneAndQuarter-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 4115.23 +/- 90.33  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 4090.30 +/- 1058.62 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 926.06 +/- 303.76</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3505.52 +/- 1626.58</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dGravityOneAndHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 4201.08 +/- 684.37  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3988.62 +/- 971.43 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 925.93 +/- 290.33 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2435.21 +/- 1391.00</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3479.76 +/- 1230.72  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3851.768 +/- 1092.1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">772.04 +/- 227.32</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2634.92 +/- 1154.12 </SMALL>
        </TD>
        <!-- <TD></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahGravityHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1495.93 +/- 823.51 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1107.50 +/- 784.31 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -369.31 +/- 113.71 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2048.93 +/- 761.03</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=5 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1256#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahGravityThreeQuarters-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1671.76 +/- 594.15 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2142.78 +/- 818.99 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1410.25 +/- 529.41</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">3268.26 +/- 703.43</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetah-v1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1743.97 +/- 100.32 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  2410.50 +/- 137.30 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">1867.99 +/- 251.58 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2554.01 +/- 115.69 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahGravityOneAndQuarter-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2649.13 +/- 143.43 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2939.14 +/- 164.62 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1966.66+/- 171.88 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2572.64 +/- 90.80</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahGravityOneAndHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3421.21 +/- 165.60 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3402.83 +/- 204.00 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2143.76 +/- 236.60</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2276.82 +/- 93.30</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2196.41 +/- 867.75  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2400.55 +/- 421.84 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">1403.87 +/- 260.63</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">2544.13 +/- 352.85</SMALL>
        </TD>
        <!-- <TD></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidGravityHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 416.41 +/- 76.41 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 421.12 +/- 95.61 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 89.60 +/- 10.92 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 849.29 +/- 213.81 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=5 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1288#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidGravityThreeQuarters-v0  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 356.74 +/- 52.52 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 385.54 +/- 72.98 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 293.14 +/- 66.12 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 637.33 +/- 170.51 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Humanoid-v1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 310.09 +/- 55.31 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 326.59 +/- 59.78 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 267.11 +/- 52.74</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 483.35 +/- 106.12 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidGravityOneAndQuarter-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 261.01 +/- 31.75 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 269.03 +/- 40.59 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 233.82 +/- 39.41 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 576.98 +/- 124.25 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidGravityOneAndHalf-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 227.17 +/- 33.62 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 226.94 +/- 29.09 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 208.74 +/- 34.43 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 538.24 +/- 113.17 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 314.28 +/- 85.41 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">325.84 +/- 59.61 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">218.48 +/- 40.72 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 617.03 +/- 145.57 </SMALL>
        </TD>
        <!-- <TD></TD> -->
    </TR>
    <!-- </TABLE><SMALL CLASS="SCRIPTSIZE"> -->

    <!-- <A NAME="table:results_gravity"></A></SMALL></TD></TR> -->
</TABLE>


<TABLE>
    <CAPTION>
        <STRONG>Table:</STRONG> Results for modified body-part running task groups. Same parameters as described in Table&nbsp;
        <A HREF="#table:results_gravity">
            <IMG ALIGN="BOTTOM" BORDER="1" SRC="crossref.png">
        </A>. Number of training iterations lowered to 500 per environment due to the larger number of environments.</CAPTION>
    <!-- <TR><TD> -->
    <!-- <TABLE CELLPADDING=3 BORDER="1"> -->
    <TR>
        <TH ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
<SPAN  CLASS="textbf">Environment <A NAME="tex2html7"
  HREF="#foot111"><SUP><SPAN CLASS="arabic">3</SPAN></SUP></A></SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Fully Trained</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">After Env Training</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">First Step</SPAN> </SMALL>
        </TH>
        <!-- <TH ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Grouping Description</SPAN></SMALL></TH> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperSmallFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  591.91 +/- 150.73 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1330.65 +/- 402.07 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 9.83 +/- 4.52 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=8 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1463#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperSmallLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2074.58 +/- 800.61 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1359.85 +/- 311.91 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 744.35  +/-120.50  </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperSmallThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 919.87 +/- 343.57  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1492.44 +/- 486.72 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1719.34 +/-757.42 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperSmallTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1094.85 +/- 319.94 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1492.97 +/- 518.47 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1636.30 +/-298.22  </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperBigFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2823.58 +/- 887.25 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1819.91 +/- 812.33 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 559.61 +/-145.24  </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperBigLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1020.13 +/- 454.74 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  2148.57 +/- 795.95</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 689.58 +/-96.23 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperBigThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2799.39 +/- 748.89 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1827.48 +/- 767.09 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 674.14 +/- 101.72 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperBigTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1971.50 +/- 794.24 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  2090.68 +/- 693.34 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1110.46 +/- 213.74 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1661.98 +/- 1025.19 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1695.31 +/- 598.48 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 892.95 +/- 203.69 </SMALL>
        </TD>
        <!-- <TD></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dSmallFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2497.10 +/- 1309.80  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 531.08 +/- 329.00 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -2.87 +/- 2.56 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=8 WIDTH=1><SMALL CLASS="SCRIPTSIZE"><SPAN><</SPAN>#1501#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dSmallLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3181.14 +/- 1131.29  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1120.19 +/- 597.09 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 318.20 +/- 229.00 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dSmallThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3106.65 +/- 641.34  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1735.39 +/- 880.44 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1317.72 +/- 737.66 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dSmallTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3132.88 +/- 991.48  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1838.79 +/- 965.60 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 979.32 +/- 582.14 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dBigFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2751.34 +/- 1216.07 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1873.60 +/- 1047.41 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 789.32 +/- 289.65 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dBigLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2820.94 +/- 1108.26 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2133.64 +/- 1246.53 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1743.53 +/- 1106.90 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dBigThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 892.54 +/- 212.46 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2756.79 +/- 1238.62 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 805.31 +/-147.40 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dBigTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3097.45 +/- 1383.43 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2701.94 +/- 1473.47 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3045.06 +/- 967.83 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2685.01 +/- 1280.70  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1836.42 +/- 972.27 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1124.45 +/- 507.89 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> </SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahSmallFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2003.46 +/- 933.59 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 898.51 +/- 363.85 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -502.264 +/- 97.99  </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=8 WIDTH=1><SMALL CLASS="SCRIPTSIZE"><SPAN><</SPAN>#1539#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahSmallLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2327.16 +/- 702.69 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1494.03 +/- 310.11 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 904.82 +/- 330.37 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahSmallThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2555.16 +/- 96.80  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  1672.22 +/- 110.11 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1311.60 +/- 281.24 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahSmallTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2294.72 +/- 109.20 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1845.20 +/- 86.03 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1515.53 +/- 94.68 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahBigFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2211.92 +/- 65.81 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1997.73 +/- 101.36 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1789.90 +/- 82.31 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahBigLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2269.78 +/- 95.57 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2101.74 +/- 95.98 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1908.53 +/- 99.49 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahBigThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2424.95 +/- 94.19 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">   2345.88 +/- 381.33 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1925.04 +/- 347.83 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahBigTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2686.13 +/- 97.96 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2620.46 +/- 297.88 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2456.04 +/- 421.03 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2346.66 +/- 464.81 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1871.97 +/- 218.33</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1413.64 +/- 207.11 </SMALL>
        </TD>
        <TD></TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 391.70 +/- 124.75 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 228.46 +/- 62.80 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 94.85  +/- 106.57 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=13 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1577#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 438.90 +/- 113.80 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 290.88 +/- 82.86  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 253.81 +/- 68.12 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 378.47 +/- 113.70 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 347.38 +/- 99.89  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 322.97 +/- 93.28 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 433.04 +/- 88.76 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 341.22 +/- 89.69 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 313.71 +/- 82.52 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigFoot-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 456.39 +/- 85.60 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 399.96 +/- 95.84  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 355.16 +/- 92.07 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigLeg-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 430.82 +/- 105.41  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 380.20 +/- 97.58  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 347.26 +/- 87.78 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigThigh-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 365.79 +/- 72.06 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 331.80 +/- 84.06  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 303.13 +/- 77.17 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigTorso-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 397.91 +/- 109.04 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 392.66 +/- 108.20 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 374.94 +/- 102.12 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallHead-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 422.33 +/- 112.20  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 395.75 +/- 101.70  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 386.14 +/- 96.37 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigHead-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 507.29 +/- 146.50  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 409.66 +/- 109.13  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 411.98 +/- 119.99 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallArm-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 429.93 +/- 113.26  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 416.41 +/- 94.45   </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 400.16 +/- 91.75 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigArm-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 466.13 +/- 129.87   </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 411.23 +/- 111.20  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 392.53 +/- 115.21 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidSmallHand-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 450.07 +/- 76.72  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 423.29 +/- 101.61 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 417.45 +/- 99.08 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidBigHand-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 409.46 +/- 69.38  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 420.65 +/- 100.29 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 415.04 +/- 108.38 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE">  </SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 427.02 +/- 112.56 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  370.68 +/- 95.66 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 342.08 +/- 95.23 </SMALL>
        </TD>
        <!-- <TD></TD> -->
        <!-- </TR> -->
        <!-- </TABLE><SMALL CLASS="SCRIPTSIZE"> -->

        <!-- <A NAME="table:results_body_parts"></A></SMALL></TD></TR> -->
</TABLE>


<TABLE>
    <CAPTION>
        <STRONG>Table:</STRONG> Results for modified running tasks with sensors, walls, or multiple goals.</CAPTION>
    <!-- <TR><TD><TABLE CELLPADDING=3 BORDER="1"> -->
    <TR>
        <TH ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
<SPAN  CLASS="textbf">Environment <A NAME="tex2html9"
  HREF="#foot150"><SUP><SPAN CLASS="arabic">4</SPAN></SUP></A></SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Fully Trained</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">After Env Training</SPAN></SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">First Step</SPAN> </SMALL>
        </TH>
        <!-- <TH ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Grouping Description</SPAN></SMALL></TH> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

HopperWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 747.67 +/- 27.06 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2881.79 +/- 623.11 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 15.51 +/- 14.88 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=2 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1700#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HopperWall-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 687.58  +/- 58.81 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 695.00 +/- 93.70 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 695.94 +/- 102.96 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Walker2dWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1897.74 +/- 1101.13 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 3357.76 +/- 1142.85 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -2.27 +/- 8.84 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=2 WIDTH=1><SMALL CLASS="SCRIPTSIZE"><SPAN><</SPAN>#1709#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Walker2dWall-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 1271.78 +/- 881.57 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 974.83 +/- 664.29 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 635.45 +/- 303.73 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

HalfCheetahWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2924.83 +/- 165.69 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2754.58 +/- 151.81 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -296.32 +/- 110.45 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=2 WIDTH=1><SMALL CLASS="SCRIPTSIZE"><SPAN><</SPAN>#1718#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HalfCheetahWall-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2022.90 +/- 826.91 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2159.17 +/- 805.27 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 2043.85 +/- 807.09 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

HumanoidWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 339.37 +/- 47.38 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 285.70 +/- 51.99 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 67.37 +/- 8.31 </SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=2 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1727#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidWall-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 334.03 +/- 51.49 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 328.90 +/- 57.41 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 284.55 +/- 49.07 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Humanoid-v1 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  252.38  +/- 12.05 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 269.23 +/- 75.11 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 72.398 +/- 2.56</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=3 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1736#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidStandup-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 75861.96 +/- 19951.32 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 75906.45 +/- 22390.07 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 70659.6 +/- 19479.4</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidStandupAndRun-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 71269.19 +/- 16689.99 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 73919.85 +/- 19215.23 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 70021.9+/-18660.3</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

HumanoidWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 112.74 +/- 23.09 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 114.75 +/- 13.48 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 64.6059 +/- 1.76</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=4 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1749#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidStandupWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 53124.35 +/- 15136.53 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 58335.81 +/- 16259.60 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 52029.5 +/- 13585.10  </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidStandupAndRunWithSensor-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 59263.15 +/- 12285.51 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 62570.26 +/- 14258.35 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 55929.7 +/- 15432.20 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
HumanoidStandupAndRunWall-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  61468.03 +/- 16135.02 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 66789.60 +/- 14405.80 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> 61764.5 +/- 15150.20 </SMALL>
        </TD>
    </TR>
    </TR>
    <!-- </TABLE><SMALL CLASS="SCRIPTSIZE"> -->

    <!-- <A NAME="table:results_sensor"></A></SMALL></TD></TR> -->
</TABLE>


<TABLE>
    <CAPTION>
        <STRONG>Table:</STRONG> Results for arm-based task groups. Same parameters as described in Table&nbsp;
        <A HREF="#table:results_gravity">
            <IMG ALIGN="BOTTOM" BORDER="1" SRC="crossref.png">
        </A>.</CAPTION>
    <!-- <TR><TD><TABLE CELLPADDING=3 BORDER="1"> -->
    <TR>
        <TH ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
<SPAN  CLASS="textbf">Environment <A NAME="tex2html11"
  HREF="#foot186"><SUP><SPAN CLASS="arabic">5</SPAN></SUP></A></SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Fully Trained</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">After Env Training</SPAN> </SMALL>
        </TH>
        <TH ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">First Step</SPAN> </SMALL>
        </TH>
        <!-- <TH ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> <SPAN  CLASS="textbf">Grouping Description</SPAN></SMALL></TH> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Striker-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  -124.87 +/- 47.33 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -114.61 +/- 36.93 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -590.61 +/- 78.77</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER" VALIGN="MIDDLE" ROWSPAN=2 WIDTH=1><SMALL CLASS="SCRIPTSIZE"> <SPAN><</SPAN>#1799#></SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
StrikerMovingStart-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  -163.08 +/- 76.29 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -146.06 +/- 60.21</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -171.06 +/- 92.10 </SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">

Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  -143.97 +/- 66.29 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -130.33 +/- 43.57</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -380.83 +/- 85.44</SMALL>
        </TD>
        <!-- <TD ALIGN="CENTER"><SMALL CLASS="SCRIPTSIZE"> </SMALL></TD> -->
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
Pusher-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">  -24.83 +/- 2.39  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -24.59 +/- 4.01</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">-209.57 +/- 7.46</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">
PusherMovingGoal-v0 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -28.01 +/- 7.24 </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -27.76 +/- 6.20</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -34.90 +/- 9.38</SMALL>
        </TD>
    </TR>
    <TR>
        <TD ALIGN="LEFT">
            <SMALL CLASS="SCRIPTSIZE">Total for Grouping </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE"> -26.42 +/- 5.62  </SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">-26.17 +/- 5.11</SMALL>
        </TD>
        <TD ALIGN="CENTER">
            <SMALL CLASS="SCRIPTSIZE">-122.24 +/- 8.42</SMALL>
        </TD>

    </TR>

</TABLE>

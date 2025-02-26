# Size of variable arrays:
sizeAlgebraic = 42
sizeStates = 27
sizeConstants = 89
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "v_T in component pp_T_fixed_I_type (m3_per_s)"
    legend_algebraic[0] = "v_venous_svc in component terminal_venous_connection (m3_per_s)"
    legend_algebraic[4] = "u in component vp_ven_simple_type (J_per_m3)"
    legend_states[1] = "v in component vp_ven_simple_type (m3_per_s)"
    legend_constants[0] = "R_pvn in component parameters (Js_per_m6)"
    legend_constants[1] = "C_pvn in component parameters (m6_per_J)"
    legend_constants[2] = "u_ext_pvn in component parameters (J_per_m3)"
    legend_constants[3] = "I_pvn in component parameters (Js2_per_m6)"
    legend_constants[4] = "q_C_init_pvn in component parameters (m3)"
    legend_states[2] = "q_C_change in component vp_ven_simple_type (m3)"
    legend_algebraic[1] = "q_C in component vp_ven_simple_type (m3)"
    legend_algebraic[3] = "q in component vp_ven_simple_type (m3)"
    legend_constants[5] = "q_us_0_pvn in component parameters (m3)"
    legend_constants[73] = "q_us_wCont in component vp_ven_simple_type (m3)"
    legend_constants[6] = "Delta_q_us_pvn in component parameters (m3)"
    legend_algebraic[6] = "u in component vp_simple_type (J_per_m3)"
    legend_states[3] = "v in component vp_simple_type (m3_per_s)"
    legend_states[4] = "q_C in component vp_simple_type (m3)"
    legend_constants[7] = "R_par in component parameters (Js_per_m6)"
    legend_constants[8] = "C_par in component parameters (m6_per_J)"
    legend_constants[9] = "u_ext_par in component parameters (J_per_m3)"
    legend_constants[10] = "I_par in component parameters (Js2_per_m6)"
    legend_constants[11] = "rho in component parameters_global (Js2_per_m5)"
    legend_constants[12] = "T in component parameters_global (second)"
    legend_algebraic[9] = "mt in component heart_Ca_input (second)"
    legend_algebraic[28] = "u_ra in component heart_Ca_input (J_per_m3)"
    legend_algebraic[29] = "u_rv in component heart_Ca_input (J_per_m3)"
    legend_algebraic[30] = "u_la in component heart_Ca_input (J_per_m3)"
    legend_algebraic[31] = "u_lv in component heart_Ca_input (J_per_m3)"
    legend_states[5] = "q_ra in component heart_Ca_input (m3)"
    legend_states[6] = "q_rv in component heart_Ca_input (m3)"
    legend_states[7] = "q_la in component heart_Ca_input (m3)"
    legend_states[8] = "q_lv in component heart_Ca_input (m3)"
    legend_constants[13] = "q_ra_us in component parameters_global (m3)"
    legend_constants[14] = "q_rv_us in component parameters_global (m3)"
    legend_constants[15] = "q_la_us in component parameters_global (m3)"
    legend_constants[16] = "q_lv_us in component parameters_global (m3)"
    legend_constants[17] = "q_ra_init in component parameters_global (m3)"
    legend_constants[18] = "q_rv_init in component parameters_global (m3)"
    legend_constants[19] = "q_la_init in component parameters_global (m3)"
    legend_constants[20] = "q_lv_init in component parameters_global (m3)"
    legend_constants[21] = "T_ac in component parameters_global (second)"
    legend_constants[22] = "T_ar in component parameters_global (second)"
    legend_constants[23] = "t_astart in component parameters_global (second)"
    legend_constants[74] = "t_astart_norm in component heart_Ca_input (dimensionless)"
    legend_states[9] = "chi_a in component heart_Ca_input (dimensionless)"
    legend_algebraic[7] = "chi_afloor in component heart_Ca_input (dimensionless)"
    legend_constants[24] = "T_vc in component parameters_global (second)"
    legend_constants[25] = "T_vr in component parameters_global (second)"
    legend_constants[26] = "t_vstart in component parameters_global (second)"
    legend_constants[87] = "t_vstart_norm in component heart_Ca_input (dimensionless)"
    legend_constants[27] = "E_ra_A in component parameters_global (J_per_m6)"
    legend_constants[28] = "E_ra_B in component parameters_global (J_per_m6)"
    legend_constants[29] = "E_rv_A in component parameters_global (J_per_m6)"
    legend_constants[30] = "E_rv_B in component parameters_global (J_per_m6)"
    legend_constants[31] = "E_la_A in component parameters_global (J_per_m6)"
    legend_constants[32] = "E_la_B in component parameters_global (J_per_m6)"
    legend_constants[33] = "E_lv_A in component parameters_global (J_per_m6)"
    legend_constants[34] = "E_lv_B in component parameters_global (J_per_m6)"
    legend_algebraic[10] = "e_a in component heart_Ca_input (dimensionless)"
    legend_algebraic[11] = "e_v in component heart_Ca_input (dimensionless)"
    legend_states[10] = "v_trv in component heart_Ca_input (m3_per_s)"
    legend_states[11] = "v_puv in component heart_Ca_input (m3_per_s)"
    legend_states[12] = "v_miv in component heart_Ca_input (m3_per_s)"
    legend_states[13] = "v_aov in component heart_Ca_input (m3_per_s)"
    legend_constants[35] = "K_vo_trv in component parameters_global (m3_per_Js)"
    legend_constants[36] = "K_vo_puv in component parameters_global (m3_per_Js)"
    legend_constants[37] = "K_vo_miv in component parameters_global (m3_per_Js)"
    legend_constants[38] = "K_vo_aov in component parameters_global (m3_per_Js)"
    legend_constants[39] = "K_vc_trv in component parameters_global (m3_per_Js)"
    legend_constants[40] = "K_vc_puv in component parameters_global (m3_per_Js)"
    legend_constants[41] = "K_vc_miv in component parameters_global (m3_per_Js)"
    legend_constants[42] = "K_vc_aov in component parameters_global (m3_per_Js)"
    legend_constants[43] = "M_rg_trv in component parameters_global (dimensionless)"
    legend_constants[44] = "M_rg_puv in component parameters_global (dimensionless)"
    legend_constants[45] = "M_rg_miv in component parameters_global (dimensionless)"
    legend_constants[46] = "M_rg_aov in component parameters_global (dimensionless)"
    legend_constants[47] = "M_st_trv in component parameters_global (dimensionless)"
    legend_constants[48] = "M_st_puv in component parameters_global (dimensionless)"
    legend_constants[49] = "M_st_miv in component parameters_global (dimensionless)"
    legend_constants[50] = "M_st_aov in component parameters_global (dimensionless)"
    legend_constants[51] = "l_eff in component parameters_global (metre)"
    legend_constants[52] = "A_nn_trv in component parameters_global (m2)"
    legend_constants[53] = "A_nn_puv in component parameters_global (m2)"
    legend_constants[54] = "A_nn_miv in component parameters_global (m2)"
    legend_constants[55] = "A_nn_aov in component parameters_global (m2)"
    legend_algebraic[13] = "A_eff_trv in component heart_Ca_input (m2)"
    legend_algebraic[17] = "A_eff_puv in component heart_Ca_input (m2)"
    legend_algebraic[21] = "A_eff_miv in component heart_Ca_input (m2)"
    legend_algebraic[25] = "A_eff_aov in component heart_Ca_input (m2)"
    legend_algebraic[34] = "u in component vv_simple_type (J_per_m3)"
    legend_states[14] = "v in component vv_simple_type (m3_per_s)"
    legend_states[15] = "q_C in component vv_simple_type (m3)"
    legend_constants[56] = "R_aortic_root in component parameters (Js_per_m6)"
    legend_constants[57] = "C_aortic_root in component parameters (m6_per_J)"
    legend_constants[58] = "u_ext_aortic_root in component parameters (J_per_m3)"
    legend_constants[59] = "I_aortic_root in component parameters (Js2_per_m6)"
    legend_algebraic[37] = "u in component pp_T_fixed_I_type (J_per_m3)"
    legend_states[16] = "v in component pp_T_fixed_I_type (m3_per_s)"
    legend_constants[60] = "R_T_systemic_T in component parameters (Js_per_m6)"
    legend_constants[61] = "C_T_systemic_T in component parameters (m6_per_J)"
    legend_constants[62] = "u_ext_systemic_T in component parameters (J_per_m3)"
    legend_states[17] = "q_T in component pp_T_fixed_I_type (m3)"
    legend_algebraic[41] = "u in component vp_ven_simple_type (J_per_m3)"
    legend_states[18] = "v in component vp_ven_simple_type (m3_per_s)"
    legend_constants[63] = "R_venous_svc in component parameters (Js_per_m6)"
    legend_constants[64] = "C_venous_svc in component parameters (m6_per_J)"
    legend_constants[65] = "u_ext_venous_svc in component parameters (J_per_m3)"
    legend_constants[66] = "I_venous_svc in component parameters (Js2_per_m6)"
    legend_constants[67] = "q_C_init_venous_svc in component parameters (m3)"
    legend_states[19] = "q_C_change in component vp_ven_simple_type (m3)"
    legend_algebraic[38] = "q_C in component vp_ven_simple_type (m3)"
    legend_algebraic[40] = "q in component vp_ven_simple_type (m3)"
    legend_constants[68] = "q_us_0_venous_svc in component parameters (m3)"
    legend_constants[75] = "q_us_wCont in component vp_ven_simple_type (m3)"
    legend_constants[69] = "Delta_q_us_venous_svc in component parameters (m3)"
    legend_constants[76] = "R_v in component vp_ven_simple_type (Js_per_m6)"
    legend_algebraic[2] = "u_C in component vp_ven_simple_type (J_per_m3)"
    legend_constants[77] = "R_v in component vp_simple_type (Js_per_m6)"
    legend_algebraic[5] = "u_C in component vp_simple_type (J_per_m3)"
    legend_states[20] = "s in component heart_Ca_input (second)"
    legend_constants[78] = "T_ac_norm in component heart_Ca_input (dimensionless)"
    legend_constants[79] = "T_ar_norm in component heart_Ca_input (dimensionless)"
    legend_constants[80] = "T_vc_norm in component heart_Ca_input (dimensionless)"
    legend_constants[81] = "T_vr_norm in component heart_Ca_input (dimensionless)"
    legend_constants[82] = "v_zero in component zero_flow (m3_per_s)"
    legend_algebraic[15] = "L_trv in component heart_Ca_input (dimensionless)"
    legend_algebraic[19] = "L_puv in component heart_Ca_input (dimensionless)"
    legend_algebraic[23] = "L_miv in component heart_Ca_input (dimensionless)"
    legend_algebraic[27] = "L_aov in component heart_Ca_input (dimensionless)"
    legend_algebraic[14] = "B_trv in component heart_Ca_input (dimensionless)"
    legend_algebraic[18] = "B_puv in component heart_Ca_input (dimensionless)"
    legend_algebraic[22] = "B_miv in component heart_Ca_input (dimensionless)"
    legend_algebraic[26] = "B_aov in component heart_Ca_input (dimensionless)"
    legend_algebraic[12] = "zeta_trv in component heart_Ca_input (dimensionless)"
    legend_algebraic[16] = "zeta_puv in component heart_Ca_input (dimensionless)"
    legend_algebraic[20] = "zeta_miv in component heart_Ca_input (dimensionless)"
    legend_algebraic[24] = "zeta_aov in component heart_Ca_input (dimensionless)"
    legend_states[21] = "zeta_trv_pre in component heart_Ca_input (dimensionless)"
    legend_states[22] = "zeta_puv_pre in component heart_Ca_input (dimensionless)"
    legend_states[23] = "zeta_miv_pre in component heart_Ca_input (dimensionless)"
    legend_states[24] = "zeta_aov_pre in component heart_Ca_input (dimensionless)"
    legend_constants[70] = "eps in component heart_Ca_input (dimensionless)"
    legend_constants[71] = "eps_1 in component heart_Ca_input (dimensionless)"
    legend_constants[72] = "eps_2 in component heart_Ca_input (dimensionless)"
    legend_states[25] = "chi_v in component heart_Ca_input (dimensionless)"
    legend_algebraic[8] = "chi_vfloor in component heart_Ca_input (dimensionless)"
    legend_constants[83] = "R_v in component vv_simple_type (Js_per_m6)"
    legend_algebraic[32] = "u_C in component vv_simple_type (J_per_m3)"
    legend_algebraic[35] = "u_d in component vv_simple_type (J_per_m3)"
    legend_algebraic[33] = "u_C_d in component vv_simple_type (J_per_m3)"
    legend_states[26] = "q_C_d in component vv_simple_type (m3)"
    legend_constants[84] = "I_T in component pp_T_fixed_I_type (Js2_per_m6)"
    legend_constants[85] = "R_v in component pp_T_fixed_I_type (Js_per_m6)"
    legend_algebraic[36] = "u_C in component pp_T_fixed_I_type (J_per_m3)"
    legend_constants[86] = "R_v in component vp_ven_simple_type (Js_per_m6)"
    legend_algebraic[39] = "u_C in component vp_ven_simple_type (J_per_m3)"
    legend_rates[1] = "d/dt v in component vp_ven_simple_type (m3_per_s)"
    legend_rates[2] = "d/dt q_C_change in component vp_ven_simple_type (m3)"
    legend_rates[3] = "d/dt v in component vp_simple_type (m3_per_s)"
    legend_rates[4] = "d/dt q_C in component vp_simple_type (m3)"
    legend_rates[9] = "d/dt chi_a in component heart_Ca_input (dimensionless)"
    legend_rates[25] = "d/dt chi_v in component heart_Ca_input (dimensionless)"
    legend_rates[20] = "d/dt s in component heart_Ca_input (second)"
    legend_rates[21] = "d/dt zeta_trv_pre in component heart_Ca_input (dimensionless)"
    legend_rates[22] = "d/dt zeta_puv_pre in component heart_Ca_input (dimensionless)"
    legend_rates[23] = "d/dt zeta_miv_pre in component heart_Ca_input (dimensionless)"
    legend_rates[24] = "d/dt zeta_aov_pre in component heart_Ca_input (dimensionless)"
    legend_rates[10] = "d/dt v_trv in component heart_Ca_input (m3_per_s)"
    legend_rates[11] = "d/dt v_puv in component heart_Ca_input (m3_per_s)"
    legend_rates[12] = "d/dt v_miv in component heart_Ca_input (m3_per_s)"
    legend_rates[13] = "d/dt v_aov in component heart_Ca_input (m3_per_s)"
    legend_rates[5] = "d/dt q_ra in component heart_Ca_input (m3)"
    legend_rates[6] = "d/dt q_rv in component heart_Ca_input (m3)"
    legend_rates[7] = "d/dt q_la in component heart_Ca_input (m3)"
    legend_rates[8] = "d/dt q_lv in component heart_Ca_input (m3)"
    legend_rates[14] = "d/dt v in component vv_simple_type (m3_per_s)"
    legend_rates[15] = "d/dt q_C in component vv_simple_type (m3)"
    legend_rates[26] = "d/dt q_C_d in component vv_simple_type (m3)"
    legend_rates[17] = "d/dt q_T in component pp_T_fixed_I_type (m3)"
    legend_rates[16] = "d/dt v in component pp_T_fixed_I_type (m3_per_s)"
    legend_rates[0] = "d/dt v_T in component pp_T_fixed_I_type (m3_per_s)"
    legend_rates[18] = "d/dt v in component vp_ven_simple_type (m3_per_s)"
    legend_rates[19] = "d/dt q_C_change in component vp_ven_simple_type (m3)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = 0.0
    states[1] = 0.0
    constants[0] = 1.333e+6
    constants[1] = 0.60015e-8
    constants[2] = 0.0
    constants[3] = 1.0e-6
    constants[4] = 1e-4
    constants[5] = 0.0
    constants[6] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    constants[7] = 10.664e+6
    constants[8] = 0.0309077e-8
    constants[9] = 0.0
    constants[10] = 1.0e-6
    constants[11] = 1050
    constants[12] = 1.0395833333
    constants[13] = 4.0e-6
    constants[14] = 10.0e-6
    constants[15] = 4.0e-6
    constants[16] = 5.0e-6
    constants[17] = 4.0e-6
    constants[18] = 10.0e-6
    constants[19] = 4.0e-6
    constants[20] = 2e-3
    constants[21] = 0.0739583333
    constants[22] = 0.0739583333
    constants[23] = 0.8916666667
    states[9] = 0.0
    constants[24] = 0.40
    constants[25] = 0.2079166667
    constants[26] = 0.0
    constants[27] = 7.998e+6
    constants[28] = 9.331e+6
    constants[29] = 73.315e+6
    constants[30] = 6.665e+6
    constants[31] = 9.331e+6
    constants[32] = 11.997e+6
    constants[33] = 366.575e+6
    constants[34] = 10.664e+6
    states[10] = 0
    states[11] = 0
    states[12] = 0
    states[13] = 0
    constants[35] = 0.3
    constants[36] = 0.2
    constants[37] = 0.3
    constants[38] = 0.04
    constants[39] = 0.4
    constants[40] = 0.2
    constants[41] = 0.4
    constants[42] = 0.04
    constants[43] = 0
    constants[44] = 0
    constants[45] = 0
    constants[46] = 0
    constants[47] = 1
    constants[48] = 1
    constants[49] = 1
    constants[50] = 1
    constants[51] = 0.01
    constants[52] = 0.0009
    constants[53] = 0.0004
    constants[54] = 0.0006
    constants[55] = 0.000314
    states[14] = 0.0
    states[15] = 0.0
    constants[56] = 1.0e6
    constants[57] = 1.2028e-08
    constants[58] = 0.0
    constants[59] = 1.0e+4
    states[16] = 0.0
    constants[60] = 1.10e8
    constants[61] = 1e-7
    constants[62] = 0.0
    states[17] = 0.0
    states[18] = 0.0
    constants[63] = 1114600.0
    constants[64] = 1e-6
    constants[65] = 0.0
    constants[66] = 1.0e-3
    constants[67] = 1.3e-3
    constants[68] = 0.0
    constants[69] = 0.0
    states[20] = 0.0
    states[21] = 0
    states[22] = 0
    states[23] = 0
    states[24] = 0
    constants[70] = 1e-14
    constants[71] = 0.07
    constants[72] = 0.02
    states[25] = 0.0
    states[26] = 0.0
    constants[73] = constants[5]+constants[6]
    constants[74] = constants[23]/constants[12]
    constants[75] = constants[68]+constants[69]
    constants[76] = 0.0100000/constants[1]
    constants[77] = 0.0100000/constants[8]
    constants[78] = constants[21]/constants[12]
    constants[79] = constants[24]/constants[12]
    constants[80] = constants[24]/constants[12]
    constants[81] = constants[25]/constants[12]
    constants[82] = 0.00000
    constants[83] = 0.0100000/constants[57]
    constants[84] = 1.00000e-06
    constants[85] = 0.0100000/constants[61]
    constants[86] = 0.0100000/constants[64]
    constants[88] = 1.00000/constants[12]
    constants[87] = constants[26]/constants[12]
    states[2] = constants[4]
    states[5] = constants[17]
    states[6] = constants[18]
    states[7] = constants[19]
    states[8] = constants[20]
    states[19] = constants[67]
    return (states, constants)

def computeRates(voi, states, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[20] = constants[88]
    rates[2] = states[3]-states[1]
    rates[4] = states[11]-states[3]
    rates[5] = (states[18]+constants[82])-states[10]
    rates[6] = states[10]-states[11]
    rates[7] = states[1]-states[12]
    rates[8] = states[12]-states[13]
    rates[15] = states[13]-states[14]
    rates[26] = states[14]-states[16]
    rates[17] = states[16]-states[0]
    algebraic[0] = states[0]
    rates[19] = algebraic[0]-states[18]
    algebraic[1] = (states[2]+constants[5])-constants[73]
    algebraic[2] = algebraic[1]/constants[1]+constants[2]
    algebraic[4] = algebraic[2]+constants[76]*(states[3]-states[1])
    algebraic[5] = states[4]/constants[8]+constants[9]
    algebraic[6] = algebraic[5]+constants[77]*(states[11]-states[3])
    rates[3] = ((algebraic[6]-algebraic[4])-constants[7]*states[3])/constants[10]
    algebraic[9] = states[20]-floor(states[20])
    algebraic[7] = states[9]-floor(states[9])
    rates[9] = custom_piecewise([greater_equal(algebraic[9] , constants[74]) & less_equal(algebraic[9] , constants[74]+constants[71]) & less_equal(algebraic[7] , 0.500000), 0.500000/constants[21] , greater(constants[74]+constants[71] , 1.00000) & less_equal(algebraic[9] , (constants[74]+constants[71])-1.00000) & less_equal(algebraic[7] , 0.500000), 0.500000/constants[21] , greater(algebraic[7] , constants[72]) & less_equal(algebraic[7] , 0.500000), 0.500000/constants[21] , greater_equal(algebraic[7] , 0.500000), 0.500000/constants[22] , True, 0.00000])
    algebraic[8] = states[25]-floor(states[25])
    rates[25] = custom_piecewise([greater_equal(algebraic[9] , constants[87]) & less_equal(algebraic[9] , constants[87]+constants[71]) & less_equal(algebraic[8] , 0.500000), 0.500000/constants[24] , greater(constants[87]+constants[71] , 1.00000) & less_equal(algebraic[9] , (constants[87]+constants[71])-1.00000) & less_equal(algebraic[8] , 0.500000), 0.500000/constants[24] , greater(algebraic[8] , constants[72]) & less_equal(algebraic[8] , 0.500000), 0.500000/constants[24] , greater(algebraic[8] , 0.500000), 0.500000/constants[25] , True, 0.00000])
    algebraic[10] = 0.500000*(1.00000-cos(2.00000* pi*algebraic[7]))
    algebraic[30] = (algebraic[10]*constants[31]+constants[32])*(states[7]-constants[15])
    rates[1] = ((algebraic[4]-algebraic[30])-constants[0]*states[1])/constants[3]
    algebraic[28] = (algebraic[10]*constants[27]+constants[28])*(states[5]-constants[13])
    algebraic[11] = 0.500000*(1.00000-cos(2.00000* pi*algebraic[8]))
    algebraic[29] = (algebraic[11]*constants[29]+constants[30])*(states[6]-constants[14])
    rates[21] = custom_piecewise([greater_equal(algebraic[28] , algebraic[29]), (1.00000-states[21])*constants[35]*(algebraic[28]-algebraic[29]) , True, states[21]*constants[39]*(algebraic[28]-algebraic[29])])
    rates[22] = custom_piecewise([greater_equal(algebraic[29] , algebraic[6]), (1.00000-states[22])*constants[36]*(algebraic[29]-algebraic[6]) , True, states[22]*constants[40]*(algebraic[29]-algebraic[6])])
    algebraic[12] = amax(vstack(states[21], 0.00000),0)
    algebraic[13] = (constants[47]*constants[52]-constants[43]*constants[52])*algebraic[12]+constants[43]*constants[52]
    algebraic[15] = (constants[11]*constants[51])/(algebraic[13]+constants[70])
    algebraic[14] = constants[11]/(2.00000*(power(algebraic[13], 2.00000))+constants[70])
    rates[10] = ((-algebraic[14]*states[10]*fabs(states[10])+algebraic[28])-algebraic[29])/algebraic[15]
    algebraic[16] = amax(vstack(states[22], 0.00000),0)
    algebraic[17] = (constants[48]*constants[53]-constants[44]*constants[53])*algebraic[16]+constants[44]*constants[53]
    algebraic[19] = (constants[11]*constants[51])/(algebraic[17]+constants[70])
    algebraic[18] = constants[11]/(2.00000*(power(algebraic[17], 2.00000))+constants[70])
    rates[11] = ((-algebraic[18]*states[11]*fabs(states[11])+algebraic[29])-algebraic[6])/algebraic[19]
    algebraic[31] = (algebraic[11]*constants[33]+constants[34])*(states[8]-constants[16])
    rates[23] = custom_piecewise([greater_equal(algebraic[30] , algebraic[31]), (1.00000-states[23])*constants[37]*(algebraic[30]-algebraic[31]) , True, states[23]*constants[41]*(algebraic[30]-algebraic[31])])
    algebraic[20] = amax(vstack(states[23], 0.00000),0)
    algebraic[21] = (constants[49]*constants[54]-constants[45]*constants[54])*algebraic[20]+constants[45]*constants[54]
    algebraic[23] = (constants[11]*constants[51])/(algebraic[21]+constants[70])
    algebraic[22] = constants[11]/(2.00000*(power(algebraic[21], 2.00000))+constants[70])
    rates[12] = ((-algebraic[22]*states[12]*fabs(states[12])+algebraic[30])-algebraic[31])/algebraic[23]
    algebraic[32] = states[15]/(constants[57]/2.00000)+constants[58]
    algebraic[34] = algebraic[32]+2.00000*constants[83]*(states[13]-states[14])
    rates[24] = custom_piecewise([greater_equal(algebraic[31] , algebraic[34]), (1.00000-states[24])*constants[38]*(algebraic[31]-algebraic[34]) , True, states[24]*constants[42]*(algebraic[31]-algebraic[34])])
    algebraic[24] = amax(vstack(states[24], 0.00000),0)
    algebraic[25] = (constants[50]*constants[55]-constants[46]*constants[55])*algebraic[24]+constants[46]*constants[55]
    algebraic[27] = (constants[11]*constants[51])/(algebraic[25]+constants[70])
    algebraic[26] = constants[11]/(2.00000*(power(algebraic[25], 2.00000))+constants[70])
    rates[13] = ((-algebraic[26]*states[13]*fabs(states[13])+algebraic[31])-algebraic[34])/algebraic[27]
    algebraic[33] = states[26]/(constants[57]/2.00000)+constants[58]
    algebraic[35] = algebraic[33]+2.00000*constants[83]*(states[14]-states[16])
    rates[14] = ((algebraic[34]-algebraic[35])-constants[56]*states[14])/constants[59]
    algebraic[36] = states[17]/constants[61]+constants[62]
    algebraic[37] = algebraic[36]+constants[85]*(states[16]-states[0])
    rates[16] = ((algebraic[35]-algebraic[37])-(states[16]*constants[60])/2.00000)/constants[84]
    algebraic[38] = (states[19]+constants[68])-constants[75]
    algebraic[39] = algebraic[38]/constants[64]+constants[65]
    algebraic[41] = algebraic[39]+constants[86]*(algebraic[0]-states[18])
    rates[0] = ((algebraic[37]-algebraic[41])-(states[0]*constants[60])/2.00000)/constants[84]
    rates[18] = ((algebraic[41]-algebraic[28])-constants[63]*states[18])/constants[66]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[0] = states[0]
    algebraic[1] = (states[2]+constants[5])-constants[73]
    algebraic[2] = algebraic[1]/constants[1]+constants[2]
    algebraic[4] = algebraic[2]+constants[76]*(states[3]-states[1])
    algebraic[5] = states[4]/constants[8]+constants[9]
    algebraic[6] = algebraic[5]+constants[77]*(states[11]-states[3])
    algebraic[9] = states[20]-floor(states[20])
    algebraic[7] = states[9]-floor(states[9])
    algebraic[8] = states[25]-floor(states[25])
    algebraic[10] = 0.500000*(1.00000-cos(2.00000* pi*algebraic[7]))
    algebraic[30] = (algebraic[10]*constants[31]+constants[32])*(states[7]-constants[15])
    algebraic[28] = (algebraic[10]*constants[27]+constants[28])*(states[5]-constants[13])
    algebraic[11] = 0.500000*(1.00000-cos(2.00000* pi*algebraic[8]))
    algebraic[29] = (algebraic[11]*constants[29]+constants[30])*(states[6]-constants[14])
    algebraic[12] = amax(vstack(states[21], 0.00000),0)
    algebraic[13] = (constants[47]*constants[52]-constants[43]*constants[52])*algebraic[12]+constants[43]*constants[52]
    algebraic[15] = (constants[11]*constants[51])/(algebraic[13]+constants[70])
    algebraic[14] = constants[11]/(2.00000*(power(algebraic[13], 2.00000))+constants[70])
    algebraic[16] = amax(vstack(states[22], 0.00000),0)
    algebraic[17] = (constants[48]*constants[53]-constants[44]*constants[53])*algebraic[16]+constants[44]*constants[53]
    algebraic[19] = (constants[11]*constants[51])/(algebraic[17]+constants[70])
    algebraic[18] = constants[11]/(2.00000*(power(algebraic[17], 2.00000))+constants[70])
    algebraic[31] = (algebraic[11]*constants[33]+constants[34])*(states[8]-constants[16])
    algebraic[20] = amax(vstack(states[23], 0.00000),0)
    algebraic[21] = (constants[49]*constants[54]-constants[45]*constants[54])*algebraic[20]+constants[45]*constants[54]
    algebraic[23] = (constants[11]*constants[51])/(algebraic[21]+constants[70])
    algebraic[22] = constants[11]/(2.00000*(power(algebraic[21], 2.00000))+constants[70])
    algebraic[32] = states[15]/(constants[57]/2.00000)+constants[58]
    algebraic[34] = algebraic[32]+2.00000*constants[83]*(states[13]-states[14])
    algebraic[24] = amax(vstack(states[24], 0.00000),0)
    algebraic[25] = (constants[50]*constants[55]-constants[46]*constants[55])*algebraic[24]+constants[46]*constants[55]
    algebraic[27] = (constants[11]*constants[51])/(algebraic[25]+constants[70])
    algebraic[26] = constants[11]/(2.00000*(power(algebraic[25], 2.00000))+constants[70])
    algebraic[33] = states[26]/(constants[57]/2.00000)+constants[58]
    algebraic[35] = algebraic[33]+2.00000*constants[83]*(states[14]-states[16])
    algebraic[36] = states[17]/constants[61]+constants[62]
    algebraic[37] = algebraic[36]+constants[85]*(states[16]-states[0])
    algebraic[38] = (states[19]+constants[68])-constants[75]
    algebraic[39] = algebraic[38]/constants[64]+constants[65]
    algebraic[41] = algebraic[39]+constants[86]*(algebraic[0]-states[18])
    algebraic[3] = algebraic[1]+constants[73]
    algebraic[40] = algebraic[38]+constants[75]
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 10, 500)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,vstack((states,algebraic)).T)
    pylab.xlabel(legend_voi)
    pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()

if __name__ == "__main__":
    (voi, states, algebraic) = solve_model()
    plot_model(voi, states, algebraic)

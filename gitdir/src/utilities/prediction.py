
from protocol_funcs.py import run_protocols

protocol_info = {"protocol_info":
{ "pre_times": [20.791666666, 0, 20.791666666],
"sim_times": [[ 3.6734693877, 5, 3.6734693877]],
"params_to_change": {
"venous_svc/v_inf": [[0, 0.0001, 0]]},
"experiment_colors": ["r"],
"experiment_labels": ["inf"]
}}

run_protocols("/hpc/vken399/Examensprojekt_hpc/CA_user/3compartment/generated_models/3compartment_3compartment_obs_data/3compartment.cellml",["aortic_root/v"], protocol_info)






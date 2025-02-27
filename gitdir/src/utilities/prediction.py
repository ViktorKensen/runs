from protocol_funcs import run_protocols
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

protocol_info = {"protocol_info":
{ "pre_times": [20.791666666],
"sim_times": [[ 20.791666666, 5, 20.791666666]],
"params_to_change": {
"venous_svc/v_inf": [[0, 0.0001, 0]]},
"experiment_colors": ["r"],
"experiment_labels": ["inf"]
}}

model_path = "/hpc/vken399/Examensprojekt_hpc/CA_user/3compartment/generated_models/3compartment_3compartment_obs_data/3compartment.cellml"

parameters_to_plot = ["aortic_root/v"]

t_list, res_list = run_protocols(model_path, parameters_to_plot, protocol_info['protocol_info'])

# Load ground truth data
ground_truth = pd.read_csv('ground_truth.csv')

# Plot the results
plt.figure(figsize=(8, 6))

for exp_idx, (t_vec, res_vec) in enumerate(zip(t_list, res_list)):
    for var_idx, var_data in enumerate(res_vec):
        mean_val = np.mean(var_data)
        plt.plot(t_vec, var_data, label=f"Experiment {exp_idx + 1} - {parameters_to_plot[var_idx]}", color=protocol_info['protocol_info']['experiment_colors'][exp_idx])
        plt.axhline(mean_val, linestyle='--', color='blue', label=f"Mean {parameters_to_plot[var_idx]}")

        # Plot ground truth if variable exists in CSV
        if parameters_to_plot[var_idx] in ground_truth.columns:
            ground_truth_val = ground_truth[parameters_to_plot[var_idx]].values[0]
            plt.axhline(ground_truth_val, linestyle='-.', color='green', label=f"Ground Truth {parameters_to_plot[var_idx]}")

plt.xlabel('Time (s)')
plt.ylabel('Variable Value')
plt.title('Simulation Results')
plt.legend()
plt.grid(True)
plt.savefig('simulation_results.png')


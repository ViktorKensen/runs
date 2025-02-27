import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from protocol_funcs import run_protocols
import ast

protocol_info = {
    "protocol_info": {
        "pre_times": [20.791666666],
        "sim_times": [[20.791666666, 5, 20.791666666]],
        "params_to_change": {
            "venous_svc/v_inf": [[0, 0.0001, 0]]
        },
        "experiment_colors": ["r"],
        "experiment_labels": ["inf"]
    }
}

model_path = "/hpc/vken399/Examensprojekt_hpc/CA_user/3compartment/generated_models/3compartment_3compartment_obs_data/3compartment.cellml"
parameters_to_plot = ["aortic_root/v"]

t_list, res_list = run_protocols(model_path, parameters_to_plot, protocol_info['protocol_info'])

# Load ground truth data
ground_truth = pd.read_csv('ground_truth.csv')

# Initialize a dictionary to store mean values for each variable
mean_values_dict = {var: [] for var in parameters_to_plot}

# Plot the results
plt.figure(figsize=(10, 8))

for exp_idx, (t_vec, res_vec) in enumerate(zip(t_list, res_list)):
    for var_idx, var_data in enumerate(res_vec):
        sim_times = protocol_info['protocol_info']['sim_times'][exp_idx]
        
        # Calculate mean values for the first and last simulation times
        mean_val_first = np.mean(var_data[:len(var_data)//2])
        mean_val_last = np.mean(var_data[len(var_data)//2:])
        
        # Append mean values as a list to the dictionary
        mean_values_dict[parameters_to_plot[var_idx]].append([mean_val_first, mean_val_last])
        
        # Plot the simulation data
        plt.plot(t_vec, var_data, label=f"Experiment {exp_idx + 1} - {parameters_to_plot[var_idx]}", color=protocol_info['protocol_info']['experiment_colors'][exp_idx])
        
        # Plot the mean values for the first and last simulation times only for their respective portions
        plt.plot([0, sim_times[0]], [mean_val_first, mean_val_first], linestyle='--', color='blue', linewidth=2.5, label=f"Mean First {parameters_to_plot[var_idx]}")
        plt.plot([sum(sim_times[:2]), sum(sim_times)], [mean_val_last, mean_val_last], linestyle='--', color='red', linewidth=2.5, label=f"Mean Last {parameters_to_plot[var_idx]}")

        # Plot ground truth if variable exists in CSV
        if parameters_to_plot[var_idx] in ground_truth.columns:
            ground_truth_vals = ast.literal_eval(ground_truth[parameters_to_plot[var_idx]].values[0])

            # Plot ground truth for the entirety of the first simulation time
            plt.plot([0, sim_times[0]], [ground_truth_vals[0], ground_truth_vals[0]], linestyle='-.', color='green', linewidth=2.5, label=f"Ground Truth (First) {parameters_to_plot[var_idx]}")

            # Plot ground truth for the third and final simulation time
            plt.plot([sum(sim_times[:2]), sum(sim_times)], [ground_truth_vals[1], ground_truth_vals[1]], linestyle=':', color='purple', linewidth=2.5, label=f"Ground Truth (Last) {parameters_to_plot[var_idx]}")

plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Variable Value', fontsize=12)
plt.title('Simulation Results', fontsize=14)
plt.legend(loc='upper right', fontsize='small', frameon=True)
plt.grid(True)
plt.savefig('simulation_results.png')

print("Simulation results have been plotted and saved as 'simulation_results.png'.")

# Save mean values to CSV file
mean_values_df = pd.DataFrame(mean_values_dict)
mean_values_df.to_csv('prediction_results.csv', index=False)

print("Mean values have been saved to 'prediction_results.csv'.")


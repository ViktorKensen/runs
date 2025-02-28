import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from protocol_funcs import run_protocols
#from /../scripts/param_id_run_script import run_param_id
import ast
import os 
import sys
import yaml

# Define the root directory path
root_dir_path = os.path.join(os.path.dirname(__file__), '../..', 'Examensprojekt_hpc')

# Append the necessary paths to the system path
utilities_dir = os.path.join(root_dir_path, 'gitdir', 'src', 'utilities')
scripts_dir = os.path.join(root_dir_path, 'gitdir', 'src', 'scripts')

print("Scripts Directory:", scripts_dir)

sys.path.append(utilities_dir)
sys.path.append(scripts_dir)

# Import the required function
from param_id_run_script import run_param_id

# Define the user inputs directory
user_inputs_dir = os.path.join(root_dir_path, 'CA_user', '3compartment')

# Load the input data dictionary from the YAML file
with open(os.path.join(user_inputs_dir, '3compartment_user_inputs.yaml'), 'r') as file:
    inp_data_dict = yaml.load(file, Loader=yaml.FullLoader)

# Run the parameter identification function
run_param_id(inp_data_dict)




protocol_info = {
    "protocol_info": {
        "pre_times": [20.791666666],
        "sim_times": [[20.791666666, 5, 20.791666666]],
        "params_to_change": {
            "venous_svc/v_inf": [[0, 0.0001, 0]]
        },
        "experiment_colors": ["r", "b"],
        "experiment_labels": ["inf", "heart"]
    }
}

model_path = "/hpc/vken399/Examensprojekt_hpc/CA_user/3compartment/generated_models/3compartment_3compartment_obs_data/3compartment.cellml"
parameters_to_plot = ["aortic_root/v", "heart/u_ra"]

t_list, res_list = run_protocols(model_path, parameters_to_plot, protocol_info['protocol_info'])

# Load ground truth data
ground_truth = pd.read_csv('ground_truth.csv')

# Initialize a dictionary to store mean values for each variable
mean_values_dict = {var: [] for var in parameters_to_plot}

# Plot the results for each parameter separately
for param in parameters_to_plot:
    plt.figure(figsize=(10, 8))

    for exp_idx, (t_vec, res_vec) in enumerate(zip(t_list, res_list)):
        var_data = res_vec[parameters_to_plot.index(param)]
        sim_times = protocol_info['protocol_info']['sim_times'][exp_idx]
        
        # Calculate mean values for the first and last simulation times
        mean_val_first = np.mean(var_data[:len(var_data)//2])
        mean_val_last = np.mean(var_data[len(var_data)//2:])
        
        # Append mean values as a list to the dictionary
        mean_values_dict[param].append([mean_val_first, mean_val_last])
        
        # Plot the simulation data
        plt.plot(t_vec, var_data, label=f"Experiment {exp_idx + 1} - {param}", color=protocol_info['protocol_info']['experiment_colors'][parameters_to_plot.index(param)])
        
        # Plot the mean values for the first and last simulation times only for their respective portions
        plt.plot([0, sim_times[0]], [mean_val_first, mean_val_first], linestyle=':', color='green', linewidth=2.5, label=f"Simulation Mean Pre {param}")
        plt.plot([sum(sim_times[:2]), sum(sim_times)], [mean_val_last, mean_val_last], linestyle=':', color='green', linewidth=2.5, label=f"Simulation Mean Post {param}")

        # Plot ground truth if variable exists in CSV
        if param in ground_truth.columns:
            ground_truth_vals = ast.literal_eval(ground_truth[param].values[0])

            # Plot ground truth for the entirety of the first simulation time
            plt.plot([0, sim_times[0]], [ground_truth_vals[0], ground_truth_vals[0]], linestyle=':', color='blue', linewidth=2.5, label=f"Messured Pre {param}")

            # Plot ground truth for the third and final simulation time
            plt.plot([sum(sim_times[:2]), sum(sim_times)], [ground_truth_vals[1], ground_truth_vals[1]], linestyle=':', color='blue', linewidth=2.5, label=f"Messured Post {param}")

    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Variable Value', fontsize=12)
    plt.title(f'Simulation Results for {param}', fontsize=14)
    plt.legend(loc='upper right', fontsize='small', frameon=True)
    plt.grid(True)
    plt.savefig(f'simulation_results_{param.replace("/", "_")}.png')

    print(f"Simulation results for {param} have been plotted and saved as 'simulation_results_{param.replace('/', '_')}.png'.")

# Save mean values to CSV file
mean_values_df = pd.DataFrame(mean_values_dict)
mean_values_df.to_csv('prediction_results.csv', index=False)

print("Mean values have been saved to 'prediction_results.csv'.")

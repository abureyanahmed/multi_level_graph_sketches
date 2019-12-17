from subprocess import call
import math

def generate():
  #root_folder = "experiment_1"
  #root_folder = "experiment_WS"
  #root_folder = "experiment_consistent_ER"
  #root_folder = "experiment_consistent_ER_2"
  #root_folder = "experiment_consistent_ER_3"
  #root_folder = "experiment_consistent_ER_4"
  root_folder = "experiment_consistent_ER_5"
  #call(["rm", "-rf", "Graph_generator/"+experiment_name])
  call(["mkdir", root_folder])
  #name_of_graph_class = ['WS','ER','BA','GE']
  #name_of_graph_class_code = ['0','1','2','3']
  name_of_graph_class = ['ER']
  #name_of_graph_class = ['WS']
  name_of_graph_class_code = ['1']
  #name_of_graph_class_code = ['0']
  #number_of_nodes_progression = [100, 100, 100]
  #number_of_levels = [1, 2, 3]
  #number_of_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  number_of_levels = [1, 2, 3, 4, 5, 6]
  #number_of_nodes_progression = [15, 15, 15]
  #number_of_levels = [1, 2, 3]
  #node_distribution_in_levels = ['L','E']
  #node_distribution_in_levels_code = ['0','1']
  #node_distribution_in_levels = ['L']
  #node_distribution_in_levels_code = ['0']
  #param1 = ['6', '.25', '5', '1.62']
  #param2 = ['.2', '0', '0', '0']
  param1 = ['.25']
  param2 = ['0']
  #param1 = ['6']
  #param2 = ['.2']
  stretch_factor = [1.2, 1.4, 2, 4]
  #stretch_factor = [2]
  #stretch_factor = [1.2, 1.4, 4]
  #stretch_factor_str = ['1_2', '1_4', '2', '4']
  #initial_nodes = 10
  #node_increment = 5
  #initial_nodes = 50
  initial_nodes = 100
  final_nodes = 300
  #final_nodes = 500
  #final_nodes = 100
  #node_increment = 10
  #node_increment = 50
  node_increment = 100
  curr_id = 1
  #curr_id = 16
  #curr_id = 26
  f1 = open(root_folder + '/id_to_file.csv', 'w')
  f2 = open(root_folder + '/id_to_file_BU_exact.csv', 'w')
  f3 = open(root_folder + '/id_to_file_TD_exact.csv', 'w')
  f4 = open(root_folder + '/id_to_file_CMP_exact.csv', 'w')
  #f1 = open(root_folder + '/id_to_file.csv', 'a')
  #f2 = open(root_folder + '/id_to_file_BU_exact.csv', 'a')
  #f3 = open(root_folder + '/id_to_file_TD_exact.csv', 'a')
  for cl in range(len(name_of_graph_class)):
   #for l in range(len(number_of_levels)):
    #for nd in range(len(node_distribution_in_levels)):
     #for sf in range(len(stretch_factor)):
      #common_part_of_name = name_of_graph_class[cl]+'_'+str(number_of_nodes_progression[l])+'_'+str(number_of_levels[l])+'_'+node_distribution_in_levels[nd]+'_'+stretch_factor_str[sf]
      common_part_of_name = name_of_graph_class[cl]
      call(["mkdir", root_folder + "/" + common_part_of_name])
      #for p in range(initial_nodes, number_of_nodes_progression[l]+1, node_increment):
      for p in range(initial_nodes, final_nodes+1, node_increment):
       if name_of_graph_class[cl] == 'ER':
        param1[cl] = str((1+1)*math.log(p)/p)
       elif name_of_graph_class[cl] == 'GE':
        param1[cl] = str(math.sqrt((1+1)*math.log(p)/(math.pi*p)))
       call(["python3", "graph_generator.py", "1", "0", str(p), root_folder + "/" + common_part_of_name + "/graph_" + str(p), name_of_graph_class_code[cl], param1[cl], param2[cl], "0"])
       #for l in range(len(number_of_levels)):
       for l in range(1, len(number_of_levels)+1, 2):
       #for l in range(7, len(number_of_levels)+1, 2):
        for sf in range(len(stretch_factor)):
         f1.write(str(curr_id) + ';' + 'spanner_exact_algorithm_only_lp.py' + ';' + root_folder + "/" + common_part_of_name +';' + "graph_" + str(p) + "_1" + ';' + str(stretch_factor[sf]) + ';' + str(l+1) + ';\n')
         f2.write(str(curr_id) + ';' + 'bot_up_approx_consistent_param.py' + ';' + root_folder + "/" + common_part_of_name +';' + "graph_" + str(p) + "_1" + ';' + str(stretch_factor[sf]) + ';' + str(l+1) + ';\n')
         #f2.write(str(curr_id) + ';' + 'bot_up_approx_subsetwise.py' + ';' + root_folder + "/" + common_part_of_name +';' + "graph_" + str(p) + "_1" + ';' + str(stretch_factor[sf]) + ';' + str(l+1) + ';\n')
         f3.write(str(curr_id) + ';' + 'top_down_approx_consistent_param.py' + ';' + root_folder + "/" + common_part_of_name +';' + "graph_" + str(p) + "_1" + ';' + str(stretch_factor[sf]) + ';' + str(l+1) + ';\n')
         f4.write(str(curr_id) + ';' + 'composite_approx_consistent_param.py' + ';' + root_folder + "/" + common_part_of_name +';' + "graph_" + str(p) + "_1" + ';' + str(stretch_factor[sf]) + ';' + str(l+1) + ';\n')
         curr_id = curr_id + 1
  f1.close()
  f2.close()
  f3.close()
  f4.close()

generate()



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from ilp_checker_lib import *
import sys
from collections import OrderedDict
import matplotlib.patches as mpatches
from input_functions import *
from matplotlib.ticker import MaxNLocator

fig_count = 0
my_inf = 10000000

def line_plot(experiment_folder, file_name, out_dir, dependent, exact, y_min, y_max):
  global fig_count
  path_to_plots_directory = experiment_folder + 'plots/'
  node, level, obj, heu_obj, stretch = parse_output_file(experiment_folder, out_dir, exact, False, False)
  max_dict = OrderedDict()
  min_dict = OrderedDict()
  sum_dict = OrderedDict()
  count_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  for i in range(len(obj)):
    if obj[i]!=-1 and heu_obj[i]!=-1:
      rat = heu_obj[i]/obj[i]
      if rat<1.0:rat=1.0
      if dependent_var[i] in max_dict.keys():
        if max_dict[dependent_var[i]]<rat:
          max_dict[dependent_var[i]] = rat
        if min_dict[dependent_var[i]]>rat:
          min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = sum_dict[dependent_var[i]] + rat
        count_dict[dependent_var[i]] = count_dict[dependent_var[i]] + 1
      else:
        max_dict[dependent_var[i]] = rat
        min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = rat
        count_dict[dependent_var[i]] = 1
  label = []
  max_ratios = []
  min_ratios = []
  avg_ratios = []
  for k in max_dict.keys():
    label.append(k)
    max_ratios.append(max_dict[k])
    min_ratios.append(min_dict[k])
    avg_ratios.append(sum_dict[k]/count_dict[k])
  print(label, max_ratios, avg_ratios, min_ratios)

  if dependent=='level':
    ax = plt.figure(fig_count).gca()
    fig_count = fig_count + 1
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  #plt.plot(label, max_ratios, 'r--', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  plt.plot(label, max_ratios, 'ro', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  plt.ylabel('Ratio', fontsize=20)
  #plt.ylim(1,max_label)
  #plt.ylim(.94,1.8)
  #plt.ylim(.94,1.9)
  plt.ylim(y_min, y_max)
  plt.legend(['max', 'avg', 'min'], loc='upper right', fontsize=16)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  #plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def line_plot_composite(experiment_folder, file_name, dependent, exact, y_min, y_max):
  global my_inf, fig_count
  path_to_plots_directory = experiment_folder + 'plots/'
  if exact:
    node, level, obj, heu_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'log_folder_TD_exact/', exact, True, False)
  else:
    node, level, obj, heu_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'bottom_up_output.txt', exact, False, False)
    node, level, obj, heu_obj_2, stretch = parse_output_file(experiment_folder, experiment_folder + 'top_down_output.txt', exact, False, False)
  max_dict = OrderedDict()
  min_dict = OrderedDict()
  sum_dict = OrderedDict()
  count_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  for i in range(len(obj)):
    if obj[i]!=-1 and heu_obj[i]!=-1:
      rat = heu_obj[i]/obj[i]
      if rat<1.0:rat=1.0
      if dependent_var[i] in max_dict.keys():
        if max_dict[dependent_var[i]]<rat:
          max_dict[dependent_var[i]] = rat
        if min_dict[dependent_var[i]]>rat:
          min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = sum_dict[dependent_var[i]] + rat
        count_dict[dependent_var[i]] = count_dict[dependent_var[i]] + 1
      else:
        max_dict[dependent_var[i]] = rat
        min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = rat
        count_dict[dependent_var[i]] = 1
  label = []
  max_ratios = []
  min_ratios = []
  avg_ratios = []
  for k in max_dict.keys():
    label.append(k)
    max_ratios.append(max_dict[k])
    min_ratios.append(min_dict[k])
    avg_ratios.append(sum_dict[k]/count_dict[k])
  print(label, max_ratios, avg_ratios, min_ratios)

  if dependent=='level':
    ax = plt.figure(fig_count).gca()
    fig_count = fig_count + 1
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  #plt.plot(label, max_ratios, 'r--', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  plt.plot(label, max_ratios, 'ro', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  plt.ylabel('Ratio', fontsize=20)
  #plt.ylim(1,max_label)
  #plt.ylim(.94,1.8)
  #plt.ylim(.94,1.9)
  plt.ylim(y_min, y_max)
  plt.legend(['max', 'avg', 'min'], loc='upper right', fontsize=16)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  #plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def line_plot_min(experiment_folder, file_name, dependent, exact, y_min, y_max):
  global my_inf, log_folder_BU_exact, fig_count
  path_to_plots_directory = experiment_folder + 'plots/'
  if exact:
    node, level, obj, heu_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_BU_exact + '/', exact, False, False)
    node, level, obj, heu_obj_2, stretch = parse_output_file(experiment_folder, experiment_folder + 'log_folder_TD_exact/', exact, False, False)
  else:
    node, level, obj, heu_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'bottom_up_output.txt', exact, False, False)
    node, level, obj, heu_obj_2, stretch = parse_output_file(experiment_folder, experiment_folder + 'top_down_output.txt', exact, False, False)
  max_dict = OrderedDict()
  min_dict = OrderedDict()
  sum_dict = OrderedDict()
  count_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  for i in range(len(obj)):
    if obj[i]!=-1 and (heu_obj[i]!=-1 or heu_obj_2[i]!=-1):
      rat = heu_obj[i]/obj[i]
      rat_2 = heu_obj_2[i]/obj[i]
      rat = min(rat, rat_2)
      if dependent_var[i] in max_dict.keys():
        if max_dict[dependent_var[i]]<rat:
          max_dict[dependent_var[i]] = rat
        if min_dict[dependent_var[i]]>rat:
          min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = sum_dict[dependent_var[i]] + rat
        count_dict[dependent_var[i]] = count_dict[dependent_var[i]] + 1
      else:
        max_dict[dependent_var[i]] = rat
        min_dict[dependent_var[i]] = rat
        sum_dict[dependent_var[i]] = rat
        count_dict[dependent_var[i]] = 1
  label = []
  max_ratios = []
  min_ratios = []
  avg_ratios = []
  for k in max_dict.keys():
    label.append(k)
    max_ratios.append(max_dict[k])
    min_ratios.append(min_dict[k])
    avg_ratios.append(sum_dict[k]/count_dict[k])
  print(label, max_ratios, avg_ratios, min_ratios)

  if dependent=='level':
    ax = plt.figure(fig_count).gca()
    fig_count = fig_count + 1
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  #plt.plot(label, max_ratios, 'r--', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  plt.plot(label, max_ratios, 'ro', label, avg_ratios, 'bs', label, min_ratios, 'g^')
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  plt.ylabel('Ratio', fontsize=20)
  #plt.ylim(1,max_label)
  #plt.ylim(.94,1.8)
  #plt.ylim(.94,1.9)
  plt.ylim(y_min, y_max)
  plt.legend(['max', 'avg', 'min'], loc='upper right', fontsize=16)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  #plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def box_plot(experiment_folder, file_name, dependent, exact, y_min, y_max):
  global fig_count, my_inf, log_folder_BU_exact, log_folder_TD_exact
  path_to_plots_directory = experiment_folder + 'plots/'
  if exact:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_BU_exact + '/', exact, False, False)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_TD_exact + '/', exact, False, False)
  else:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'bottom_up_output.txt', exact, False, False)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'top_down_output.txt', exact, False, False)
  BU_dict = OrderedDict()
  TD_dict = OrderedDict()
  min_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  if 'consistent' not in experiment_folder:
    len_obj = len(obj)
  else:
    len_obj = len(BU_exact_obj)
    obj = BU_exact_obj
  if 'consistent' in experiment_folder:
    min_obj = []
    for i in range(len_obj):
      if BU_exact_obj[i]==-1 or TD_exact_obj[i]==-1:
        min_obj.append(max(BU_exact_obj[i], TD_exact_obj[i]))
      else:
        min_obj.append(min(BU_exact_obj[i], TD_exact_obj[i]))
  for i in range(len_obj):
    if obj[i]!=-1 and BU_exact_obj[i]!=-1:
      if 'consistent' not in experiment_folder:
        rat = BU_exact_obj[i]/obj[i]
      else:
        rat = BU_exact_obj[i]/min_obj[i]
      if dependent_var[i] not in BU_dict.keys():
        BU_dict[dependent_var[i]] = []
      BU_dict[dependent_var[i]].append(rat)
  print(BU_dict)
  for i in range(len_obj):
    if obj[i]!=-1 and TD_exact_obj[i]!=-1:
      if 'consistent' not in experiment_folder:
        rat = TD_exact_obj[i]/obj[i]
      else:
        rat = TD_exact_obj[i]/min_obj[i]
      if dependent_var[i] not in TD_dict.keys():
        TD_dict[dependent_var[i]] = []
      TD_dict[dependent_var[i]].append(rat)
  print(TD_dict)
  for i in range(len_obj):
    if obj[i]!=-1 and (BU_exact_obj[i]!=-1 or TD_exact_obj[i]!=-1):
      if BU_exact_obj[i]!=-1:
        if 'consistent' not in experiment_folder:
          rat_BU = BU_exact_obj[i]/obj[i]
        else:
          rat_BU = BU_exact_obj[i]
      else:
        rat_BU = my_inf
      if TD_exact_obj[i]!=-1:
        if 'consistent' not in experiment_folder:
          rat_TD = TD_exact_obj[i]/obj[i]
        else:
          rat_TD = TD_exact_obj[i]
      else:
        rat_TD = my_inf
      if dependent_var[i] not in min_dict.keys():
        min_dict[dependent_var[i]] = []
      min_rat = min(rat_BU, rat_TD)
      min_dict[dependent_var[i]].append(min_rat)
  print(min_dict)
  size = len(BU_dict.keys())
  label_ind = 0
  labels = []
  sorted_keys = []
  for k in BU_dict.keys():
    sorted_keys.append(k)
  sorted_keys.sort()
  for k in sorted_keys:
    labels.append(k)
  data = []
  gaps = 1
  i = 0
  for k in sorted_keys:
    data.append(BU_dict[k])
    data.append(TD_dict[k])
    if 'consistent' not in experiment_folder:
      data.append(min_dict[k])
    if i<size-1:
      for g in range(gaps):
        # some space
        data.append([])
    i = i + 1

  min_len = len(data[0])
  for i in range(len(data)):
    if len(data[i])==0:continue
    data[i].sort()
    if min_len>len(data[i]):min_len=len(data[i])
    data[i] = data[i][::-1]
  print('min_len', min_len)
  print(data)
  if 'consistent' not in experiment_folder:
    for i in range(len(data)):
      data[i] = data[i][:min_len-5]
      #data[i] = data[i][:min_len-1]
      if len(data[i])>0:data[i].append(1.0)
  print(data)

  plt.figure(fig_count)
  fig_count = fig_count + 1
  if 'consistent' not in experiment_folder:
    color = ['red', 'blue', 'violet']
  else:
    color = ['red', 'blue']
  #text = ['BU', 'TD', 'min(BU, TD)']
  if 'consistent' not in experiment_folder:
    text = ['BU', 'TD', 'CMP']
    #text = ['BU', 'TD', 'min(BU, TD)']
  else:
    text = ['BU', 'TD']
  bp = plt.boxplot(data, 0, '', whis=1000, patch_artist=True)
  i = 0
  for box in bp['boxes']:
    # change outline color
    # check whether it is a gap, if gap no need to color
    c_i = i%(len(text)+gaps)
    if c_i<len(text):
      box.set(color=color[c_i], linewidth=2)
    i = i + 1
  handles = []
  for i in range(len(text)):
    patch = mpatches.Patch(color=color[i], label=text[i])
    handles.append(patch)
  plt.legend(handles=handles)
  label_i = 1
  # labels computation is complex, it has add 2 for gaps, negate 2 for boundary condition 
  if 'consistent' not in experiment_folder:
    tmp = range(1,size*(len(text)+gaps)+1-2)
  else:
    tmp = range(1,size*(len(text)+gaps)+1-1)
  tmp2 = []
  for i in range(len(tmp)):
    # Add 2 with len(text) because we want two gaps between groups of boxes
    if i%(len(text)+gaps)==label_i:
      tmp2.append(labels[label_ind])
      label_ind = label_ind + 1
    else:
      tmp2.append('')
  plt.xticks(tmp, tmp2)
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  if 'consistent' not in experiment_folder:
    plt.ylabel('Ratio', fontsize=20)
    plt.ylim(y_min, y_max)
  else:
    plt.ylabel('Ratio', fontsize=20)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def box_plot_time(experiment_folder, file_name, dependent, exact):
  global fig_count, my_inf, log_folder_BU_exact, log_folder_TD_exact, log_folder_CMP_exact
  path_to_plots_directory = experiment_folder + 'plots/'
  if exact:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_BU_exact + '/', exact, False, True)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_TD_exact+ '/', exact, False, True)
    node, level, obj, CMP_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_CMP_exact+ '/', exact, False, True)
  else:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'bottom_up_output.txt', exact, False, True)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'top_down_output.txt', exact, False, True)
  BU_dict = OrderedDict()
  TD_dict = OrderedDict()
  CMP_dict = OrderedDict()
  min_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  if 'consistent' not in experiment_folder:
    len_obj = len(obj)
  else:
    len_obj = len(BU_exact_obj)
    obj = BU_exact_obj
  for i in range(len_obj):
    #if obj[i]!=-1 and BU_exact_obj[i]!=-1:
    if BU_exact_obj[i]!=-1:
      #rat = BU_exact_obj[i]/obj[i]
      if exact:
        rat = BU_exact_obj[i]/3600
      else:
        rat = BU_exact_obj[i]
      #if rat<1.0:rat=1.0
      if dependent_var[i] not in BU_dict.keys():
        BU_dict[dependent_var[i]] = []
      BU_dict[dependent_var[i]].append(rat)
  print(BU_dict)
  for i in range(len_obj):
    #if obj[i]!=-1 and TD_exact_obj[i]!=-1:
    if TD_exact_obj[i]!=-1:
      #rat = TD_exact_obj[i]/obj[i]
      if exact:
        rat = TD_exact_obj[i]/3600
      else:
        rat = TD_exact_obj[i]
      #if rat<1.0:rat=1.0
      if dependent_var[i] not in TD_dict.keys():
        TD_dict[dependent_var[i]] = []
      TD_dict[dependent_var[i]].append(rat)
  print(TD_dict)
  for i in range(len_obj):
    if node[i]==500:continue
    #if obj[i]!=-1 and TD_exact_obj[i]!=-1:
    if CMP_exact_obj[i]!=-1:
      #rat = TD_exact_obj[i]/obj[i]
      if exact:
        rat = CMP_exact_obj[i]/3600
      else:
        rat = CMP_exact_obj[i]
      #if rat<1.0:rat=1.0
      if dependent_var[i] not in CMP_dict.keys():
        CMP_dict[dependent_var[i]] = []
      CMP_dict[dependent_var[i]].append(rat)
  print(CMP_dict)
  for i in range(len_obj):
    #if obj[i]!=-1 and (BU_exact_obj[i]!=-1 or TD_exact_obj[i]!=-1):
    if BU_exact_obj[i]!=-1 or TD_exact_obj[i]!=-1:
      if BU_exact_obj[i]!=-1:
        #rat_BU = BU_exact_obj[i]/obj[i]
        if exact:
          rat_BU = BU_exact_obj[i]/3600
        else:
          rat_BU = BU_exact_obj[i]
        #if rat_BU<1.0:rat_BU=1.0
      else:
        #rat_BU = my_inf
        rat_BU = 1
      if TD_exact_obj[i]!=-1:
        #rat_TD = TD_exact_obj[i]/obj[i]
        if exact:
          rat_TD = TD_exact_obj[i]/3600
        else:
          rat_TD = TD_exact_obj[i]
        #if rat_TD<1.0:rat_TD=1.0
      else:
        #rat_TD = my_inf
        rat_TD = 1
      if dependent_var[i] not in min_dict.keys():
        min_dict[dependent_var[i]] = []
      #min_dict[dependent_var[i]].append(min(rat_BU, rat_TD))
      min_dict[dependent_var[i]].append(max(rat_BU, rat_TD))
  print(min_dict)
  size = len(BU_dict.keys())
  label_ind = 0
  labels = []
  sorted_keys = []
  for k in BU_dict.keys():
    sorted_keys.append(k)
  sorted_keys.sort()
  for k in sorted_keys:
    labels.append(k)
  data = []
  gaps = 1
  i = 0
  for k in sorted_keys:
    data.append(BU_dict[k])
    data.append(TD_dict[k])
    data.append(CMP_dict[k])
    if i<size-1:
      for g in range(gaps):
        # some space
        data.append([])
    i = i + 1

  min_len = len(data[0])
  for i in range(len(data)):
    if len(data[i])==0:continue
    data[i].sort()
    if min_len>len(data[i]):min_len=len(data[i])
    data[i] = data[i][::-1]
  print('min_len', min_len)
  if 'consistent' not in experiment_folder:
    for i in range(len(data)):
      data[i] = data[i][:min_len-5]

  plt.figure(fig_count)
  fig_count = fig_count + 1
  color = ['red', 'blue', 'violet']
  #text = ['BU', 'TD', 'min(BU, TD)']
  text = ['BU', 'TD', 'CMP']
  bp = plt.boxplot(data, 0, '', whis=1000, patch_artist=True)
  i = 0
  for box in bp['boxes']:
    # change outline color
    # check whether it is a gap, if gap no need to color
    c_i = i%(len(text)+gaps)
    if c_i<len(text):
      box.set(color=color[c_i], linewidth=2)
    i = i + 1
  handles = []
  for i in range(len(text)):
    patch = mpatches.Patch(color=color[i], label=text[i])
    handles.append(patch)
  plt.legend(handles=handles)
  label_i = 1
  # labels computation is complex, it has add 2 for gaps, negate 2 for boundary condition 
  tmp = range(1,size*(len(text)+gaps)+1-2)
  tmp2 = []
  for i in range(len(tmp)):
    # Add 2 with len(text) because we want two gaps between groups of boxes
    if i%(len(text)+gaps)==label_i:
      tmp2.append(labels[label_ind])
      label_ind = label_ind + 1
    else:
      tmp2.append('')
  plt.xticks(tmp, tmp2)
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  #plt.ylabel('Ratio', fontsize=20)
  if exact:
    plt.ylabel('Time (hours)', fontsize=20)
  else:
    plt.ylabel('Time (seconds)', fontsize=20)
  #plt.ylim(y_min, y_max)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def box_plot_single(experiment_folder, file_name, dependent, exact, prop):
  global fig_count, my_inf, log_folder_BU_exact
  path_to_plots_directory = experiment_folder + 'plots/'
  if exact:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + log_folder_BU_exact + '/', exact, False, True)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'log_folder_TD_exact/', exact, False, True)
  else:
    node, level, obj, BU_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'bottom_up_output.txt', exact, False, False)
    node, level, obj, TD_exact_obj, stretch = parse_output_file(experiment_folder, experiment_folder + 'top_down_output.txt', exact, False, False)
  if prop=='density':
    densities = get_density(experiment_folder)
  exact_dict = OrderedDict()
  #BU_dict = OrderedDict()
  #TD_dict = OrderedDict()
  #min_dict = OrderedDict()
  if dependent=='node':
    dependent_var = node
  elif dependent=='level':
    dependent_var = level
  elif dependent=='stretch':
    dependent_var = stretch
  for i in range(len(obj)):
    if obj[i]!=-1:
      rat = obj[i]/3600
      if prop=='density':
        rat = densities[i]
      if dependent_var[i] not in exact_dict.keys():
        exact_dict[dependent_var[i]] = []
      exact_dict[dependent_var[i]].append(rat)
  print(exact_dict)
  #for i in range(len(obj)):
  #  if obj[i]!=-1 and BU_exact_obj[i]!=-1:
  #    rat = BU_exact_obj[i]
  #    if dependent_var[i] not in BU_dict.keys():
  #      BU_dict[dependent_var[i]] = []
  #    BU_dict[dependent_var[i]].append(rat)
  #print(BU_dict)
  #for i in range(len(obj)):
  #  if obj[i]!=-1 and TD_exact_obj[i]!=-1:
  #    rat = TD_exact_obj[i]
  #    if dependent_var[i] not in TD_dict.keys():
  #      TD_dict[dependent_var[i]] = []
  #    TD_dict[dependent_var[i]].append(rat)
  #print(TD_dict)
  #for i in range(len(obj)):
  #  if obj[i]!=-1 and (BU_exact_obj[i]!=-1 or TD_exact_obj[i]!=-1):
  #    if BU_exact_obj[i]!=-1:
  #      rat_BU = BU_exact_obj[i]
  #    else:
  #      rat_BU = my_inf
  #    if TD_exact_obj[i]!=-1:
  #      rat_TD = TD_exact_obj[i]
  #    else:
  #      rat_TD = my_inf
  #    if dependent_var[i] not in min_dict.keys():
  #      min_dict[dependent_var[i]] = []
  #    #t = min(rat_BU, rat_TD)
  #    t = rat_TD
  #    min_dict[dependent_var[i]].append(t)
  #print(min_dict)
  #size = len(BU_dict.keys())
  size = len(exact_dict.keys())
  label_ind = 0
  labels = []
  for k in exact_dict.keys():
    labels.append(k)
  data = []
  gaps = 1
  i = 0
  for k in exact_dict.keys():
    data.append(exact_dict[k])
  min_len = len(data[0])
  for i in range(len(data)):
    data[i].sort()
    if min_len>len(data[i]):min_len=len(data[i])
    data[i] = data[i][::-1]
  print('min_len', min_len)
  for i in range(len(data)):
    data[i] = data[i][:min_len-5]
    #data[i] = data[i][:10]
  plt.figure(fig_count)
  fig_count = fig_count + 1
  bp = plt.boxplot(data, 0, '', whis=1000, patch_artist=True)
  i = 0
  tmp = range(1, len(labels)+1)
  tmp2 = labels
  plt.xticks(tmp, tmp2)
  if dependent=='node':
    plt.xlabel('Number of vertices', fontsize=20)
  elif dependent=='level':
    plt.xlabel('Number of levels', fontsize=20)
  elif dependent=='stretch':
    plt.xlabel('Stretch factors', fontsize=20)
  if prop=='time':
    plt.ylabel('Time (hours)', fontsize=20)
  if prop=='density':
    plt.ylabel('Density', fontsize=20)
  #plt.ylim(.94,1.27)
  plt.tick_params(axis='x', labelsize=16)
  plt.tick_params(axis='y', labelsize=16)
  plt.show()
  plt.savefig(path_to_plots_directory+file_name, bbox_inches='tight')
  plt.close()

def parse_id_csv(experiment_folder):
  folders = []
  stretch = []
  file_names = []
  level = []
  node = []
  f = open(experiment_folder + 'id_to_file.csv', 'r')
  line_number = 1
  while True:
   line = f.readline()
   if line=='':
    break
   #if 'consistent' in experiment_folder and line_number==13:break
   arr = line.split(';')
   CODE_FILE = arr[1]
   ROOT_FOLDER = arr[2]
   folders.append(ROOT_FOLDER)
   FILE_NAME = arr[3]
   file_names.append(FILE_NAME)
   STRETCH_FACTOR = arr[4]
   stretch.append(STRETCH_FACTOR)
   if 'consistent' in experiment_folder:
     level.append(int(arr[5]))
   line_number += 1
  f.close()
  for i in range(len(folders)):
   if 'consistent' not in experiment_folder:
     level.append(int(folders[i].split('/')[1].split('_')[2]))
   node.append(int(file_names[i].split('_')[1]))
  return folders, stretch, file_names, level, node

def parse_output_file(experiment_folder, out_dir, exact, composite, time):
  obj = []
  BU_exact_obj = []
  folders, stretch, file_names, level, node = parse_id_csv(experiment_folder)
  if 'consistent' not in experiment_folder:
    for i in range(len(folders)):
     if time:
      val = parse_time_data(experiment_folder + 'log_folder/' + 'output_'+str(i+1)+'.dat')
      if val!=-1:
        obj.append(val)
      else:
        print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
        obj.append(-1)
     else:
      f = open(folders[i]+'/print_log_'+file_names[i]+'_stretch_'+str(float(stretch[i]))+'.txt')
      #print(f.read())
      s = f.read()
      if 'Solution value  = ' in s:
        arr = s.split('Solution value  = ')
        val = float(arr[1].strip())
        obj.append(val)
      else:
        print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
        obj.append(-1)
      f.close()
  if exact:
   if not composite:
    for i in range(len(folders)):
     if time:
       val = parse_time_data(out_dir + 'output_'+str(i+1)+'.dat')
       if val!=-1:
         BU_exact_obj.append(val)
       else:
         if experiment_folder == 'experiment_2/':
           if 'TD' in out_dir:
             #if i+1==60:
             #  BU_exact_obj.append(25*3600-757)
             #elif i+1==59:
             #  BU_exact_obj.append(20*3600-377)
             #else:
             #  print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
             #  BU_exact_obj.append(-1)
             print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
             BU_exact_obj.append(22*3600*int(node[i])*int(level[i])*float(stretch[i])/80/3/4)
           if 'BU' in out_dir:
             #if i+1==60:
             #  BU_exact_obj.append(20*3600-334)
             #elif i+1==59:
             #  BU_exact_obj.append(15*3600-377)
             #else:
             #  print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
             #  BU_exact_obj.append(-1)
             print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
             BU_exact_obj.append(16*3600*int(node[i])*int(level[i])*float(stretch[i])/80/3/4)
           if 'CMP' in out_dir:
             print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
             BU_exact_obj.append(19.5*3600*int(node[i])*int(level[i])*float(stretch[i])/80/3/4)
         if experiment_folder == 'experiment_WS/':
           print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
           BU_exact_obj.append(-1)
     else:
       f = open(out_dir + 'output_'+str(i+1)+'.dat')
       #print(f.read())
       s = f.read()
       if 'value:' in s:
         arr = s.split('value:')
         t = arr[1].strip()
         val = float(t[:len(t)-3])
         BU_exact_obj.append(val)
       else:
         print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
         BU_exact_obj.append(-1)
       f.close()
   else:
    for i in range(len(folders)):
     val = composite_value(folders[i]+'/'+file_names[i]+'.txt', out_dir + 'output_'+str(i+1)+'.dat', multiplicative_check, float(stretch[i]))
     if val!=-1:
       BU_exact_obj.append(val)
     else:
       print('ID:',i+1,' , time limit exceeded, folder:', folders[i], ', file:', file_names[i])
       BU_exact_obj.append(-1)
  else:
   if time:
     if experiment_folder == 'experiment_1/':
       if 'bottom_up' in out_dir:
         BU_exact_obj = parse_approx_time_data('bot_up_approx_1.py')
       elif 'top_down' in out_dir:
         BU_exact_obj = parse_approx_time_data('top_down_approx_1.py')
     elif experiment_folder == 'experiment_WS/':
       if 'bottom_up' in out_dir:
         BU_exact_obj = parse_approx_time_data('bot_up_approx_WS.py')
       elif 'top_down' in out_dir:
         BU_exact_obj = parse_approx_time_data('top_down_approx_WS.py')
   else:
     #for i in range(len(folders)):
      f = open(out_dir, 'r')
      line = f.readline()
      line = f.readline()
      line_number = 1
      while line!='':
       if 'consistent' in experiment_folder and line_number==10:break
       arr = line.split(';')
       BU_exact_obj.append(float(arr[2]))
       line = f.readline()
       line_number += 1
  return node, level, obj, BU_exact_obj, stretch

def get_density(experiment_folder):
  folders, stretch, file_names, level, node = parse_id_csv(experiment_folder)
  densities = []
  for i in range(len(folders)):
    f = open(folders[i]+'/'+file_names[i]+'.txt')
    m = int(f.readline().strip())
    n = node[i]
    densities.append(2*m/(n*(n-1)))
    f.close()
  return densities

def parse_output(file_name):
  eps = .001
  edge_lists = []
  f = open(file_name)
  s = str(f.read())
  if s=='':return -1
  level_txt = s.split('Solution value  =')
  #for i in range(len(level_txt)):
  #  print(level_txt[i][:500])
  for i in range(1,len(level_txt)):
    #print('level', len(level_txt)-i)
    edge_list = []
    s = level_txt[i]
    lines = s.split('\\n')
    for line in lines:
      if 'Column' in line:
        t = line.split(':')
        name = t[0].split()[1].strip()
        value = t[1].split('=')[1].strip()
        if(name.count('_')==2):
          #print(name, value)
          #if abs(float(value))<eps:
          #  print(name, 0)
          if abs(float(value)-1)<eps:
            #print(name, 1)
            t = name.split('_')
            edge_list.append([int(t[1]), int(t[2])])
          #elif abs(float(value)-2)<eps:
          #  print(name, 2)
          #elif abs(float(value)-3)<eps:
          #  print(name, 3)
    edge_lists.append(edge_list)
  f.close()
  return edge_lists

def graph_from_edges(G, edges):
  G2 = nx.Graph()
  for e in edges:
    G2.add_edge(e[0], e[1], weight=G.get_edge_data(e[0], e[1])['weight'])
  return G2

def edge_weight_sum(G):
  s =0
  for e in G.edges():
    s = s + G.get_edge_data(e[0], e[1])['weight']
  return s

def graph_union(G1, G2):
  G = nx.Graph()
  for e in G1.edges():
    G.add_edge(e[0], e[1], weight=G1.get_edge_data(e[0], e[1])['weight'])
  for e in G2.edges():
    G.add_edge(e[0], e[1], weight=G2.get_edge_data(e[0], e[1])['weight'])
  return G

def multiplicative_check(subgraph_distance, actual_distance, multiplicative_stretch):
        if subgraph_distance <= multiplicative_stretch*actual_distance:
                return True
        return False

def all_pairs_from_subset(s):
        all_pairs = []
        for i in range(len(s)):
                for j in range(i+1, len(s)):
                        p = []
                        p.append(s[i])
                        p.append(s[j])
                        all_pairs.append(p)
        return all_pairs

def verify_spanner_with_checker(G_S, G, all_pairs, check_stretch, param):
        for i in range(len(all_pairs)):
                if not (all_pairs[i][0] in G_S.nodes() and all_pairs[i][1] in G_S.nodes()):
                        return False
                if not nx.has_path(G_S, all_pairs[i][0], all_pairs[i][1]):
                        return False
                sp = nx.shortest_path_length(G, all_pairs[i][0], all_pairs[i][1], 'weight')
                #if not check_stretch(nx.dijkstra_path_length(G_S, all_pairs[i][0], all_pairs[i][1]), sp, param):
                if not check_stretch(nx.shortest_path_length(G_S, all_pairs[i][0], all_pairs[i][1], 'weight'), sp, param):
                        return False
        return True

def prune(G, G_main, subset, checker, param):
  G_S = nx.Graph()
  G_S.add_weighted_edges_from(G.edges(data='weight'))
  for e in G.edges():
    G_S.remove_edge(e[0], e[1])
    if not verify_spanner_with_checker(G_S, G_main, all_pairs_from_subset(subset), checker, param):
      G_S.add_edge(e[0], e[1], weight=G.get_edge_data(e[0], e[1])['weight'])
    #else:
    #  print('Pruned:', e[0], e[1])
  return G_S

def composite_value(graph_file, output_file, checker, param):
  global my_inf
  obj_val = my_inf
  edge_lists = parse_output(output_file)
  if edge_lists==-1:return -1
  G, subset_arr = build_networkx_graph(graph_file)
  if len(edge_lists)==3:
    # s3 + (s3Us2) + (s3Us2Us1)
    # s2 pruned + s2 + (s2Us1)
    # s3 + (s2U(s1 pruned)) + (s3Us1)
    # s1 pruned respect to t3 + s1 pruned respect to t2 + s1
    G3 = graph_from_edges(G, edge_lists[0])
    G2 = graph_from_edges(G, edge_lists[1])
    G1 = graph_from_edges(G, edge_lists[2])
    #case 1
    val = edge_weight_sum(G3)
    Gt = graph_union(G3, G2)
    val = val + edge_weight_sum(Gt)
    val = val + edge_weight_sum(graph_union(Gt, G1))
    if obj_val>val:obj_val=val
    #case 2
    G2_pruned = prune(G2, G, subset_arr[0], checker, param)
    val = edge_weight_sum(G2_pruned)
    val = val + edge_weight_sum(G2)
    val = val + edge_weight_sum(graph_union(G2, G1))
    if obj_val>val:obj_val=val
    #case 3
    val = edge_weight_sum(G3)
    val = val + edge_weight_sum(graph_union(G2, prune(G1, G, subset_arr[1], checker, param)))
    val = val + edge_weight_sum(graph_union(G3, G1))
    if obj_val>val:obj_val=val
    #case 4
    val = edge_weight_sum(prune(G1, G, subset_arr[0], checker, param))
    val = val + edge_weight_sum(prune(G1, G, subset_arr[1], checker, param))
    val = val + edge_weight_sum(G1)
    if obj_val>val:obj_val=val
  elif len(edge_lists)==2:
    # s2 + (s2Us1)
    # (s2U(s1 pruned)) + s1
    # s1 pruned respect to t2 + s1
    G2 = graph_from_edges(G, edge_lists[0])
    G1 = graph_from_edges(G, edge_lists[1])
    #case 1
    val = edge_weight_sum(G2)
    Gt = graph_union(G2, G1)
    val = val + edge_weight_sum(Gt)
    if obj_val>val:obj_val=val
    #case 2
    val = edge_weight_sum(graph_union(G2, prune(G1, G, subset_arr[0], checker, param)))
    val = val + edge_weight_sum(G1)
    if obj_val>val:obj_val=val
    #case 3
    val = edge_weight_sum(prune(G2, G, subset_arr[0], checker, param))
    val = val + edge_weight_sum(G1)
    if obj_val>val:obj_val=val
  else:
    G1 = graph_from_edges(G, edge_lists[0])
    obj_val = edge_weight_sum(G1)
  return obj_val

def parse_time_data(file_name):
  f = open(file_name)
  s = str(f.read())
  if s=='':return -1
  s = s.split('Total (root+branch&cut) =')
  total_time = 0
  for i in range(1, len(s)):
    total_time += float(s[i].split('sec.')[0].strip())
  f.close()
  return total_time

def parse_approx_time_data(file_name):
  time_arr = []
  f = open(file_name)
  while True:
    s = f.readline()
    if s=='':break
    if 'Time to compute ' in s:
      time_arr.append(float(s.split(':')[1].strip()))
  f.close()
  return time_arr

log_folder_BU_exact = ''
log_folder_TD_exact = ''
log_folder_CMP_exact = ''
y_min = .94
y_max = 1.27
experiment_folder = 'experiment_2/'
#experiment_folder = 'experiment_WS/'
#experiment_folder = 'experiment_consistent_ER/'
#experiment_folder = 'experiment_consistent_ER_4/'
if experiment_folder == 'experiment_2/':
  log_folder_BU_exact = 'log_folder_BU_exact'
  log_folder_TD_exact = 'log_folder_TD_exact'
  log_folder_CMP_exact = 'log_folder_CMP_exact'
elif experiment_folder == 'experiment_WS/':
  log_folder_BU_exact = 'log_folder_BU_exact'
  log_folder_TD_exact = 'log_folder_TD_exact'
  y_max = 1.5
elif experiment_folder == 'experiment_consistent_ER_4/':
  log_folder_BU_exact = 'log_folder_BU_consistent'
  log_folder_TD_exact = 'log_folder_TD_consistent'

def convert_approx_to_exact(obj_file, time_file, log_folder):
  time_arr = parse_approx_time_data('experiment_consistent_ER_4/' + time_file)
  f = open('experiment_consistent_ER_4/' + obj_file, 'r')
  line = f.readline()
  line = f.readline()
  obj_arr = []
  while line!='':
    arr = line.split(';')
    if arr[2]=='':break
    obj_arr.append(float(arr[2]))
    line = f.readline()
  f.close()
  for i in range(11):
  #for i in range(10):
    f = open('experiment_consistent_ER_4/' + log_folder + 'output_' + str(i+1) + '.dat', 'w')
    f.write('Total (root+branch&cut) =    ' + str(time_arr[i]) + ' sec. (16.85 ticks)\n')
    f.write('Objective value: ' + str(obj_arr[i]) + '\n')
    f.close()

#convert_approx_to_exact('top_down_output.txt', 'top_down_approx_consistent_ER.py', 'log_folder_TD_consistent/')
#convert_approx_to_exact('bottom_up_output.txt', 'bot_up_approx_consistent_ER.py', 'log_folder_BU_consistent/')

if experiment_folder == 'experiment_2/' or experiment_folder == 'experiment_WS/':
  #line_plot(experiment_folder, 'BU_oracle_NVR.png', experiment_folder + log_folder_BU_exact + '/', 'node', True, y_min, y_max)
  #line_plot(experiment_folder, 'TD_oracle_NVR.png', experiment_folder + 'log_folder_TD_exact/', 'node', True, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_oracle_NVR.png', 'node', True, y_min, y_max)
  ##line_plot_composite(experiment_folder, 'CMP_oracle_NVR.png', 'node', True, y_min, y_max)
  #box_plot(experiment_folder, 'Oracle_NVR_box.png', 'node', True, y_min, y_max)
  #box_plot_single(experiment_folder, 'Oracle_NVT_box.png', 'node', True, 'time')
  #box_plot_single(experiment_folder, 'NVD_box.png', 'node', True, 'density')
  #box_plot_time(experiment_folder, 'Oracle_heu_NVT_box.png', 'node', True)
  #line_plot(experiment_folder, 'BU_oracle_LVR.png', experiment_folder + log_folder_BU_exact + '/', 'level', True, y_min, y_max)
  #line_plot(experiment_folder, 'TD_oracle_LVR.png', experiment_folder + 'log_folder_TD_exact/', 'level', True, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_oracle_LVR.png', 'level', True, y_min, y_max)
  box_plot(experiment_folder, 'Oracle_LVR_box.png', 'level', True, y_min, y_max)
  #box_plot_single(experiment_folder, 'Oracle_LVT_box.png', 'level', True, 'time')
  #box_plot_single(experiment_folder, 'LVD_box.png', 'level', True, 'density')
  #box_plot_time(experiment_folder, 'Oracle_heu_LVT_box.png', 'level', True)
  #line_plot(experiment_folder, 'BU_oracle_SVR.png', experiment_folder + log_folder_BU_exact + '/', 'stretch', True, y_min, y_max)
  #line_plot(experiment_folder, 'TD_oracle_SVR.png', experiment_folder + 'log_folder_TD_exact/', 'stretch', True, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_oracle_SVR.png', 'stretch', True, y_min, y_max)
  #box_plot(experiment_folder, 'Oracle_SVR_box.png', 'stretch', True, y_min, y_max)
  #box_plot_single(experiment_folder, 'Oracle_SVT_box.png', 'stretch', True, 'time')
  #box_plot_single(experiment_folder, 'SVD_box.png', 'stretch', True, 'density')
  #box_plot_time(experiment_folder, 'Oracle_heu_SVT_box.png', 'stretch', True)

  #line_plot(experiment_folder, 'BU_approx_NVR.png', experiment_folder + 'bottom_up_output.txt', 'node', False, y_min, y_max)
  #line_plot(experiment_folder, 'TD_approx_NVR.png', experiment_folder + 'top_down_output.txt', 'node', False, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_approx_NVR.png', 'node', False, y_min, y_max)
  #box_plot(experiment_folder, 'Approx_NVR_box.png', 'node', False, y_min, y_max)
  ##box_plot_time(experiment_folder, 'approx_heu_NVT_box.png', 'node', False)
  #line_plot(experiment_folder, 'BU_approx_LVR.png', experiment_folder + 'bottom_up_output.txt', 'level', False, y_min, y_max)
  #line_plot(experiment_folder, 'TD_approx_LVR.png', experiment_folder + 'top_down_output.txt', 'level', False, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_approx_LVR.png', 'level', False, y_min, y_max)
  #box_plot(experiment_folder, 'Approx_LVR_box.png', 'level', False, y_min, y_max)
  ##box_plot_time(experiment_folder, 'approx_heu_LVT_box.png', 'level', False)
  #line_plot(experiment_folder, 'BU_approx_SVR.png', experiment_folder + 'bottom_up_output.txt', 'stretch', False, y_min, y_max)
  #line_plot(experiment_folder, 'TD_approx_SVR.png', experiment_folder + 'top_down_output.txt', 'stretch', False, y_min, y_max)
  #line_plot_min(experiment_folder, 'CMP_approx_SVR.png', 'stretch', False, y_min, y_max)
  #box_plot(experiment_folder, 'Approx_SVR_box.png', 'stretch', False, y_min, y_max)
  ##box_plot_time(experiment_folder, 'approx_heu_SVT_box.png', 'stretch', False)

#print(get_density(experiment_folder))

# for visualization
#edge_lists = parse_output('experiment_1/log_folder_TD_exact/output_41.dat')
#print(len(edge_lists[0]))
#print(len(edge_lists[1]))
#print(len(edge_lists[2]))
#print(edge_lists)

#arr = parse_approx_time_data('bot_up_approx_1.py')
#print(arr)
#print(len(arr))

if experiment_folder == 'experiment_consistent_ER_4/':
  #box_plot(experiment_folder, 'Approx_NVR_box.png', 'node', True, y_min, y_max)
  #box_plot(experiment_folder, 'Approx_LVR_box.png', 'level', True, y_min, y_max)
  #box_plot(experiment_folder, 'Approx_SVR_box.png', 'stretch', True, y_min, y_max)
  box_plot_time(experiment_folder, 'Approx_heu_NVT_box.png', 'node', True)
  box_plot_time(experiment_folder, 'Approx_heu_LVT_box.png', 'level', True)
  box_plot_time(experiment_folder, 'Approx_heu_SVT_box.png', 'stretch', True)




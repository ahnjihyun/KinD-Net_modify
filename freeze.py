import tensorflow as tf
from tensorflow.python.tools import freeze_graph

freeze_graph.freeze_graph(input_graph='/home/dkswlgus/KinD_backup/checkpoint/graph.pbtxt',
                          input_saver="",
                          input_binary=False,
                          input_checkpoint='/home/dkswlgus/KinD_backup/checkpoint/kind.ckpt',
                          output_node_names='Illumination_adjust_net/Sigmoid', #DecomNet/ Restoration_net/ Illumination_adjust_net
#'DecomNet/Sigmoid, DecomNet/Sigmoid_1'
                          restore_op_name="",
                          filename_tensor_name="",
                          output_graph='/home/dkswlgus/KinD_backup/checkpoint/3.pb',
                          clear_devices=False,
                          initializer_nodes="")

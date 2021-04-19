# -*- coding: utf-8 -*-
from rknn.api import RKNN

#create RKNN object
rknn = RKNN(verbose=True)

#Load model
print('--> Loading model')
ret = rknn.load_tensorflow(tf_pb='/home/dkswlgus/KinD_backup/checkpoint/3.pb',
	                     inputs=['input_low_i', 'input_low_i_ratio'],
	                     outputs=['Illumination_adjust_net/Sigmoid'],
	                     input_size_list=[[400, 600, 1], [400, 600, 1]]) #세로, 가로, 채널
if ret !=0:
	print('Load failed!')
	exit(ret)
print('done')

#----------------
#Build model
print('--> Building model')
ret = rknn.build(do_quantization=False)
if ret !=0:
	print('Build failed!')
	exit(ret)
print('done')

#----------------
#Export rknn model
print('--> Export RKNN model')
ret = rknn.export_rknn('./3.rknn') #다음과 같은 이름으로 저장
if ret != 0:
	print('Export failed!')
	exit(ret)
print('done')


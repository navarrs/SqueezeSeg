# Author: Bichen Wu (bichen@berkeley.edu) 08/25/2016

"""Model configuration for pascal dataset"""
import numpy as np
from config import base_model_config

def kitti_squeezeSeg_config():
  """Specify the parameters to tune below."""
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                    [ 0.12,  0.56,  0.37],
                                    [ 0.66,  0.55,  0.71],
                                    [ 0.58,  0.72,  0.88]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 64

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  mc.RCRF_ITER          = 3
  mc.BILATERAL_THETA_A  = np.array([.9, .9, .6, .6])
  mc.BILATERAL_THETA_R  = np.array([.015, .015, .01, .01])
  mc.BI_FILTER_COEF     = 0.1
  mc.ANG_THETA_A        = np.array([.9, .9, .6, .6])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  mc.INPUT_MEAN         = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_STD          = np.array([[[11.47, 6.91, 0.86, 0.16, 12.32]]])
  
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc

def kitti_squeezeSeg32_config():
  """Specify the parameters to tune below."""
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                    [ 0.12,  0.56,  0.37],
                                    [ 0.66,  0.55,  0.71],
                                    [ 0.58,  0.72,  0.88]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 32

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  mc.RCRF_ITER          = 3
  mc.BILATERAL_THETA_A  = np.array([.9, .9, .6, .6])
  mc.BILATERAL_THETA_R  = np.array([.015, .015, .01, .01])
  mc.BI_FILTER_COEF     = 0.1
  mc.ANG_THETA_A        = np.array([.9, .9, .6, .6])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  mc.INPUT_MEAN         = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_STD          = np.array([[[11.47, 6.91, 0.86, 0.16, 12.32]]])
  
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc

def kitti_squeezeSeg16_config():
  """Specify the parameters to tune below."""
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                    [ 0.12,  0.56,  0.37],
                                    [ 0.66,  0.55,  0.71],
                                    [ 0.58,  0.72,  0.88]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 16

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  mc.RCRF_ITER          = 3
  mc.BILATERAL_THETA_A  = np.array([.9, .9, .6, .6])
  mc.BILATERAL_THETA_R  = np.array([.015, .015, .01, .01])
  mc.BI_FILTER_COEF     = 0.1
  mc.ANG_THETA_A        = np.array([.9, .9, .6, .6])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  mc.INPUT_MEAN         = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_STD          = np.array([[[11.47, 6.91, 0.86, 0.16, 12.32]]])
  
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc

def kitti_squeezeSeg_config_ext():
  """ Parameters to tune after adding one class """
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist', 'ground']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0, 1/10.0])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                    [ 0.12,  0.56,  0.37],
                                    [ 0.66,  0.55,  0.71],
                                    [ 0.58,  0.72,  0.88], 
                                    [ 0.25,  0.51,  0.76]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 64

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  mc.RCRF_ITER          = 3

  # Not sure if I need to change this 
  mc.BI_FILTER_COEF     = 0.1
  mc.BILATERAL_THETA_A  = np.array([.9,   .9,   .6,  .6,  .9])
  mc.BILATERAL_THETA_R  = np.array([.015, .015, .01, .01, .015])
  mc.ANG_THETA_A        = np.array([.9,   .9,   .6,  .6,  .9])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  mc.INPUT_MEAN         = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_STD          = np.array([[[11.47, 6.91,  0.86, 0.16, 12.32]]])
  
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc

def kitti_squeezeSeg32_config_ext():
  """ Parameters to tune after adding one class """
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist', 'ground']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  #mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0, 1/10.0])
  mc.CLS_LOSS_WEIGHT    = np.array([0.00399712, 1.0,  0.68579656, 0.68579656, 0.01329])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                    [ 0.12,  0.56,  0.37],
                                    [ 0.66,  0.55,  0.71],
                                    [ 0.58,  0.72,  0.88], 
                                    [ 0.25,  0.51,  0.76]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 32

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  #mc.RCRF_ITER         = 3
  mc.RCRF_ITER          = 5

  # Not sure if I need to change this 
  mc.BI_FILTER_COEF     = 0.1
  mc.BILATERAL_THETA_A  = np.array([0.9,   0.9,  0.6, 0.6, 0.9])
  mc.BILATERAL_THETA_R  = np.array([0.015, 0.015, 0.01, 0.01, 0.015])
  mc.ANG_THETA_A        = np.array([0.9,   0.9,   0.6, 0.6,  0.9])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  # mc.INPUT_MEAN  = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_MEAN    = np.array([[[7.11174452147, 0.0943776729418, -0.500243253951, 0.110507476635,7.70754909688]]])
  # mc.INPUT_STD   = np.array([[[11.47, 6.91,  0.86, 0.16, 12.32]]])
  mc.INPUT_STD          = np.array([[[10.9252722964, 4.8862697957, 0.775360202555, 0.166859600962,11.6589714541]]])
  
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc

def kitti_squeezeSeg16_config_ext():
  """ Parameters to tune after adding one class """
  mc                    = base_model_config('KITTI')
  mc.CLASSES            = ['unknown', 'car', 'pedestrian', 'cyclist', 'ground']
  mc.NUM_CLASS          = len(mc.CLASSES)
  mc.CLS_2_ID           = dict(zip(mc.CLASSES, range(len(mc.CLASSES))))
  mc.CLS_LOSS_WEIGHT    = np.array([1/15.0, 1.0,  10.0, 10.0, 1/15.0])
  mc.CLS_COLOR_MAP      = np.array([[ 0.00,  0.00,  0.00],
                                      [ 0.12,  0.56,  0.37],
                                      [ 0.66,  0.55,  0.71],
                                      [ 0.58,  0.72,  0.88], 
                                      [ 0.25,  0.51,  0.76]])

  mc.BATCH_SIZE         = 32
  mc.AZIMUTH_LEVEL      = 512
  mc.ZENITH_LEVEL       = 16

  mc.LCN_HEIGHT         = 3
  mc.LCN_WIDTH          = 5
  mc.RCRF_ITER          = 3

  # Not sure if I need to change this 
  mc.BI_FILTER_COEF     = 0.1
  mc.BILATERAL_THETA_A  = np.array([.9,   .9,   .6,  .6,  .9])
  mc.BILATERAL_THETA_R  = np.array([.015, .015, .01, .01, .015])
  mc.ANG_THETA_A        = np.array([.9,   .9,   .6,  .6,  .9])
  mc.ANG_FILTER_COEF    = 0.02

  mc.CLS_LOSS_COEF      = 15.0
  mc.WEIGHT_DECAY       = 0.0001
  mc.LEARNING_RATE      = 0.01
  mc.DECAY_STEPS        = 10000
  mc.MAX_GRAD_NORM      = 1.0
  mc.MOMENTUM           = 0.9
  mc.LR_DECAY_FACTOR    = 0.5

  mc.DATA_AUGMENTATION  = True
  mc.RANDOM_FLIPPING    = True

  # x, y, z, intensity, distance
  mc.INPUT_MEAN         = np.array([[[10.88, 0.23, -1.04, 0.21, 12.12]]])
  mc.INPUT_STD          = np.array([[[11.47, 6.91,  0.86, 0.16, 12.32]]])
      
  mc.num_of_input_channels=5
  mc.use_focal_loss=False
  mc.EVAL_ON_ORG=False

  return mc  

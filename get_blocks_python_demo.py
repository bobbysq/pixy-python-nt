from __future__ import print_function
import pixy
from networktables import NetworkTables
from ctypes import *
from pixy import *

NetworkTables.initialize(server='roborio-4646-frc.local')

# Pixy2 Python SWIG get blocks example #

print("Pixy2 Python SWIG Example -- Get Blocks")

pixy.init()
pixy.change_prog("color_connected_components")


class Blocks (Structure):
    _fields_ = [("m_signature", c_uint),
                ("m_x", c_uint),
                ("m_y", c_uint),
                ("m_width", c_uint),
                ("m_height", c_uint),
                ("m_angle", c_uint),
                ("m_index", c_uint),
                ("m_age", c_uint)]


blocks = BlockArray(100)
frame = 0
pixyTable = NetworkTables.getTable('Pixy')

while 1:
    count = pixy.ccc_get_blocks(100, blocks)

    if count > 0:
        print('frame %3d:' % (frame))
        frame = frame + 1
        for index in range(0, count):
            #print('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height))
            pixyTable.putNumber('sig', blocks[index].m_signature)
            pixyTable.putNumber('x', blocks[index].m_x)
            pixyTable.putNumber('y', blocks[index].m_y)
            pixyTable.putNumber('width', blocks[index].m_width)
            pixyTable.putNumber('height', blocks[index].m_height)
            pixyTable.putNumber('angle', blocks[index].m_angle)
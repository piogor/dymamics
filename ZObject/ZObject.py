# -*- coding: utf-8 -*-
#
# This file is part of the ZObject project
#
# 
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" Dynamics

"""

__all__ = ["ZObject", "main"]

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import class_property, device_property
from PyTango import AttrQuality, AttrWriteType, DispLevel, DevState
# Additional import
# PROTECTED REGION ID(ZObject.additionnal_import) ENABLED START #
import numpy as np
# PROTECTED REGION END #    //  ZObject.additionnal_import


class ZObject(Device):
    """
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(ZObject.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  ZObject.class_variable
    # ----------------
    # Class Properties
    # ----------------

    # -----------------
    # Device Properties
    # -----------------

    # ----------
    # Attributes
    # ----------

    Output = attribute(
        dtype='double',
    )

    Input = attribute(
        dtype='double',
        access=AttrWriteType.WRITE,
    )

    InternalState = attribute(
        dtype=('double',),
        access=AttrWriteType.READ_WRITE,
        max_dim_x=10,
    )

    TransformationMatrix = attribute(
        dtype=(('double',),),
        access=AttrWriteType.WRITE,
        max_dim_x=10, max_dim_y=10,
        display_level=DispLevel.EXPERT,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(ZObject.init_device) ENABLED START #
        self._internal_state = np.array([1.0, 5.0])
        self._matrix = np.array([[0.6, 0.3], [0.3, 0.6]])
        self.set_state(PyTango.DevState.ON)
        # PROTECTED REGION END #    //  ZObject.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(ZObject.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  ZObject.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(ZObject.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  ZObject.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Output(self):
        # PROTECTED REGION ID(ZObject.Output_read) ENABLED START #
        return self._internal_state[0]

        # PROTECTED REGION END #    //  ZObject.Output_read

    def write_Input(self, value):
        # PROTECTED REGION ID(ZObject.Input_write) ENABLED START #
        self._internal_state[len(self._internal_state)-1] = value
        # PROTECTED REGION END #    //  ZObject.Input_write

    def read_InternalState(self):
        # PROTECTED REGION ID(ZObject.InternalState_read) ENABLED START #
        return self._internal_state

        # PROTECTED REGION END #    //  ZObject.InternalState_read

    def write_InternalState(self, value):
        # PROTECTED REGION ID(ZObject.InternalState_write) ENABLED START #
        self._internal_state =  value
        #pass
        # PROTECTED REGION END #    //  ZObject.InternalState_write

    def write_TransformationMatrix(self, value):
        # PROTECTED REGION ID(ZObject.TransformationMatrix_write) ENABLED START #
        self._matrix = np.array(value)

        # PROTECTED REGION END #    //  ZObject.TransformationMatrix_write

    # --------
    # Commands
    # --------

    @command
    @DebugIt()
    def Compute(self):
        # PROTECTED REGION ID(ZObject.Compute) ENABLED START #
        self._internal_state = np.dot(self._matrix,self._internal_state)

        # PROTECTED REGION END #    //  ZObject.Compute

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    from PyTango.server import run
    return run((ZObject,), args=args, **kwargs)

if __name__ == '__main__':
    main()

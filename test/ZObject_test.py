#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the ZObject project
#
# 
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.
"""Contain the tests for the Dynamics."""

# Path
import sys
import os
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, os.path.abspath(path))

# Imports
from time import sleep
from mock import MagicMock
from PyTango import DevFailed, DevState
from devicetest import DeviceTestCase, main
from ZObject import ZObject

# Note:
#
# Since the device uses an inner thread, it is necessary to
# wait during the tests in order the let the device update itself.
# Hence, the sleep calls have to be secured enough not to produce
# any inconsistent behavior. However, the unittests need to run fast.
# Here, we use a factor 3 between the read period and the sleep calls.
#
# Look at devicetest examples for more advanced testing


# Device test case
class ZObjectDeviceTestCase(DeviceTestCase):
    """Test case for packet generation."""
    # PROTECTED REGION ID(ZObject.test_additionnal_import) ENABLED START #
    # PROTECTED REGION END #    //  ZObject.test_additionnal_import
    device = ZObject
    properties = {
                  }
    empty = None  # Should be []

    @classmethod
    def mocking(cls):
        """Mock external libraries."""
        # Example : Mock numpy
        # cls.numpy = ZObject.numpy = MagicMock()
        # PROTECTED REGION ID(ZObject.test_mocking) ENABLED START #
        # PROTECTED REGION END #    //  ZObject.test_mocking

    def test_properties(self):
        # test the properties
        # PROTECTED REGION ID(ZObject.test_properties) ENABLED START #
        # PROTECTED REGION END #    //  ZObject.test_properties
        pass

    def test_State(self):
        """Test for State"""
        # PROTECTED REGION ID(ZObject.test_State) ENABLED START #
        self.device.State()
        # PROTECTED REGION END #    //  ZObject.test_State

    def test_Status(self):
        """Test for Status"""
        # PROTECTED REGION ID(ZObject.test_Status) ENABLED START #
        self.device.Status()
        # PROTECTED REGION END #    //  ZObject.test_Status

    def test_Compute(self):
        """Test for Compute"""
        # PROTECTED REGION ID(ZObject.test_Compute) ENABLED START #
        self.device.Compute()
        # PROTECTED REGION END #    //  ZObject.test_Compute

    def test_Output(self):
        """Test for Output"""
        # PROTECTED REGION ID(ZObject.test_Output) ENABLED START #
        self.device.Output
        # PROTECTED REGION END #    //  ZObject.test_Output

    def test_Input(self):
        """Test for Input"""
        # PROTECTED REGION ID(ZObject.test_Input) ENABLED START #
        self.device.Input
        # PROTECTED REGION END #    //  ZObject.test_Input

    def test_InternalState(self):
        """Test for InternalState"""
        # PROTECTED REGION ID(ZObject.test_InternalState) ENABLED START #
        self.device.InternalState
        # PROTECTED REGION END #    //  ZObject.test_InternalState

    def test_TransformationMatrix(self):
        """Test for TransformationMatrix"""
        # PROTECTED REGION ID(ZObject.test_TransformationMatrix) ENABLED START #
        self.device.TransformationMatrix
        # PROTECTED REGION END #    //  ZObject.test_TransformationMatrix


# Main execution
if __name__ == "__main__":
    main()

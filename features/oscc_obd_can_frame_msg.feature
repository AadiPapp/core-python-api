# WARNING: Auto-generated file. Any changes are subject to being overwritten
# by setup.py build script.

Feature: oscc_obd_can_frame_msg support
	Scenario: Excercise PolySync message conversion between Python API and C API
		Given I have a Py_oscc_obd_can_frame_msg object
		When I convert it to its C API equivalent a oscc_obd_can_frame_msg
		And I convert the oscc_obd_can_frame_msg back to a Py_oscc_obd_can_frame_msg
		Then the oscc_obd_can_frame_msg values are equivalent to each Py_oscc_obd_can_frame_msg value

	Scenario: Excercise Python API publish type check
		Given a oscc_obd_can_frame_msg.publish function exists
		When I try to publish something that is not of type Py_oscc_obd_can_frame_msg
		Then a TypeError indicates the type was not Py_oscc_obd_can_frame_msg

	Scenario: Excercise Py_oscc_obd_can_frame_msg publish and subscribe
		Given I have a licensed PsNode for publishing Py_oscc_obd_can_frame_msg
		And I have a Py_oscc_obd_can_frame_msg
		And I have a handler for Py_oscc_obd_can_frame_msg subscription
		When I publish my Py_oscc_obd_can_frame_msg
		Then I receive the corresponding Py_oscc_obd_can_frame_msg in my handler

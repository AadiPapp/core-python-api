# WARNING: Auto-generated file. Any changes are subject to being overwritten
# by setup.py build script.

#!/usr/bin/python
import time
from behave import given
from behave import when
from behave import then
from hamcrest import assert_that, equal_to

try:
    import polysync.node as ps_node
    from polysync.data_model.types import Py_sbp_msg_navigation_velocity_ecef
    from polysync.data_model._internal.compare import sbp_msg_navigation_velocity_ecef_type_convert_testable, Py_sbp_msg_navigation_velocity_ecef_initialize_random
    from polysync.data_model.message_support.sbp_msg_navigation_velocity_ecef import publish, subscribe
except ImportError:
    raise ImportError(
        'Py_sbp_msg_navigation_velocity_ecef module dependencies \
        missing for tests, is the project built?')


@given('I have a Py_sbp_msg_navigation_velocity_ecef object')
def step_impl(context):
    pass

@when('I convert it to its C API equivalent a sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    pass

@when('I convert the sbp_msg_navigation_velocity_ecef back to a Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    pass

@then('the sbp_msg_navigation_velocity_ecef values are equivalent to each Py_sbp_msg_navigation_velocity_ecef value')
def step_impl(context):
    msg = Py_sbp_msg_navigation_velocity_ecef_initialize_random()
    result = sbp_msg_navigation_velocity_ecef_type_convert_testable(msg)
    assert not result, result

@given('a sbp_msg_navigation_velocity_ecef.publish function exists')
def step_impl(context):
    assert callable(publish)

@when('I try to publish something that is not of type Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    bad_obj = "not the right type of object!"
    context.exception = None

    try:
        publish(bad_obj)
    except Exception as e:
        context.exception = e

@then('a {exeption} indicates the type was not Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context, exeption):
    assert isinstance(context.exception, eval(exeption)), \
    "Invalid exception %s - expected %s" \
    % (type(context.exception).__name__, exeption)

GLOBAL_TIMESTAMP = None
GLOBAL_GUID = None

def Py_sbp_msg_navigation_velocity_ecef_handler(msg):
    if msg.header.src_guid == GLOBAL_GUID:
        global GLOBAL_TIMESTAMP
        GLOBAL_TIMESTAMP = msg.header.timestamp

@given(u'I have a licensed PsNode for publishing Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    assert context.node_ref
    global GLOBAL_GUID
    GLOBAL_GUID = context.my_guid

@given(u'I have a Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    context.msg = Py_sbp_msg_navigation_velocity_ecef()
    context.msg.header.timestamp = 0xFFFF

@given(u'I have a handler for Py_sbp_msg_navigation_velocity_ecef subscription')
def step_impl(context):
    assert Py_sbp_msg_navigation_velocity_ecef_handler
    subscribe(handler=Py_sbp_msg_navigation_velocity_ecef_handler)

@when(u'I publish my Py_sbp_msg_navigation_velocity_ecef')
def step_impl(context):
    publish(context.msg)

@then(u'I receive the corresponding Py_sbp_msg_navigation_velocity_ecef in my handler')
def step_impl(context):
    global GLOBAL_TIMESTAMP
    while not GLOBAL_TIMESTAMP:
        time.sleep(1)
    assert_that(context.msg.header.timestamp, equal_to(GLOBAL_TIMESTAMP))


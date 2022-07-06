import maya.cmds as cmds
import random

global maxRange
global minRange


# closure with mini environment
def function_wrapper(fn, attr_change):
    def wrapped(_):
        fn(attr_change)

    return wrapped


def randomize_all(attr_change):
    # Randomizes Translations of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(minRange, maxRange)
            cmds.setAttr('{}.{}{}'.format(i, attr_change, a), randnum)


def randomize_last(attr_change):
    # Randomizes Translation of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True))) - 1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(minRange, maxRange)
        cmds.setAttr('{}.{}{}'.format(sel, attr_change, a), randnum)


def randomization_ui():
    global maxRange
    global minRange

    def value_slider(ui_label):
        slider = cmds.intSliderGrp(min=1, max=60, value=3, step=1, field=True)

        def query():
            return cmds.intSlider(slider, q=True, v=True)

        return slider, query

    window = cmds.window(title="My UI Test", widthHeight=(500, 250), sizeable=True)

    master_layout = cmds.columnLayout(adjustableColumn=True)
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)

    s1, q1 = value_slider('slider1')
    s2, q2 = value_slider('slider2')

    minRange = q1()
    maxRange = q2()

    cmds.textField(editable=False, text='Minimum Range')
    min_slider = cmds.intSliderGrp(min=1, max=180, value=3, step=1, field=True)

    cmds.textField(editable=False, text='Maximum Range')
    max_slider = cmds.intSliderGrp(min=1, max=60, value=3, step=1, field=True)

    cmds.setParent(master_layout)

    cmds.button(label='Randomize Scale', command=function_wrapper(randomize_last, 'scale'))
    cmds.button(label='Randomize Scale for All Selected', command=function_wrapper(randomize_all, 'scale'))

    cmds.button(label='Randomize Rotation', command=function_wrapper(randomize_last, 'rotate'))
    cmds.button(label='Randomize Rotation for All Selected', command=function_wrapper(randomize_all, 'rotate'))

    cmds.button(label='Randomize Translation', command=function_wrapper(randomize_last, 'translate'))
    cmds.button(label='Randomize Translation for All Selected', command=function_wrapper(randomize_all, 'translate'))

    cmds.showWindow(window)


randomization_ui()
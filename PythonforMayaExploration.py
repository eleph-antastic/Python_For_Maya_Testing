import maya.cmds as cmds
import random

"""   
## A function I am exploring to begin the process of copy/pasting keyframes from one selected object to another          
def transfer_animation(obj_one, obj_two, cut=False):
    if cut:
        cmds.cutKey(obj_one, animation='objects', option='keys')
    else:
        cmds.copyKey(obj_one, animation='objects', option='keys')
    cmds.pasteKey(obj_two, animation='objects', option='replaceCompletely')
"""
#closure with mini environment
def function_wrapper(fn, *args, **kwargs):
    def wrapped(_):
        fn(*args, **kwargs)
        
    return wrapped
    

def randomize_translate_all(min_range, max_range):
    #Randomizes Translations of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(min_range, max_range)
            cmds.setAttr('{}.translate{}'.format(i, a), randnum)

                  
def randomize_translate(min_range, max_range):
    #Randomizes Translation of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(min_range, max_range)
        cmds.setAttr('{}.translate{}'.format(sel, a), randnum)

    
def randomize_scale_all(min_range, max_range):
    #Randomizes Scale of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(min_range, max_range)
            cmds.setAttr('{}.scale{}'.format(i, a), randnum)

                    
def randomize_scale(min_range, max_range):
    #Randomizes Scale of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(min_range, max_range)
        cmds.setAttr('{}.scale{}'.format(sel, a), randnum)

                
def randomize_rotation_all(min_range, max_range):
    #Randomizes Rotation of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(min_range, max_range)
            cmds.setAttr('{}.rotate{}'.format(i, a), randnum)


def randomize_rotation(min_range, max_range):
    #Randomizes Rotation of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(min_range, max_range)
        cmds.setAttr('{}.rotate{}'.format(sel, a), randnum)               


def randomization_ui():
    window = cmds.window(title = "My UI Test", widthHeight = (500,250), sizeable = True)
    
    master_layout = cmds.columnLayout(adjustableColumn=True)
    
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    min_range_textfield = cmds.textField(editable=False, text='Minimum Range')
    min_range = cmds.textField(editable=True, text='1')
        
    max_range_textfield = cmds.textField(editable=False, text='Max Range')
    max_range = cmds.textField(editable=True, text='10')
        
    cmds.setParent(master_layout)
    
    cmds.button(label = 'Randomize Scale', command=function_wrapper(randomize_scale, min_range, max_range))
    cmds.button(label = 'Randomize Scale for All Selected', command=function_wrapper(randomize_scale_all, min_range, max_range))
    
    cmds.button(label = 'Randomize Rotation', command=function_wrapper(randomize_rotation, min_range, max_range))
    cmds.button(label = 'Randomize Rotation for All Selected', command=function_wrapper(randomize_rotation_all, min_range, max_range))
    
    cmds.button(label = 'Randomize Translation', command=function_wrapper(randomize_translate, min_range, max_range))
    cmds.button(label = 'Randomize Translation for All Selected', command=function_wrapper(randomize_translate_all, min_range, max_range))
    
    
    cmds.showWindow(window)
    
randomization_ui()                    

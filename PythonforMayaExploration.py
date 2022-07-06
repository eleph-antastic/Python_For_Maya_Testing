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

global maxRange
global minRange
    
#closure with mini environment
def function_wrapper(fn):
    def wrapped(_):
        fn()
        
    return wrapped
    

def randomize_translate_all():
    #Randomizes Translations of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(minRange, maxRange)
            cmds.setAttr('{}.translate{}'.format(i, a), randnum)

                  
def randomize_translate():
    #Randomizes Translation of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(minRange, maxRange)
        cmds.setAttr('{}.translate{}'.format(sel, a), randnum)

    
def randomize_scale_all():
    #Randomizes Scale of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(minRange, maxRange)
            cmds.setAttr('{}.scale{}'.format(i, a), randnum)

                    
def randomize_scale():
    #Randomizes Scale of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(minRange, maxRange)
        cmds.setAttr('{}.scale{}'.format(sel, a), randnum)

                
def randomize_rotation_all():
    #Randomizes Rotation of All Selected objects
    for i in cmds.ls(sl=True):
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(minRange, maxRange)
            cmds.setAttr('{}.rotate{}'.format(i, a), randnum)


def randomize_rotation():
    #Randomizes Rotation of Last Object Selected
    sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
    for a in ['X', 'Y', 'Z']:
        randnum = random.uniform(minRange, maxRange)
        cmds.setAttr('{}.rotate{}'.format(sel, a), randnum)               


def randomization_ui():
    global maxRange
    global minRange
    
    def value_slider(ui_label):
        slider = cmds.intSliderGrp(min = 1, max = 60, value = 3, step = 1, field = True)
        
        def query():
            return cmds.intSlider(slider, q=True, v=True)
        
        return slider, query
        
    window = cmds.window(title = "My UI Test", widthHeight = (500,250), sizeable = True)
    
    master_layout = cmds.columnLayout(adjustableColumn=True)
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    
    s1, q1 = value_slider('slider1')
    s2, q2 = value_slider('slider2')
    
    maxRange = q1()
    minRange = q2()    
    
    cmds.textField(editable=False, text='Maximum Range')
    max_slider = cmds.intSliderGrp(min = 1, max = 60, value = 3, step = 1, field = True)
        
    cmds.textField(editable=False, text='Minimum Range')
    min_slider = cmds.intSliderGrp(min = 1, max = 60, value = 3, step = 1, field = True)  
    
        
    cmds.setParent(master_layout)
    
    cmds.button(label = 'Randomize Scale', command=function_wrapper(randomize_scale))
    cmds.button(label = 'Randomize Scale for All Selected', command=function_wrapper(randomize_scale_all))
    
    cmds.button(label = 'Randomize Rotation', command=function_wrapper(randomize_rotation))
    cmds.button(label = 'Randomize Rotation for All Selected', command=function_wrapper(randomize_rotation_all))
    
    cmds.button(label = 'Randomize Translation', command=function_wrapper(randomize_translate))
    cmds.button(label = 'Randomize Translation for All Selected', command=function_wrapper(randomize_translate_all))
    
    
    cmds.showWindow(window)
    
randomization_ui()                    

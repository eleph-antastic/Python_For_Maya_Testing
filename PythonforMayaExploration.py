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

def wrap_function(function_title, min_range, max_range):
    def randomize_translate_all():
        #Randomizes Translations of All Selected objects
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                randnum = random.uniform(min_range, max_range)
                cmds.setAttr('{}.translate{}'.format(i, a), randnum)
        pass
                  
    def randomize_translate():
        #Randomizes Translation of Last Object Selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(min_range, max_range)
            cmds.setAttr('{}.translate{}'.format(sel, a), randnum)
        pass
    
    def randomize_scale_all():
        #Randomizes Scale of All Selected objects
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                randnum = random.uniform(min_range, max_range)
                cmds.setAttr('{}.scale{}'.format(i, a), randnum)
        pass
                    
    def randomize_scale():
        #Randomizes Scale of Last Object Selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform(min_range, max_range)
            cmds.setAttr('{}.scale{}'.format(sel, a), randnum)
        pass
                
    def randomize_rotation_all():
        #Randomizes Rotation of All Selected objects
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                randnum = random.uniform(min_range, max_range)
                cmds.setAttr('{}.rotate{}'.format(i, a), randnum)
        pass
                    
    def randomize_rotation():
        #Randomizes Rotation of Last Object Selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
            randnum = random.uniform((min_range, max_range)
            cmds.setAttr('{}.rotate{}'.format(sel, a), randnum)
        pass
                
    if function_title == "Translate All":
        return randomize_translate_all
    else if function_title == "Translate Selected":
        return randomize_translate
    else if function_title == "Scale All":
        return randomize_scale_all
    else if function_title == "Scale Selected":
        return randomize_scale
    else if function_title == "Rotate All":
        return randomize_rotation_all
    else:
        return randomize_rotation
                    
                    
def randomization_ui():
    window = cmds.window(title = "My UI Test", widthHeight = (500,250), sizeable = True)
    
    master_layout = cmds.columnLayout(adjustableColumn=True)
    
    #Scale Buttons/TextFields
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    scale_min_range_textfield = cmds.textField(editable=False, text='Minimum Range')
    scale_min_range = cmds.textField(editable=True, text='1')
        
    scale_max_range_textfield = cmds.textField(editable=False, text='Max Range')
    scale_max_range = cmds.textField(editable=True, text='10')
        
    cmds.setParent(master_layout)
    
    cmds.button(label = 'Randomize Scale', command=wrap_function("Translate All", min_range, max_range))
    cmds.button(label = 'Randomize Scale for All Selected', command=wrap_function("Translate All", min_range, max_range))
    
    cmds.button(label = 'Randomize Rotation', command=wrap_function("Translate All", min_range, max_range))
    cmds.button(label = 'Randomize Rotation for All Selected', command=wrap_function("Translate All", min_range, max_range))
    
    cmds.button(label = 'Randomize Translation', command=wrap_function("Translate All", min_range, max_range))
    cmds.button(label = 'Randomize Translation for All Selected', command=wrap_function("Translate All", min_range, max_range))
    
    
    cmds.showWindow(window)
    
randomization_ui()                    

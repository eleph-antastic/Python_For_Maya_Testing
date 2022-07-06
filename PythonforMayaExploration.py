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

    
def randomize_translate (multi_select = False, range_min = -10, range_max = 10):
    #Randomizes Translations of the selected object(s) by a range (received in parameters)
    if multi_select == True:  # applies to every item selected
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.translate{}'.format(i, a), randnum)
    else: # applies to last item selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.translate{}'.format(sel, a), randnum)

def randomize_scale (multi_select = False, range_min = 1, range_max = 5):
    #Randomizes Scale of the selected object(s) by a range (received in parameters)
    if multi_select == True:  # applies to every item selected
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.scale{}'.format(i, a), randnum)
    else: # applies to last item selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.scale{}'.format(sel, a), randnum)
                    
                    
def randomize_rotation (multi_select = False, range_min = 0, range_max = 180):
    #Randomizes Translations of the selected object(s) by a range (received in parameters)
    if multi_select == True:  # applies to every item selected
        for i in cmds.ls(sl=True):
            for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.rotate{}'.format(i, a), randnum)
    else: # applies to last item selected
        sel = cmds.ls(sl=True)[len((cmds.ls(sl=True)))-1]
        for a in ['X', 'Y', 'Z']:
                    randnum = random.uniform(range_min, range_max)
                    cmds.setAttr('{}.rotate{}'.format(sel, a), randnum)
                    
                    
def randomization_ui():
    window = cmds.window(title = "My UI Test", widthHeight = (500,250), sizeable = True)
    
    master_layout = cmds.columnLayout(adjustableColumn=True)
    
    #Scale Buttons/TextFields
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    scale_min_range_textfield = cmds.textField(editable=False, text='Minimum Range for Random Scale')
    scale_min_range = cmds.textField(editable=True, text='1')
        
    scale_max_range_textfield = cmds.textField(editable=False, text='Max Range')
    scale_max_range = cmds.textField(editable=True, text='5')
        
    cmds.setParent(master_layout)
    cmds.button(label = 'Randomize Scale', command="randomize_scale(False, " + scale_min_range + ", " + scale_max_range + ")")
    cmds.button(label = 'Randomize Scale for All Selected', command="randomize_scale(True, " + scale_min_range + ", " + scale_max_range + ")")
    
    #Rotation Buttons/TextFields
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    rotate_min_range_textfield = cmds.textField(editable=False, text='Minimum Range for Random Rotation')
    rotate_min_range = cmds.textField(editable=True, text='0')
        
    rotate_max_range_textfield = cmds.textField(editable=False, text='Max Range')
    rotate_max_range = cmds.textField(editable=True, text='180')
        
    cmds.setParent(master_layout)
    cmds.button(label = 'Randomize Rotation', command="randomize_rotation(False, " + rotate_min_range + ", " +  rotate_max_range + ")")
    cmds.button(label = 'Randomize Rotation for All Selected', command="randomize_rotation(True, " + rotate_min_range + ", " + rotate_max_range + ")")
    
    #Translate Buttons/TextFields
    cmds.rowLayout(adjustableColumn=1, numberOfColumns=6)
        
    scale_min_range_textfield = cmds.textField(editable=False, text='Minimum Range for Random Translation')
    scale_min_range = cmds.textField(editable=True, text='1')
        
    scale_max_range_textfield = cmds.textField(editable=False, text='Max Range')
    scale_max_range = cmds.textField(editable=True, text='20')
        
    cmds.setParent(master_layout)
    cmds.button(label = 'Randomize Translation', command="randomize_translate(False, " + scale_min_range + ", " + scale_max_range + ")")
    cmds.button(label = 'Randomize Translation for All Selected', command="randomize_translate(True, " + scale_min_range + ", " + scale_max_range + ")")
    
    
    cmds.showWindow(window)
    
randomization_ui()                    

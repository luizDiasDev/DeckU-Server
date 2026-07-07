import vgamepad as vg

class VirtualGamepad:

    BUTTON_MAP = {
        "LAX": 0, 
        "LAY": 0, 
        "RAX": 0, 
        "RAY": 0, 
        "R2": 0, 
        "L2": 0, 
        "L1": 0, 
        "R1": 0, 
        "DPY": 0, 
        "DPX": 0, 
        "A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A, 
        "X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X, 
        "B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B, 
        "Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, 
        "Select": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, 
        "Start": vg.XUSB_BUTTON.XUSB_GAMEPAD_START
    }

    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
    
    def read_input(self, gamepad_input):

        self.gamepad.left_trigger(value=gamepad_input.get("L2", 0))
        self.gamepad.right_trigger(value=gamepad_input.get("R2", 0))
        self.gamepad.left_joystick(x_value=gamepad_input.get("LAX", 0), y_value=gamepad_input.get("LAY", 0) * -1)
        self.gamepad.right_joystick(x_value=gamepad_input.get("RAX", 0), y_value=gamepad_input.get("RAY", 0) * -1)

        if "A" in gamepad_input:
            if gamepad_input["A"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            if gamepad_input["A"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        
        if "B" in gamepad_input:
            if gamepad_input["B"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            if gamepad_input["B"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        if "X" in gamepad_input:
            if gamepad_input["X"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            if gamepad_input["X"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        
        if "Y" in gamepad_input:
            if gamepad_input["Y"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            if gamepad_input["Y"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        
        if "Select" in gamepad_input:
            if gamepad_input["Select"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            if gamepad_input["Select"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        if "Start" in gamepad_input:
            if gamepad_input["Start"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            if gamepad_input["Start"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        if "L1" in gamepad_input:
            if gamepad_input["L1"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            if gamepad_input["L1"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        if "R1" in gamepad_input:
            if gamepad_input["R1"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            if gamepad_input["R1"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        if "DPY" in gamepad_input:
            if gamepad_input["DPY"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            if gamepad_input["DPY"] == -1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            if gamepad_input["DPY"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        
        if "DPX" in gamepad_input:
            if gamepad_input["DPX"] == 1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            if gamepad_input["DPX"] == -1:
                self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            if gamepad_input["DPX"] == 0:
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            
        self.gamepad.update()

        

        # value = 1

        # if value == 1:
        #     self.gamepad.press_button(button=self.BUTTON_MAP["A"])
        # elif value == 0:
        #     self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    
    
    

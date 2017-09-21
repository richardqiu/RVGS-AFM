"""
Created on Wed Sep 20 00:33:22 2017

@author: Richard
"""

class ReadScanParams:
    def __init__(self, FileName):
        with open(FileName, "r") as ScanFile:
            for line in ScanFile:
                if line.find("Pixels in X:") != -1:
                    self.xPixels = int(line[12:])
                if line.find("Lines in Y:") != -1:
                    self.yPixels = int(line[11:])
                if line.find("X Range:") != -1:
                    self.xRange = float(line[8:])
                if line.find("Y Range:") != -1:
                    self.yRange = float(line[8:])    
                if line.find("Z-Drive") != -1:
                    self.zDriveCalibration = float(line[20:])
                if line.find("Z-Sense") != -1:
                    self.zSenseCalibration = float(line[20:])
                if line.find("X Calibration") != -1:
                    self.xCalibration = float(line[14:])
                if line.find("Y Calibration") != -1:
                    self.yCalibration = float(line[14:])
                if line.find("X Offset") != -1:
                    self.xOffset = float(line[9:])
                if line.find("Y Offset") != -1:
                    self.yOffset = float(line[9:])
                if line.find("Rotation") != -1:
                    self.Rotation = float(line[13:])
                if line.find("Scan Rate") != -1:
                    self.ScanRate = float(line[15:])
                if line.find("Scan Type: ") != -1:
                    self.ScanType = str(line[12:]).rstrip('\n')
                if line.find("Vpp:") != -1:
                    self.Vpp = float(line[4:])
                if line.find("Phase") != -1:
                    self.Phase = float(line[6:])
                if line.find("Demod Gain") != -1:
                    self.DemodGain = line[12:].strip(' \tdB\n')
                if line.find("Selected") != -1:
                    self.Selected = float(line[16:])
                if line.find("Display Type: ") != -1:
                    self.DisplayType = str(line[15:]).rstrip('\n')
                if line.find("Samples/Pixel") != -1:
                    self.SamplesPerPixel = int(line[14:])
                if line.find("XY HV Gain") != -1:
                    self.xyHVGain = float(line[11:])
                if line.find("Z HV Gain") != -1:
                    self.zHVGain = float(line[10:])
                if line.find("Z Sensor Gain") != -1:
                    self.zSensorGain = float(line[14:])            
                if line.find("Setpoint") != -1:
                    self.Setpoint = float(line[9:])
                #X, Y, Z GPID?

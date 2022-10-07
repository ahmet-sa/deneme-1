

from enum import Enum



class QueueState(Enum):
    
    IDLE="IDLE"
    STARTED="STARTED"
    RUNNING="RUNNING"
    CANCELLED="CANCELLED"
    PAUSED="PAUSED"
    FINISHED="FINISHED"

    # def __str__(self):
    #     return str(self.value)



class BedPosition(Enum):
    MIDDLE="MIDDLE"
    FRONT="FRONT"
    BACK="BACK"
    
    # def __str__(self):
    #     return str(self.value)



class MotorState(Enum):
    IDLE="IDLE"
    FORWARD="FORWARD"
    BACKWORD="BACKWORD"
    
class EjectState(Enum):
    WAIT_FOR_TEMP="WAIT_FOR_TEMP"
    EJECTING="EJECTING"
    EJECT_FAİL="EJECT_FAİL"




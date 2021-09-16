from types import ModuleType

from i2c_pkg import i2c as i2c_module
from i2c_pkg.emc2301_pkg import emc2301


class RaspiCM4IOBoardFanSensor(emc2301.EMC2301):
    def __init__(self,
                 address: int = 0x2f,
                 busnum: int = 10,
                 i2c: ModuleType = i2c_module,
                 **kwargs):
        super().__init__(address=address,
                         busnum=busnum,
                         i2c=i2c,
                         **kwargs)

    def fan_speed(self) -> int:
        return self.speed()[0]

    def set_fan_speed_percentage(self, percentage: int):
        """Percentage should be 0 - 100"""
        converted_value = int(percentage / 100 * 255)
        self.write_register(register='FAN_SETTING', value=converted_value)

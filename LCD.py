import asyncio
import RPi_I2C_driver  # assuming the lcd driver is imported here

# ChargeHandler 클래스 선언
class LCDHandler:
    def __init__(self, lcd_address=0x27):
        # LCD 객체 초기화
        self.lcd = RPi_I2C_driver.lcd(lcd_address)

    # 비동기 chargePercent 메서드
    async def chargePercent(self):
        self.lcd.cursor()

        for i in range(0, 100):
            self.lcd.print("Charging")
            self.lcd.setcursor(2, 1)
            self.lcd.print(f"percent : {i}%")
            await asyncio.sleep(0.5)  # 비동기 처리
            self.lcd.clear()

    # 추가적인 메서드가 필요하다면 여기에 정의 가능
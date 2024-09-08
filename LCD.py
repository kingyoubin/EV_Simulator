import asyncio
import RPi_I2C_driver  # assuming the lcd driver is imported here

# ChargeHandler 클래스 선언
class LCDHandler:

    def __init__(self, lcd_address=0x27):
        # LCD 객체 초기화
        self.lcd = RPi_I2C_driver.lcd(lcd_address)

    # 비동기 chargePercent 메서드
    async def chargePercent(self):
        self.lcd.cursor()  # 커서 활성화

        for i in range(0, 100):
            self.lcd.lcd_display_string("Charging", 1)  # 첫 번째 줄에 "Charging" 출력
            self.lcd.lcd_display_string_pos(f"percent : {i}%", 2, 1)  # 두 번째 줄 1번째 위치에 퍼센트 출력
            await asyncio.sleep(0.5)  # 비동기 처리
            self.lcd.clear()

    # 추가적인 메서드가 필요하다면 여기에 정의 가능
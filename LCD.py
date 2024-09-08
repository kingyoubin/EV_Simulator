import asyncio
import RPi_I2C_driver  # assuming the lcd driver is imported here
import time

# ChargeHandler 클래스 선언
class LCDHandler:
    def __init__(self, lcd_address=0x27):
        # LCD 객체 초기화
        self.lcd = RPi_I2C_driver.lcd(lcd_address)

    # chargePercent 메서드: 스레드를 통해 관리
    def chargePercent(self):
        self.lcd.cursor()  # 커서 활성화

        for i in range(0, 100):
            self.lcd.lcd_display_string("Charging", 1)  # 첫 번째 줄에 "Charging" 출력
            self.lcd.lcd_display_string_pos(f"percent : {i}%", 2, 1)  # 두 번째 줄 1번째 위치에 퍼센트 출력
            time.sleep(1)  # 스레드에서 대기 시간을 사용

    def chargeReady(self):
        self.lcd.cursor()  # 커서 활성화
        self.lcd.lcd_display_string("Charging Ready", 1)  # 첫 번째 줄에 "Charging Ready" 출력
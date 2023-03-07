"""
For reference only.
"""

from dataclasses import dataclass
import pyautogui

@dataclass
class Button:
    coordinates:tuple[int,int]
    
    def click(self):
        pyautogui.click(self.coordinates)

@dataclass
class HalfAnniversaryPage:
    frost_and_flame:Button = Button((1234,1234))
    fruit_dodging:Button = Button((1234,1234))
    punch:Button = Button((1234,1234))
    match:Button = Button((1234,1234))
    
    def start_punch(self):
        self.punch.click()
        self.match.click()


half_anni_page:HalfAnniversaryPage = HalfAnniversaryPage()

half_anni_page.start_punch()
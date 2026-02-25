from qfluentwidgets import ScrollBar

def enterEvent(self, e):
    self._isEnter = True
    self.expand()

def leaveEvent(self, e):
    self._isEnter = False
    self.collapse()

ScrollBar.enterEvent = enterEvent
ScrollBar.leaveEvent = leaveEvent

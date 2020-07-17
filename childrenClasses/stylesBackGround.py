from tkinter.ttk import Style
from tkinter import PhotoImage

class BackgroundsStyle(Style):

    BackgroundGrayStyleImage = PhotoImage


    def __init__(self,master=None):

        super().__init__(master=master)

        self.BackgroundGrayStyleImage = PhotoImage("backGroundGrayImage",data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAALiSURBVHhe7Zs/TyJBGMbfHZY/CpdooYmAUl1FIpUNhELt/Qzy1aivwC8gjdpQQaCyMgqFJoRECQq43DzjK8ci3l1icbf7zi8h7+zsbrLPs7MzU/A4p6enPxzH+U6fkEwm6eDggNLpNNrR19fXtP590/covuS/YDabeZFI5FH/esPhcNLr9ajRaJBu8xUf0fdcO5VKpanb+29dv0ilUlQqlWhra4u63S5Np1M+Ewxc16VMJkP39/d0dXVFT09PfMZHa+VbLBQKdHJyQqPRiG5ubgInHuCZ8ezPz89Gy/7+h3ds8BmghzUdHx/T3t4e3d7eYojwmeACDdCSy+Xo8PDQaFzEZ8DR0RFFo1EaDAbcEx6gKR6PG42LzA3AsF9fX//tpBF0oA0aofUdYwAmvHw+H8o3vww0QitWN2AMwGx/d3dnOiQAreVy2bQV3j6WujBMeH8LtG5ubtLa2ho51WrV7AOCuNR9hVgsBiNaamdnJ5Dr/FcZj8dmd4tPIMZ94tArQkxNJpM0H4sD2pX+DlJ8LA5oxzLo2w0KQ0kWb7AGcBWLNYCrWKwBXMViDeAqFmsAV7FYA7iKxRrAVSzWAK5isQZwFYs1gKtYrAFcxWIN4CoWawBXsVgDuIrFGsBVLNYArmKxBnAVCwzw3poi8ZTjOCujFBKAduW6bo+PxQHtajgcjvlYHKPRaKyQrkLASBr4szS0K0TLkK6Sxvb2Nl1eXhI+AXp4ePgQJgoz0Nrv9+nl5eVtHwAnstmsOSkBaL24uDBtYwBChZ1OhzY2NkxnmIHGdrs9D4fNd4LNZtN0voeJwgjiQXjZrVaLe5a2wvV63SQpwjgSoAkpUmhcxGcAwkTn5+cmcrq7uxuKiVEpZbRA07J44DPgHQyRs7Mzk6rChIE1M2jgmfHsiUSCarWab9gv8sf4POKmxWLR7BW0IdHpdJrxPC+l71lp3r9Cj955fF7v8CZIvCM1jqXuM2az2fVPzKoSDzlkojsAAAAASUVORK5CYII=""")

        self.configure("TFrame", borderwidth=0,bg="#616161")

    def CreateStyleBackgroundGray(self):

        self.element_create("backGroundGray","image","backGroundGrayImage",("focus", "backGroundGrayImage"),border=16,sticky="nsew")

        self.layout("backGroundGray",[("backGroundGrayElement",{"sticky": "nsew"})])
from tkinter.ttk import Style
from tkinter import PhotoImage

class BackgroundsStyle(Style):

    BackgroundGrayStyleImage = PhotoImage


    def __init__(self,master=None):

        super().__init__(master=master)

        self.BackgroundGrayStyleImage = PhotoImage("backGroundGrayImage",data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAAL8SURBVHhe7Zs7bxNBFIXPztob78YJxo9AQUioQkODXCQRNBENCH4BNOG/IWpAggIkkIiUSAkUgBBUMYQCnPXKED/Wm3iWOw/nheig8M58snSU2VWUc33nzKS4zurq/RSgzzE4K6BXvIre5BUkExfAc9P0BtNPxwMHQ7CDPXiDbwi67xF03oLxWD89ggqwesy9g870EtqVO6j6Pcz7O6jmQxRzPbj0C8cJso/OsIgwqaDRn0UYT6IUPkLx1wY9PbJ8WIDUcdGauQdWWsBSaRMzXihfyArNpIb1dh28/QmV5gM4qfpCdV870nxQnsOt2vPMmRfMeLu4WX1BHufJ6129qgsg2p6dXcBK5TXyzoFYyiQe28dKeQ1O6TJ5XpZrTASe2POL05uZNj8iT0VYPLNFnm/TtvfARNqLwDs3kb22/xvnJ3ZR8WN0p+pUADrq5ijtTWO+8EUe80yc8zU66kyj6kXyjsO4OyXPedMI3D6Ed5Y6jI6C8brk/AsYXYbE3We87rf/AWMLMLoMH94ETWPkWBfg5H+DJmFsB4ywHaDVOGwIajV2C9gO0GpDUKtxnNoC5nFqC5iHDUGtNgSVmNcBp7aAeR1gQ1CrDUElNgSVGIQNQa02BJXYEFRiIDYEldgQNA4bglptCCqxIajEIGwIarUhqMSGoBIDsR2g1ThsCGo1dgvYDtBqQ9BJOXjq6h/NQQxVibkhxoZ76Ax9vWwO/WEBwjsTc3W7SVUvm0OYlOVMIRNDhY3+Rb1sDtvkOei+owJ03qAVB/hhUBd8H9QQxT4m97YoA/gApdZjbLTrSHhOv5JdBjyPjZ918vyEQnBfHYNinJS3P+NldD3TRUjI/KvoGtD+SJ7X5drhPUCMk/aiBp6FN2SLZA3h6Sl560XbKDcf6lW6EJ0cnhZTpMtyqLBc6OOS/xXVfAtBLqZKcf3GeMDpL+7sFxAdVGTgRXFBtr0anj7ijwIIUicvhwrV+PwsuFuUA0bjhLjkuHTOe4Md+N0PMvDEnj8J8Bt64Q8saTpJaQAAAABJRU5ErkJggg==""")
        self.BackGroundGreenStyleImage = PhotoImage("BackGroundGreenImage",data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAAIOSURBVHhe7ZtNT9tAFEWvxzE4riVAIEGgqgSirNmwaP9N/iwsYMGWFhVRtQ0bSCo5IYm/mDc8o1iA6LLMe2dzY3t1TzxvvJmg3+/XeIF5t8Kol2O8XmKaliijGnXAD/9zAtsozAPEWYj0NsTKIMLSveGnbZ4JKGzRm4MpRjv5uyn8FiRk7XeEze8xOvN2qZaWyUqJy69jDD/6U56gLne20+WXMe5tx0WeBFD5q6MJ8rjiO/5B3X7YjosSnIBiqcbPwwmq8MVx4BXU8dp2pZlGOAG05vPY//IN1HVgOxNmnthpv527C0lQZ1oSZrTl18D7V2r77g+tBJOtF3xLHtTdzFJ/p/5bUHfTTEOJUHcjcf03UPfWl6BEVACnWFQAp1hUAKdYVACnWFQAp1hUAKdYVACnWFQAp1hUAKdYVACnWFQAp1hUAKdYVACnWFQAp1hUAKdYVACnWFQAp1hUAKdYVACnWFQAp1gMnaeRCnU3dLpKKtTdLGdyV8FyFsKktx2+lAedKTSrg8itBWkEFbD2J4KhE5Wr9oc0qHM0NY/b4NZFbC/kDEPq2vsWu99OQMdOw0/nCUzpvwRTPHZtdr+nLSD5G2L3NPH6TaBue2eJ69rQ2gPpwf5J6g4a05DwBTfwfkX4fJyiu1CeePX4fN6tMOzlyDYKzD5U7lQ53tHLQafE6Rsnveu4P5QG3nOABwwuo+OTdyKeAAAAAElFTkSuQmCC""")


    def CreateStyleBackgroundGray(self):

        self.element_create("backGroundGrayElement","image","backGroundGrayImage",border=16,sticky="nsew")

        self.layout("backGroundGray",[("backGroundGrayElement",{"sticky": "nsew","expand":True})])

    def CreateStyleBackgroundGrayProcess(self):

        self.element_create("backGroundGrayElementPro","image","backGroundGrayImage",border=16,sticky="nsew")

        self.layout("backGroundGrayPro",[("backGroundGrayElementPro",{"sticky": "nsew","expand":True})])

    def CreateStyleResultPanel(self):

        self.element_create("BackGroundGreenElement","image","BackGroundGreenImage",border=16,sticky="nsew")

        self.layout("BackGroundGreen",[("BackGroundGreenElement",{"sticky": "nsew","expand":True})])

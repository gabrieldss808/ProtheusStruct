from tkinter.ttk import Style
from tkinter import PhotoImage

class BackgroundsStyle(Style):

    BackgroundGrayStyleImage = PhotoImage


    def __init__(self,master=None):

        super().__init__(master=master)

        self.BackgroundGrayStyleImage = PhotoImage("backGroundGrayImage",data="""iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAAL8SURBVHhe7Zs7bxNBFIXPztob78YJxo9AQUioQkODXCQRNBENCH4BNOG/IWpAggIkkIiUSAkUgBBUMYQCnPXKED/Wm3iWOw/nheig8M58snSU2VWUc33nzKS4zurq/RSgzzE4K6BXvIre5BUkExfAc9P0BtNPxwMHQ7CDPXiDbwi67xF03oLxWD89ggqwesy9g870EtqVO6j6Pcz7O6jmQxRzPbj0C8cJso/OsIgwqaDRn0UYT6IUPkLx1wY9PbJ8WIDUcdGauQdWWsBSaRMzXihfyArNpIb1dh28/QmV5gM4qfpCdV870nxQnsOt2vPMmRfMeLu4WX1BHufJ6129qgsg2p6dXcBK5TXyzoFYyiQe28dKeQ1O6TJ5XpZrTASe2POL05uZNj8iT0VYPLNFnm/TtvfARNqLwDs3kb22/xvnJ3ZR8WN0p+pUADrq5ijtTWO+8EUe80yc8zU66kyj6kXyjsO4OyXPedMI3D6Ed5Y6jI6C8brk/AsYXYbE3We87rf/AWMLMLoMH94ETWPkWBfg5H+DJmFsB4ywHaDVOGwIajV2C9gO0GpDUKtxnNoC5nFqC5iHDUGtNgSVmNcBp7aAeR1gQ1CrDUElNgSVGIQNQa02BJXYEFRiIDYEldgQNA4bglptCCqxIajEIGwIarUhqMSGoBIDsR2g1ThsCGo1dgvYDtBqQ9BJOXjq6h/NQQxVibkhxoZ76Ax9vWwO/WEBwjsTc3W7SVUvm0OYlOVMIRNDhY3+Rb1sDtvkOei+owJ03qAVB/hhUBd8H9QQxT4m97YoA/gApdZjbLTrSHhOv5JdBjyPjZ918vyEQnBfHYNinJS3P+NldD3TRUjI/KvoGtD+SJ7X5drhPUCMk/aiBp6FN2SLZA3h6Sl560XbKDcf6lW6EJ0cnhZTpMtyqLBc6OOS/xXVfAtBLqZKcf3GeMDpL+7sFxAdVGTgRXFBtr0anj7ijwIIUicvhwrV+PwsuFuUA0bjhLjkuHTOe4Md+N0PMvDEnj8J8Bt64Q8saTpJaQAAAABJRU5ErkJggg==""")

    def CreateStyleBackgroundGray(self):

        self.element_create("backGroundGrayElement","image","backGroundGrayImage",border=16,sticky="nsew")

        self.layout("backGroundGray",[("backGroundGrayElement",{"sticky": "nsew","expand":True})])

    def CreateStyleBackgroundGrayProcess(self):

        self.element_create("backGroundGrayElementPro","image","backGroundGrayImage",border=16,sticky="nsew")

        self.layout("backGroundGrayPro",[("backGroundGrayElementPro",{"sticky": "nsew","expand":True})])
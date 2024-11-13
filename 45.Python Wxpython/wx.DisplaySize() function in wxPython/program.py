# importing the module
import wx


# definition of the Example class
class Example(wx.Frame):

    # instantiating the class
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    # method for creation of user interface
    def InitUI(self):
        # print the size of display
        print(wx.DisplaySize())


# definition of the main function
def main():
    # creating an App object
    app = wx.App()

    # creating an Example object
    ex = Example(None)

    # showing the Example object
    ex.Show()

    # running the App object
    app.MainLoop()


# driver code
if __name__ == '__main__':
    main()

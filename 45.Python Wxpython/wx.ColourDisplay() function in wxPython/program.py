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

        # condition for colour display
        if (wx.ColourDisplay() == True):

            # print if display is Colour display
            print("Display is Colour Display")

        else:

            # print if display is not Colour display
            print("Display is not Colour Display")


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

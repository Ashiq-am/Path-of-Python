# import wxPython
import wx


class TextExample(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(TextExample, self).__init__(*args, **kwargs)
        # put some text
        st = wx.StaticText(self, label="Welcome to GeeksforGeeks")

        # create font object
        font = st.GetFont()

        # increase text size
        font.PointSize += 10

        # make text bold
        font = font.Bold()

        # associate font with text
        st.SetFont(font)


def main():
    app = wx.PySimpleApp()

    frame = TextExample(None, title="Read Text")
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

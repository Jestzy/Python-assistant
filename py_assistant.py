import wx
import wikipedia
import wolframalpha
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 

class QFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos = wx.DefaultPosition,\
                          size = wx.Size(450,100), style = wx.MINIMIZE_BOX\
                          | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX |\
                          wx.CLIP_CHILDREN, title = "Py Assistant")
        panel = wx.Panel(self)
        panel.SetBackgroundColour('grey')
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,\
                            label = "Hello, I'm your Assistant. How canI help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, \
                               size = (400, 30) )
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine.say('Hello, How can I help you?')
        engine.runAndWait()
                            
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = "YOUR_APPID"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
            engine.say(answer)
            engine.runAndWait()
            
        except:
            #wikipedia
            print wikipedia.summary(input)
            engine.say("Search for" + input)
            engine.runAndWait()
            
        
if __name__ == "__main__":

    app = wx.App(True)
    frame = QFrame()
    app.MainLoop()





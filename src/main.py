from tkinter import *
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import dijkstra
import graph

class TopMenu(Frame):
    """ Top menu of the application

    """
    def __init__(self, parent, g):
        Frame.__init__(self, parent)
        self.btnHome = Button(self, text="Home", command=lambda:self.clickHome(parent))
        self.btnHome.grid(row=0, column=0, sticky=W)
        self.btnSetup = Button(self, text="Setup", command=lambda:self.clickSetup(parent))
        self.btnSetup.grid(row=0, column=1, sticky=W)
        self.gr = g
        self.content = Home(parent, self.gr)
        self.content.grid(row=1, column=0, sticky=W)
    
    def clickSetup(self, parent):
        """Shows the setup frame when the Setup button is clicked.

        """
        self.content.destroy()
        self.content = Setup(parent, self.gr)
        self.content.grid(row=1, column=0, sticky=W)

    def clickHome(self, parent):
        """Shows the home frame when the Home button is pressed.
        
        """
        self.content.destroy()
        self.content = Home(parent, self.gr)
        self.content.grid(row=1, column=0, sticky=W)

class Home(Frame):
    """Home frame with the visualisation of the graph and results for different
    strategies.
        
    """
    def __init__(self, parent, g):
        Frame.__init__(self, parent)
        self.gr = g
        self.greedy = IntVar(parent)
        self.reposition = IntVar(parent)
        self.comparison = IntVar(parent)
        self.waiting = IntVar(parent)
        self.recoveryGreedy = IntVar(parent)
        self.src = IntVar(parent)
        self.dest = IntVar(parent)
        self.methodName=""
        self.path = "------"
        self.len = "------"
        self.penalty = "------"

        # Checkbuttons to choose which method to use for CTP/RCTP solving
        cbFrame = Frame(self)
        cbFrame.grid(row=1, column=0)
        cbGreedy = Checkbutton(cbFrame, variable=self.greedy, text="Greedy")
        cbGreedy.grid(row=0, column=0,sticky=W)
        cbReposition = Checkbutton(cbFrame, variable=self.reposition, text="Reposition")
        cbReposition.grid(row=0, column=1,sticky=W)
        cbComparison = Checkbutton(cbFrame, variable=self.comparison, text="Comparison")
        cbComparison.grid(row=0, column=2,sticky=W)
        cbWaiting = Checkbutton(cbFrame, variable=self.waiting, text="Waiting")
        cbWaiting.grid(row=0, column=3,sticky=W)
        cbRecoveryGreedy = Checkbutton(cbFrame, variable=self.recoveryGreedy, text="Recovery greedy")
        cbRecoveryGreedy.grid(row=0, column=4,sticky=W)    
        
        # Entries for source and destination and start button
        enFrame = Frame(self)
        enFrame.grid(row=2, column=0)
        srcLabel = Label(enFrame, text="Source:")
        srcLabel.grid(row=0, column=0, sticky=W)
        srcEntry = Entry(enFrame, textvariable=self.src, width=3)
        srcEntry.grid(row=0, column=1, sticky=W)
        destLabel = Label(enFrame, text="Destination:")
        destLabel.grid(row=0, column=2, sticky=W)
        destEntry = Entry(enFrame, textvariable=self.dest, width=3)
        destEntry.grid(row=0, column=3, sticky=W)
        button1 = Button(enFrame, text="Start!", command=lambda:(self.solveCTP(self), print(self.greedy.get())))
        button1.grid(row=0, column=4, sticky=W)

        # Graph
        self.canvas = FigureCanvasTkAgg(self.gr.f, self)  
        self.canvas.get_tk_widget().grid(row=3, column=0)

        # Results
        self.resultFrame = Frame(self)
        self.resultFrame.grid(row=5, column=0)
        self.resultMainLabel = Label(self.resultFrame, text="Method:")
        self.resultMainLabel.grid(row=0, column=0)
        self.MethodLabel = Label(self.resultFrame, text=self.methodName)
        self.MethodLabel.grid(row=0, column=1)
        self.pathLabel1 = Label(self.resultFrame, text="Path:")
        self.pathLabel1.grid(row=1, column=0)
        self.pathLabel2 = Label(self.resultFrame, text=self.path)
        self.pathLabel2.grid(row=1, column=1)
        self.lenLabel1 = Label(self.resultFrame, text="Lenght:")
        self.lenLabel1.grid(row=2, column=0)
        self.lenLabel2 = Label(self.resultFrame, text=self.len)
        self.lenLabel2.grid(row=2, column=1)
        self.penaltyLabel1 = Label(self.resultFrame, text="Penalty:")
        self.penaltyLabel1.grid(row=3, column=0)
        self.penaltyLabel2 = Label(self.resultFrame, text=self.penalty)
        self.penaltyLabel2.grid(row=3, column=1)
        

    def solveCTP(self, parent):
        """Method that start solving the CTP/RCTP when the Start! button is pressed.
        
        """
        resultFrame = Frame(parent)
        resultFrame.grid(row=4, column=0)

        button0 = Button(resultFrame, text="Graph", command=lambda:self.showResults(parent, self, self.gr.f, "------", "------", "------", ""))
        button0.grid(row=0, column=0, sticky=W)
        try:
            if self.greedy.get() == 1:
                pG= graph.Greedy(self.gr.G)
                self.pathGreedy = pG.greedy(int(self.src.get()), int(self.dest.get()))
                button1 = Button(resultFrame, text="Result Greedy", command=lambda:self.showResults(parent, self, self.pathGreedy[3], self.pathGreedy[0], self.pathGreedy[1], "-----", "Greedy"))
                button1.grid(row=0, column=1, sticky=W)
            if self.reposition.get() == 1:
                pR = graph.Reposition(self.gr.G)
                self.pathReposition = pR.reposition(int(self.src.get()), int(self.dest.get()))
                button2 = Button(resultFrame, text="Result Reposition", command=lambda:self.showResults(parent, self, self.pathReposition[3], self.pathReposition[0], self.pathReposition[1], "-----", "Repostition"))
                button2.grid(row=0, column=2, sticky=W)
            if self.comparison.get() == 1:
                pC = graph.Comparison(self.gr.G)  
                self.pathComparison = pC.comparison(int(self.src.get()), int(self.dest.get()))
                button3 = Button(resultFrame, text="Result Comparison", command=lambda:self.showResults(parent, self, self.pathComparison[3], self.pathComparison[0], self.pathComparison[1], "-----", "Comparison"))
                button3.grid(row=0, column=3, sticky=W)
            if self.waiting.get() == 1:
                pW = graph.Waiting(self.gr.G)
                self.pathWaiting = pW.waiting(int(self.src.get()), int(self.dest.get()))
                button4 = Button(resultFrame, text="Result Waiting", command=lambda:self.showResults(parent, self, self.pathWaiting[4], self.pathWaiting[0], self.pathWaiting[1], self.pathWaiting[2], "Waiting"))
                button4.grid(row=0, column=4, sticky=W)
            if self.recoveryGreedy.get() == 1:
                pRG = graph.RecoveryGreedy(self.gr.G)
                self.pathRecoveryGreedy = pRG.recoveryGreedy(int(self.src.get()), int(self.dest.get()))
                button5 = Button(resultFrame, text="Result Recovery Greedy", command=lambda:self.showResults(parent, self, self.pathRecoveryGreedy[4], self.pathRecoveryGreedy[0], self.pathRecoveryGreedy[1], self.pathRecoveryGreedy[2], "Recovery Greedy"))
                button5.grid(row=0, column=5, sticky=W)
        except:
            print("bad parameters")

    def showResults(self, figureParent, resultParent, f, p, l, pen, m):
        """Shows the results for chosen strategy.
        
        """
        self.showGraph(figureParent, f)
        txt = ""
        for i in p:
            txt += str(i)
            txt += " "
        self.MethodLabel["text"] = m
        self.pathLabel2["text"] = txt
        self.lenLabel2["text"] = l
        self.penaltyLabel2["text"] = pen
    
    def showGraph(self, figureParent, f):
        """Shows the Matplotlib figure in the Home frame.
        
        """
        self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(f, figureParent)  
        self.canvas.get_tk_widget().grid(row=3, column=0)


class Setup(Frame):
    """Setup frame with the configuration options.

    User can generate random graph, add edges, change edges.
    
    """
    def __init__(self, parent, g):
        Frame.__init__(self, parent)
        self.probability = IntVar(parent)
        self.num = IntVar(parent)
        self.directed = IntVar(parent)
        self.eFrom = IntVar(parent)
        self.eTo = IntVar(parent)
        self.eLen = IntVar(parent)
        self.ePenalty = IntVar(parent)
        self.eFromChange = IntVar(parent)
        self.eToChange = IntVar(parent)
        self.eLenChange = IntVar(parent)
        self.ePenaltyChange = IntVar(parent)
        self.gr = g

        label1 = Label(self, text="Setup")
        label1.grid(row=0, column=0)
        
        # Generating random graph
        label2 = Label(self, text="Generate random graph?")
        label2.grid(row=1, column=0, sticky=W)
        numVertLabel = Label(self, text="Number of vertices:")
        numVertLabel.grid(row=2, column=0, sticky=W)
        numVertEntry = Entry(self, textvariable=self.num, width=3)
        numVertEntry.grid(row=2, column=1, sticky=W)
        probabilityLabel = Label(self, text="Probability of blockages:")
        probabilityLabel.grid(row=3, column=0, sticky=W)
        probabilityEntry = Entry(self, textvariable=self.probability, width=3)
        probabilityEntry.grid(row=3, column=1, sticky=W)
        probabilityEntry.var = self.probability
        directedLabel = Label(self, text="Directed?")
        directedLabel.grid(row=4, column=0, sticky=W)
        directedCB = Checkbutton(self, variable=self.directed)
        directedCB.grid(row=4, column=1,sticky=W)
        button2 = Button(self, text="Generate!", command=self.generateGraph)
        button2.grid(row=5, column=0, sticky=W)

        # Adding edge
        label3 = Label(self, text="Add edge (from-to-length-penalty):")
        label3.grid(columnspan=5, row=7, column=0, sticky=W)
        edgeFrom = Entry(self, width=2)
        edgeFrom.grid(row=7, column=3, sticky=W)
        edgeFrom.var = self.eFrom
        edgeTo = Entry(self, width=2)
        edgeTo.grid(row=7, column=4, sticky=W)
        edgeTo.var = self.eTo
        edgeLength = Entry(self, width=2)
        edgeLength.grid(row=7, column=5, sticky=W)
        edgeLength.var = self.eLen
        edgePenalty = Entry(self, width=2)
        edgePenalty.grid(row=7, column=6, sticky=W)
        edgePenalty.var = self.ePenalty
        button4 = Button(self, text="Add!", command=lambda:(self.gr.addEdge(int(edgeFrom.get()), int(edgeTo.get()), int(edgeLength.get()), int(edgePenalty.get())), self.fillEdges(), self.gr.drawGraph()))
        button4.grid(row=7, column=7, sticky=W)
        
        # Listbox with edges
        label4 = Label(self, text="Edges (source destination lenght penalty)")
        label4.grid(columnspan=3, row=8, column=0)
        self.listbox = Listbox(self, selectmode=BROWSE)
        self.listbox.bind("<<ListboxSelect>>", self.chosenEdge)
        self.listbox.grid(row=9, column=0)
        self.fillEdges()

        # Changing and removing edges
        label5 = Label(self, text="Change edge (from-to-length-penalty):")
        label5.grid(columnspan=5, row=10, column=0, sticky=W)
        self.edgeFromChange = Entry(self, textvariable=self.eFromChange, width=2)
        self.edgeFromChange.grid(row=10, column=3, sticky=W)
        #self.edgeFromChange.var = self.eFromChange
        self.edgeToChange = Entry(self, textvariable=self.eToChange, width=2)
        self.edgeToChange.grid(row=10, column=4, sticky=W)
        #self.edgeToChange.var = self.eToChange
        self.edgeLengthChange = Entry(self, textvariable=self.eLenChange, width=2)
        self.edgeLengthChange.grid(row=10, column=5, sticky=W)
        #self.edgeLengthChange.var = self.eLenChange
        self.edgePenaltyChange = Entry(self, textvariable=self.ePenaltyChange, width=2)
        self.edgePenaltyChange.grid(row=10, column=6, sticky=W)
        #self.edgePenaltyChange.var = self.ePenaltyChange
        button5 = Button(self, text="Change!", command=lambda:(self.gr.changeEdge(int(self.eFromChange.get()), int(self.eToChange.get()), int(self.eLenChange.get()), int(self.ePenaltyChange.get())), self.fillEdges(), self.gr.drawGraph()))
        button5.grid(row=10, column=7, sticky=W)
        button6 = Button(self, text="Remove!", command=lambda:(self.gr.removeEdge(int(self.eFromChange.get()), int(self.eToChange.get())), self.fillEdges(), self.gr.drawGraph()))
        button6.grid(row=10, column=8, sticky=W)

    def generateGraph(self):
        """Method called when the Generate! button is pressed.

        """
        try:
            self.gr.generateRandom(self.num.get(), bool(self.directed.get()), self.probability.get()/100)
            self.listbox.delete(0, END)
            self.fillEdges()
        except:
            print("bad parameters")

    def fillEdges(self):
        """Method which fills the listbox with edges parameters.

        """
        self.listbox.delete(0, END)
        lEdges = list(self.gr.G.edges)
        for e in lEdges:
            s = str(e[0]) + " " + str(e[1]) + " " + str(self.gr.G.edges[e[0], e[1]]['lenght']) + " " + str(self.gr.G.edges[e[0], e[1]]['penalty'])
            self.listbox.insert(END, s)
            print(e[0], e[1], self.gr.G.edges[e[0], e[1]]['lenght'], self.gr.G.edges[e[0], e[1]]['penalty'])
    
    def chosenEdge(self, evt):
        """Method that fills the prepared Entry widges with the values of the selected edge
        from listbox to change them.

        """
        s = self.listbox.get(self.listbox.curselection())
        s1 = []
        sh = ""
        for i in s:
            if i != " ":
                sh += i
            else:
                s1.append(sh)
                sh = ""
        s1.append(sh)
        # self.eFromChange = int(s1[0])
        self.eFromChange.set(int(s1[0]))
        self.changeEntry(self.edgeFromChange, self.eFromChange.get())
        self.eToChange.set(int(s1[1]))
        self.changeEntry(self.edgeToChange, self.eToChange.get())
        # self.eLenChange = int(s1[2])
        self.eLenChange.set(int(s1[2]))
        self.changeEntry(self.edgeLengthChange, self.eLenChange.get())
        # self.ePenaltyChange = int(s1[3])
        self.ePenaltyChange.set(int(s1[3]))
        self.changeEntry(self.edgePenaltyChange, self.ePenaltyChange.get())
    
    def changeEntry(self, what, new_entry):
        """Changes entry of the widget.
        
        """
        what.delete(0, END)
        what.insert(0, new_entry)

def main():
    g = graph.Graph()
    root = Tk()
    root.title("CTP")
    root.geometry("600x600+0+0")
    t = TopMenu(root, g)
    t.grid(row=0, column=0, sticky=W)
    root.mainloop()


if __name__ == '__main__':
    main()
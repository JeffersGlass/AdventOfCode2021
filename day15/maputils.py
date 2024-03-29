import curses
from time import sleep
from astarutils import calc_h_cost

class mapDisplay():
    def __init__(self, maxX, maxY, risk, locationScores=[], openPoints=[], closedPoints=[], pathPoints = [], oldSelection=[0,0], end=None, pathLength = 0):
        self.maxX = maxX
        self.maxY = maxY
        self.risk = risk
        self.locationScores = locationScores
        self.openPoints = openPoints
        self.closedPoints = closedPoints
        self.selection = oldSelection
        self.pathPoints = pathPoints
        self.pathLength = pathLength
        self.retCode = {'exitcode':0, 'selection': self.selection }
        if end == None:
            self.end = (maxX-1, maxY-1)
        else:
            self.end = end

        screen = curses.initscr()
        screen.keypad(True)

        curses.start_color()
        #color pair 0 is white on black standard
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) #1 - open points
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) #2 - closed points
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) #3 - end point 
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK) #4 -  final path

        curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_WHITE) #11 - open points highlighted
        curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_GREEN) #11 - open points highlighted
        curses.init_pair(12, curses.COLOR_BLACK, curses.COLOR_RED) #12 - closed points highlighted
        curses.init_pair(13, curses.COLOR_BLACK, curses.COLOR_YELLOW) #13 - end point 
        curses.init_pair(14, curses.COLOR_BLACK, curses.COLOR_MAGENTA) #14 - final path

    
        self.map_pad = curses.newpad(maxY+1,maxX+1)

        self.info_pad = curses.newpad(7, 40)
        self.info_pad.addstr(0,0,"Coords:")
        self.info_pad.addstr(1,0,"F_Cost:")
        self.info_pad.addstr(2,0,"G_Cost:")
        self.info_pad.addstr(3,0,"H_Cost:")

        self.instruction_pad = curses.newpad(5,40)
        self.instruction_pad.addstr(0,0,"Arrow keys to move")
        self.instruction_pad.addstr(1,0,"Enter to advance")
        self.instruction_pad.addstr(2,0,"Esc to hard quit")

        self.open_pad = curses.newpad(200,20)
        self.open_pad.addstr(0,0,"Open Points", curses.A_UNDERLINE)
         
        curses.noecho()
        self.redraw()

        while True:
            c = screen.getch()
            if c == 10: #Enter to continue
                self.retCode['exitcode'] = 0
                break
            elif c == 27: #Escape to quit
                self.retCode['exitcode'] = 1
                break
            elif c == 100: #d
                self.redraw()
            elif c == 50 or c == 456: #numpad down
                self.selection[1] = min(self.selection[1] + 1, maxY)
                self.redraw()
            elif c == 56 or c == 450: #numpad up
                self.selection[1] = max(self.selection[1]-1, 0)
                self.redraw()
            elif c == 52 or c == 452: #numpad left
                self.selection[0] = max(self.selection[0]-1, 0)
                self.redraw()
            elif c == 54 or c == 454: #numpad right
                self.selection[0] = min(self.selection[0]+1, maxX)
                self.redraw()

    def redraw(self): #pad, maxX, maxY, risk, locationScores=[], openPoints=[], closedPoints=[], selection=[0,0]):
        self.updateMapPad()
        self.update_info_pad()
        self.update_instruction_pad()
        self.update_open_pad()

    def updateMapPad(self):
        for x in range(self.maxX):
            for y in range (self.maxY):
                if [x, y] == self.selection:
                    if (x,y) == self.end: color = curses.color_pair(13)
                    elif (x,y) in self.pathPoints: color = curses.color_pair(14)
                    elif (x,y) in self.openPoints: color = curses.color_pair(11)
                    elif (x,y) in self.closedPoints: color = curses.color_pair(12)
                    else: color = curses.color_pair(10)
                else:
                    if (x,y) == self.end: color = curses.color_pair(3)
                    elif (x,y) in self.pathPoints: color= curses.color_pair(4)
                    elif (x,y) in self.openPoints: color = curses.color_pair(1)
                    elif (x,y) in self.closedPoints: color = curses.color_pair(2)
                    else: color = curses.color_pair(0)
                
                self.map_pad.addch(y, x, str(self.risk[(x,y)]), color)

        self.map_pad.refresh(0,0,0,0,curses.LINES-1,40)

    def update_info_pad(self):
        #Coordinates
        self.info_pad.addstr(0,10,"          ")
        self.info_pad.addstr(0,10,str(self.selection))

        #F Cost
        self.info_pad.addstr(1,10,"          ")
        if tuple(self.selection) in self.locationScores:
            self.info_pad.addstr(1,10,str(self.locationScores[tuple(self.selection)].f_cost) + "      ")
            self.info_pad.addstr(2,10,str(self.locationScores[tuple(self.selection)].g_cost) + "      ")
        else:
            self.info_pad.addstr(1,10,"Unknown")
            self.info_pad.addstr(2,10,"Unknown")

        #H Cost
        self.info_pad.addstr(3,10,"         ")
        self.info_pad.addstr(3,10,str(calc_h_cost(self.selection, self.end)))
        if self.pathPoints != []:
            self.info_pad.addstr(4,0,"Path Length:")
            self.info_pad.addstr(5,0,str(self.pathLength))
        else:
            self.info_pad.addstr(4,0,"Searching...")

        self.info_pad.refresh(0,0,0,40,5,80)
    
    def update_instruction_pad(self):
        self.instruction_pad.refresh(0,0,10,40,12,60)

    def update_open_pad(self):
        pointList = sorted(self.openPoints[:min(len(self.openPoints), 99)], key= lambda x:self.locationScores[x].f_cost)
        for i, p in enumerate(pointList):
            self.open_pad.addstr(i+1,0,f"{p} - {self.locationScores[p].f_cost}")
        self.open_pad.refresh(0,0,0,70,10,100)

    
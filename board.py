from pieces import Pieces  
#9 horizontal, 10 vertical board.

#Use Brackets [] - []

class Board:
  def __init__(self, board = []):
    self.b = board
    self.b1 = self.b
    self.undo = False
    print("self.b1 = self.b")
    a = ["_", "_","_", "_","_", "_","_", "_","_"]
    for i in range(10):
      self.b.append(a)
      a = ["_", "_","_", "_","_", "_","_", "_","_"]
      #every line of the board would point to the same A list if we don't do the step above
      #therefore, changing one line would change the only A list and change everyline on board
    
    self.b[0][0] = '黑车'
    self.b[0][8] =  '黑车'
    self.b[9][0] =  '红车'
    self.b[9][8] =  '红车'
    
    self.b[0][1] =  '黑马'
    self.b[0][7] =  '黑马'
    self.b[9][1] =  '红马'
    self.b[9][7] =  '红马'
    
    self.b[0][2] =  '黑相'
    self.b[0][6] =  '黑相'
    self.b[9][2] =  '红相'
    self.b[9][6] =  '红相'
    
    self.b[0][3] =  ('黑士')
    self.b[0][5] =  ('黑士')
    self.b[9][3] =  ('红士')
    self.b[9][5] =  ('红士')
    
    self.b[0][4] =  ('黑帅')
    self.b[9][4] =  ('红帅')
    
    self.b[2][1] =  ('黑炮')
    self.b[2][7] =  ('黑炮')
    self.b[7][1] =  ('红炮')
    self.b[7][7] =  ('红炮')
    
    for v in range(10):
      for h in range(9):
        if v == 3 and h % 2 == 0:
          self.b[v][h] =  ('黑兵')
        if h % 2 == 0 and v == 6:
          self.b[v][h] =  ('红兵')
        if self.b[v][h] == "_":
          self.b[v][h] =  ('一一') #empty space
        
    
  def printBoard(self):
    print("|0| |零零|   |一一|  |二二|  |三三|  |四四|  |五五|  |六六|  |七七| |八八|")
    for v in range(10):
      print("|" + str(v) + "|"),
      for h in range(8):
        print('[' + str(self.b[v][h]) + ']-'),
      print('[' + str(self.b[v][8]) + ']')
      if v != 9 and v != 4 and v != 1 and v != 0 and v != 7 and v != 8:
        print("       |      |       |       |       |       |       |     |       |")
      if v == 4:
        print("|楚____________________河_____________________汉___________________界|")
      if v == 1 or v == 8:
        print("       |      |       |       |  /   |   \   |       |     |       |")
      if v == 0 or v == 7:
        print("       |      |       |       |  \    |  /   |       |     |       |")
        #printed after line 5 is printed
        
  def endgame(self):
    redcommander = False
    blackcommander = False
    for v in range(10):
      for h in range(8):
        if self.b[v][h] == "红帅":
          redcommander = True
        if self.b[v][h] == "黑帅":
          blackcommander = True
    if redcommander == True and blackcommander == False:
      print("红方胜")
      return True
      
    if redcommander == False and blackcommander == True:
      print("黑方胜")
      return True
        
  def play(self, turn):
    if turn % 2 == 0: #It's red's turn
      print("轮到红方了")
      side = "红"
    else:
      print("轮到黑方了")
      side = "黑"
    
    #self.b[v][h] [0] is side
    #self.b[v][h] [1] is role
    

    print("undo?") #this function currently doesn't work because b1 points to b at all times.
    h = input()
    if h == "Yes" or h == "yes":
      if self.undo != True:
        self.undo = True
        self.b1 = self.b
      elif self.undo == True:
        self.b = self.b1
        self.undo = False
        return turn - 1
    else:
      self.undo = True
      self.b1 = self.b
        
    
    print("输入棋子的坐标X")
    h = int(input())
    print("输入棋子的坐标Y")
    v = int(input())
    
    print("你想棋子挪到哪里? 请输入X, Y 坐标。")
    x = int(input())
    y = int(input())
    
    if h == x and v == y or side == self.b[y][x][0]:
      print("你在干嘛?")
      return turn
    
    
    if self.b[v][h] [0] != side:
      print("That unit doesn't belong to you")
      return turn
    else:
      if self.b[v][h] [1] == "车":
        if x == h: #it is moving vertically
        
          if y > v: #downwards
            for i in range(v + 1, y, 1):
              if self.b[i][x] [1] != "一":
                print("有东西挡着你的棋子")
                return turn
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          
          if v > y: #upwardsF
            for i in range(y + 1, v, 1):
              if self.b[i][x] [1] != "一":
                print("有东西挡着你的棋子")
                return turn
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
                
          
        if v == y: #horizontally
          if x > h:
            for i in range(h + 1, x, 1): #rightwards
              if self.b[v][i] [1] != "一":
                print("有东西挡着你的棋子")
                return turn
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          if x < h: #moving leftwards
            for i in range(x + 1, h, 1):
              if self.b[v][i] [1] != "一":
                print("有东西挡着你的棋子")
                return turn
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
        
        print("车不是这么挪的")
        return turn
         
        
      if self.b[v][h][1] == "马":
        if abs(x - h) == 2 and abs(y - v) == 1 or abs(y - v) == 2 and abs(x - h) == 1:
          if x - h == 2 and self.b[v][h + 1] == '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          if h - x == 2 and self.b[v][h - 1] == '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          if v - y == 2 and self.b[v - 1][h] == '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          if y - v == 2 and self.b[v + 1][h] == '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          print("蹩马腿了")
        print("马不是这么跳的")
        return turn
      
      
      if self.b[v][h][1] == "相":
        if abs(x - h) == 2 and abs(y - v) == 2 or abs(y - v) == 2 and abs(x - h) == 2:
          if x > h and y < v and self.b[v + 1][h - 1] == '一一':
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          if h > x and v > y and self.b[v - 1][h - 1] == '一一':
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          if h > x and v < y and self.b[v + 1][h - 1] == '一一':
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          if v < y and h < x and self.b[v + 1][h + 1] == '一一':
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
          print("塞象眼了")
        print("象不是这么飞的")
        return turn
      
          
      if self.b[v][h][1] == "炮":
        if x == h: #it is moving vertically
          obc = 0
          if y > v: #downwards
            for i in range(v + 1, y, 1):
              if self.b[i][x] [1] != "一":
                obc = obc + 1
              if obc > 2:
                print("炮不是这么打的")
                return turn
            if obc == 0 and self.b[y][x] == '一一' or obc == 1 and self.b[y][x] != '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          
          if v > y: #upwards
            for i in range(y + 1, v, 1):
              if self.b[i][x] [1] != "一":
                obc = obc + 1
              if obc > 2:
                print("炮不是这么打的")
                return turn
            if obc == 0 and self.b[y][x] == '一一' or obc == 1 and self.b[y][x] != '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
                
          
        if v == y: #horizontally
          obc = 0
          if x > h:
            for i in range(h + 1, x, 1): #rightwards
              if self.b[v][i] [1] != "一":
                obc = obc + 1
              if obc > 2:
                print("炮不是这么打的")
                return turn
            if obc == 0 and self.b[y][x] == '一一' or obc == 1 and self.b[y][x] != '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
          if x < h: #moving leftwards
            for i in range(x + 1, h, 1):
              if self.b[v][i] [1] != "一":
                obc = obc + 1
              if obc > 2:
                print("炮不是这么打的")
                return turn
            if obc == 0 and self.b[y][x] == '一一' or obc == 1 and self.b[y][x] != '一一':
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
        
        print("炮不是这么打的")
        return turn
      
      
      
      
      if self.b[v][h][1] == "兵":
        if self.b[v][h][0] == "黑" and y - v == 1 and x - h == 0:
          self.b[y][x]  = self.b[v][h] 
          self.b[v][h]  = "一一"
          if y == 5:
            self.b[y][x] = str(self.b[y][x][0]) + "卒"
          return turn + 1
        if self.b[v][h][0] == "红" and v - y == 1 and x - h == 0:
          self.b[y][x]  = self.b[v][h] 
          self.b[v][h]  = "一一"
          if y == 4:
            self.b[y][x] = str(self.b[y][x][0]) + "卒"
          return turn + 1
        print("兵不是这样走的")
        return turn
      if self.b[v][h][1] == "卒":
        if self.b[v][h][0] == "红":
          if abs(x - h) == 1 and v - y == 0 or v - y == 1 and x - h == 0:
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
        if self.b[v][h][0] == "黑":
          if abs(x - h) == 1 and v - y == 0 or y - v == 1 and x - h == 0:
            self.b[y][x]  = self.b[v][h] 
            self.b[v][h]  = "一一"
            return turn + 1
        print("卒不是这样走的")
        return turn
    
      if self.b[v][h][1] == "士":
        if self.b[v][h][0] == "黑":
          if v == 1 and h == 4:
            if y == 0 or y == 2:
              if x == 3 or x == 5:
                self.b[y][x]  = self.b[v][h] 
                self.b[v][h]  = "一一"
                return turn + 1
          if y == 1 and x == 4:
            if v == 0 or v == 2:
              if h == 3 or h == 5:
                self.b[y][x]  = self.b[v][h] 
                self.b[v][h]  = "一一"
                return turn + 1
        if self.b[v][h][0] == "红":
          if v == 8 and h == 4:
            if y == 7 or y == 9:
              if x == 3 or x == 5:
                self.b[y][x]  = self.b[v][h] 
                self.b[v][h]  = "一一"
                return turn + 1
          if y == 8 and x == 4:
            if v == 7 or v == 9:
              if h == 3 or h == 5:
                self.b[y][x]  = self.b[v][h] 
                self.b[v][h]  = "一一"
                return turn + 1
        print("士不是这么用的")
        return turn
      
            
      if self.b[v][h][1] == "帅":
        if 3 <= x <= 5:
          if abs(x - h) == 1 and y == v or abs(y - v) == 1 and x == h:
            if self.b[v][h][0] == "黑" and y <= 2 or self.b[v][h][0] == "红" and y >= 7:
              self.b[y][x]  = self.b[v][h] 
              self.b[v][h]  = "一一"
              return turn + 1
        print("帅不是这么走的")
        return turn
        
    
          
      
    #except:
    print("error")
    return turn
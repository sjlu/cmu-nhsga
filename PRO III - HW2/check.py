# -------------- CHECKING FOR POSSIBILITIES in HEIRARCHY ---------------
    # ------------ CHECKING 8 IN A ROW IN ALL WAYS ----------------
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
        
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1

        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):
            self.legal=1
            
    # ------------ CHECKING 7 IN ALL WAYS ------------
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]):
            self.legal=1
            
        if(self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
            
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1
            
        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):
            self.legal=1
        
        
    # -------------- CHECKING 6 IN ALL WAYS -----------
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):
            self.legal=1
            
    # ----------------- CHECKING 5 IN ALL WAYS ------------------
        
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):
            self.legal=1
   
    # ------------------- CHECKING 4 IN ALL WAYS ---------------------
    
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):
            self.legal=1
            
    # ---------------------- CHECKING 3 IN ALL WAYS ---------------------
        if(self.xGrid[oX][0].getName()[-1]==self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][1].getName()[-1]==self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][2].getName()[-1]==self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][3].getName()[-1]==self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][4].getName()[-1]==self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[oX][5].getName()[-1]==self.xGrid[oX][6].getName()[-1]==self.xGrid[oX][7].getName()[-1]):
            self.legal=1
        
        if(self.xGrid[tX][0].getName()[-1]==self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][1].getName()[-1]==self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][2].getName()[-1]==self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][3].getName()[-1]==self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][4].getName()[-1]==self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]):
            self.legal=1
        if(self.xGrid[tX][5].getName()[-1]==self.xGrid[tX][6].getName()[-1]==self.xGrid[tX][7].getName()[-1]):
            self.legal=1
      
        if(self.xGrid[0][oY].getName()[-1]==self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][oY].getName()[-1]==self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][oY].getName()[-1]==self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][oY].getName()[-1]==self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[4][oY].getName()[-1]==self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[5][oY].getName()[-1]==self.xGrid[6][oY].getName()[-1]==self.xGrid[7][oY].getName()[-1]):
            self.legal=1
        if(self.xGrid[0][tY].getName()[-1]==self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[1][tY].getName()[-1]==self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[2][tY].getName()[-1]==self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[3][tY].getName()[-1]==self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[4][tY].getName()[-1]==self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]):
            self.legal=1
        if(self.xGrid[5][tY].getName()[-1]==self.xGrid[6][tY].getName()[-1]==self.xGrid[7][tY].getName()[-1]):  
            self.legal=1
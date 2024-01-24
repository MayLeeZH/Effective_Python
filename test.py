def first_point(info):
    for i in range(len(info)):
        for j in range(len(info[0])):
            if (info[i][j] == '1'):
                return (i,j,0)

def recurse_find(info,point,path):
    global continueFlag
    path.append([point[0],point[1]])
    # Set this point is used
    info[point[0]][point[1]] = '0'
    # If this is first point of this polygon
    if(point[2] == 0):
        
        # Go east is first choice
        # If moving east, do not cross the boundary
        if(point[1]+1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
 
        # Go south east is second choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)

        # Go south is third choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)

    # If this point come from west
    elif(point[2] == 1):

        # Go northwest is first choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is first choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return
        
        # Go northeast is third choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0])and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return
        
        # Go east is forth choice
        # If moving east, do not cross the boundary

        if( point[1] + 1 < len(info[0])and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return
        
        # Go southeast is fivth choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0])and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return
        
        # Go south is sixth choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info)and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return
        
        # Go southwest is seventh choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return
        
            
    
    # If this point come from northwest
    elif(point[2] == 2):
        # Go north is first choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go northeast is second choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False 
            return

        # Go east is third choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go southeast is fourth choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go south is fifth choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go southwest is sixth choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is seventh choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return
        
    # If this point come from north
    elif(point[2] == 3):
        # Go northeast is first choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go east is second choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go southeast is third choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go south is fourth choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go southwest is fifth choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is sixth choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go northwest is seventh choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

    # If this point come from northeast
    elif(point[2] == 4):

        # Go east is first choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go southeast is second choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go south is third choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go southwest is fourth choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is fifth choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go northwest is sixth choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is seventh choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

    # If this point come from east
    elif(point[2] == 5):
        # Go southeast is first choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go south is second choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go southwest is third choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1] - 1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is fourth choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            retu

        # Go northwest is fifth choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is sixth choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go northeast is seventh choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

    # If this point come from southeast
    elif(point[2] == 6):
        # Go south is first choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go southwest is second choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is third choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go northwest is fourth choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is fifth choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go northeast is sixth choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go east is seventh choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

    # If this point come from south
    elif(point[2] == 7):
        # Go southwest is first choice
        # If moving southwest, do not cross the boundary
        if(point[0]+1 < len(info) and point[1]-1 >= 0 and info[point[0]+1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]-1,4)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go west is second choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go northwest is third choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is fourth choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go northeast is fifth choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go east is sixth choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go southeast is seventh choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

    # If this point come from southwest
    elif(point[2] == 8):
        # Go west is first choice
        # If moving west, do not cross the boundary
        if(point[1]-1 >= 0 and info[point[0]][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]-1,5)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go northwest is second choice
        # If moving northwest, do not cross the boundary
        if(point[0]-1 >= 0  and point[1] - 1 >= 0 and info[point[0]-1][point[1]-1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]-1,6)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]-1 == start_point[1]):
            continueFlag = False
            return

        # Go north is third choice
        # If moving north, do not cross the boundary
        if(point[0] - 1 >= 0 and info[point[0]-1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1],7)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return

        # Go northeast is fourth choice
        # If moving northeast, do not cross the boundary
        if( point[0] - 1 >= 0  and point[1] + 1 < len(info[0]) and info[point[0]-1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]-1,point[1]+1,8)
            recurse_find(info,newpoint,path)
        elif(point[0]-1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go east is fifth choice
        # If moving east, do not cross the boundary
        if( point[1] + 1 < len(info[0]) and info[point[0]][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0],point[1]+1,1)
            recurse_find(info,newpoint,path)
        elif(point[0] == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go southeast is sixth choice
        # If moving southeast, do not cross the boundary
        if( point[0]+1 < len(info) and point[1]+1 < len(info[0]) and info[point[0]+1][point[1]+1] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1]+1,2)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1]+1 == start_point[1]):
            continueFlag = False
            return

        # Go south is seventh choice
        # If moving south, do not cross the boundary
        if(point[0]+1 < len(info) and info[point[0]+1][point[1]] == '1' and continueFlag == True):
            newpoint = (point[0]+1,point[1],3)
            recurse_find(info,newpoint,path)
        elif(point[0]+1 == start_point[0] and point[1] == start_point[1]):
            continueFlag = False
            return
    
    info[point[0]][point[1]] = '1'
    if(continueFlag == True):
        path.pop()
    return

def process(info,path):
    recurse_find(info, start_point,path)

def get_polygons(info):

    sum_polys = 0
    global continueFlag
    global start_point
    path = []
    start_point = []
    continueFlag = True
    # 2 stand for first polygongs, since 1 and 0 are occupied

    path_list = []
    poly_nums = 2
    path = []
    continueFlag = True
    start_point = first_point(info)

    old_info = info
    # for i in info:

    process(info,path)

    # change point in old_info
    # for i in info:

    for i in range(len(info)):
        for j in range(len(info[0])):
            if([i,j] in path):
                old_info[i][j] = str(poly_nums)
    info = old_info


    while(len(path) != 0):
        sum_polys = sum_polys + 1
        path_list.append(path)
        # If a new Ploygon can be found
        poly_nums = poly_nums + 1
        path = []
        start_point = first_point(info)

        old_info = info
        continueFlag = True
        if(start_point == None):
            break

        process(info,path)


        # change point in old_info
        for i in range(len(info)):
            for j in range(len(info[0])):
                if([i,j] in path):
                    old_info[i][j] = str(poly_nums)
        info = old_info

    for i in range(len(info)):
        for j in range(len(info[0])):
            if(info[i][j] == '1'):
                # print('no')
                raise PolygonsError('Cannot get polygons as expected.')
    return sum_polys

def get_perimeter(origin_path):
    path = copy.deepcopy(origin_path)
    ver_hor_line_num = 0
    diagonal_num = 0
    path.append(path[0])
    for i in range(len(path)):
        if(i + 1 == len(path)):
            break
        # vertical or horizontal line
        if( abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) == 1):
            ver_hor_line_num = ver_hor_line_num + 1
        # diagonal line
        if( abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) == 2):
            diagonal_num = diagonal_num + 1

    # retrun string
    if(diagonal_num == 0 and ver_hor_line_num != 0 ):
        perimeter = str(format( ver_hor_line_num * 0.4 ,'.1f'))
    elif(diagonal_num != 0 and ver_hor_line_num == 0):
        perimeter = str(diagonal_num)+"*sqrt(.32)"
    else:
        perimeter = str( format(ver_hor_line_num * 0.4 ,'.1f'))+" + " + str(diagonal_num)+"*sqrt(.32)"
    return perimeter
    # print(ver_hor_line_num)
    # print(diagonal_num)

def get_area(path):
    area = 0
    next = path[-1]
    for current in path:
        area += next[0] * current[1] - next[1] * current[0]
        next = current
    return format(abs(area / 2) * 0.16 ,'.2f' )

def judge_convex(origin_path):
    path = copy.deepcopy(origin_path)
    path.append(path[0])
    path.append(path[1])
    for i in range(0,len(path)-2):
        cross =  (path[i+1][0] - path[i][0]) * (path[i+2][1] - path[i][1]) - (path[i+1][1] - path[i][1]) * (path[i+2][0] - path[i][0])
        if(i == 0):
            first_cross = cross
        else:
            if ((cross > 0) != (first_cross>0)):
                return 'no'
    return 'yes'

def get_nbOfInvariantRotations(points):
    n = len(points)
    angles = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        magnitude1 = sqrt( pow((p1[0] - p2[0]),2)+ pow((p1[1] - p2[1]),2) )
        magnitude2 = sqrt( pow((p2[0] - p3[0]),2)+ pow((p2[1] - p3[1]),2) )
        angle = acos(dot_product / (magnitude1 * magnitude2))
        angles.append(angle)
    # rotate 0 or 360 always work
    invariant_rotations = 1 
    for i in range(1, n):
        if angles[i:] + angles[:i] == angles:
            invariant_rotations += 1

    return str(invariant_rotations)

def get_depth(path,info,poly_num):

    # To avoid misjudgment caused by passing through vertices, it is necessary to judge in three directions simultaneously.

    current_num = str(poly_num)
    depth_w =0
    depth_n =0
    depth_e =0

    # print(path[0])
    # Choose test point
    x = path[0][0]
    y = path[0][1]
    cross_dict_w = {}

    # Go west
    while(y > 0):
        y = y - 1
        if(info[x][y] != current_num and info[x][y] != '0' and info[x][y] != '1'):
            if(info[x][y] in cross_dict_w.keys()):
                cross_dict_w[info[x][y]] = cross_dict_w[info[x][y]]+1
            else:
                cross_dict_w[info[x][y]] = 1
    # for key, value in cross_dict_w.items():
    #     if(value % 2 != 0):
    #         depth_w = depth_w+1

    key_w = set(cross_dict_w.keys())
    # print(cross_dict_w)

    # Reset
    x = path[0][0]
    y = path[0][1]

    cross_dict_n = {}

    # Go north
    while(x > 0):
        x = x - 1
        if(info[x][y] != current_num and info[x][y] != '0' and info[x][y] != '1'):
            if(info[x][y] in cross_dict_n.keys()):
                cross_dict_n[info[x][y]] = cross_dict_n[info[x][y]]+1
            else:
                cross_dict_n[info[x][y]] = 1

    # for key, value in cross_dict_n.items():
    #     if(value % 2 != 0):
    #         depth_n = depth_n+1

    key_n = set(cross_dict_n.keys())
    # print(cross_dict_n)

    # Reset
    x = path[0][0]
    y = path[0][1]

    cross_dict_e = {}

    # Go east
    y = y + 1
    while(y < len(info[0])):
        if(info[x][y] != current_num and info[x][y] != '0' and info[x][y] != '1'):
            if(info[x][y] in cross_dict_e.keys()):
                cross_dict_e[info[x][y]] = cross_dict_e[info[x][y]]+1
            else:
                cross_dict_e[info[x][y]] = 1
        y = y + 1

    key_e = set(cross_dict_e.keys())
    # print(cross_dict_e)

    # Go south
    x = path[0][0]
    y = path[0][1]

    cross_dict_s = {}
    x = x + 1
    while(x < len(info)):
        if(info[x][y] != current_num and info[x][y] != '0' and info[x][y] != '1'):
            if(info[x][y] in cross_dict_s.keys()):
                cross_dict_s[info[x][y]] = cross_dict_s[info[x][y]]+1
            else:
                cross_dict_s[info[x][y]] = 1
        x = x + 1

    key_s = set(cross_dict_s.keys())
    # print(cross_dict_s)


    common_keys = key_w.intersection(key_n,key_e,key_s)
    # print(common_keys)

    depth = 0
    for k in common_keys:

        if(cross_dict_w[k] % 2 == 1):
            depth = depth + 1
            continue
        elif(cross_dict_n[k] % 2 == 1):
            depth = depth + 1
            continue
        elif(cross_dict_e[k] % 2 == 1):
            depth = depth + 1
            continue
        elif(cross_dict_s[k] % 2 == 1):
            depth = depth + 1
            continue
    
    # print(depth)



    return depth

def print_information(info,poly_num,path,result_list):
    print("Polygon " + str(poly_num - 1) +":")
    print("    Perimeter: "+get_perimeter(path))
    area = get_area(path)

    print("    Area: "+str(area))
    print("    Convex: "+judge_convex(path))
    print("    Nb of invariant rotations: " + get_nbOfInvariantRotations(path))
    depth = get_depth(path,info,poly_num)
    print("    Depth: " + str(depth))
    # get_depth(path,info,poly_num)
    # for i in info:
    #     print(i) 

    # Add area to suppert self.display()
    path.append(area)
    result_list[depth].append(path)

def process_information(info,poly_num,path,result_list):

    area = get_area(path)
    depth = get_depth(path,info,poly_num)
    # get_depth(path,info,poly_num)
    # for i in info:
    #     print(i) 

    # Add area to suppert self.display()
    path.append(area)
    result_list[depth].append(path)




def get_polygons_analyse_noOutput(info,sum_poly):
    result_list = [[]for i in range(sum_poly)]
    global continueFlag
    global start_point
    path = []
    start_point = []
    continueFlag = True
    # 2 stand for first polygongs, since 1 and 0 are occupied

    path_list = []
    poly_nums = 2
    path = []
    continueFlag = True
    start_point = first_point(info)

    old_info = info

    process(info,path)

    for i in range(len(info)):
        for j in range(len(info[0])):
            if([i,j] in path):
                old_info[i][j] = str(poly_nums)
    info = old_info

    while(len(path) != 0):

        # Get polygon's information on the fly
        process_information(info,poly_nums,path,result_list)
        # If a new Ploygon can be found
        poly_nums = poly_nums + 1
        path = []
        start_point = first_point(info)
        old_info = info
        continueFlag = True
        if(start_point == None):
            break

        process(info,path)

        # change point in old_info
        for i in range(len(info)):
            for j in range(len(info[0])):
                if([i,j] in path):
                    old_info[i][j] = str(poly_nums)
        info = old_info

    for i in range(len(info)):
        for j in range(len(info[0])):
            if(info[i][j] == '1'):
                # print('no')
                raise PolygonsError('Cannot get polygons as expected.')
    return result_list

def get_polygons_analyse(info,sum_poly):
    result_list = [[]for i in range(sum_poly)]
    global continueFlag
    global start_point
    path = []
    start_point = []
    continueFlag = True
    # 2 stand for first polygongs, since 1 and 0 are occupied

    path_list = []
    poly_nums = 2
    path = []
    continueFlag = True
    start_point = first_point(info)

    old_info = info

    process(info,path)

    for i in range(len(info)):
        for j in range(len(info[0])):
            if([i,j] in path):
                old_info[i][j] = str(poly_nums)
    info = old_info

    while(len(path) != 0):

        # Get polygon's information on the fly
        print_information(info,poly_nums,path,result_list)
        # If a new Ploygon can be found
        poly_nums = poly_nums + 1
        path = []
        start_point = first_point(info)
        old_info = info
        continueFlag = True
        if(start_point == None):
            break

        process(info,path)

        # change point in old_info
        for i in range(len(info)):
            for j in range(len(info[0])):
                if([i,j] in path):
                    old_info[i][j] = str(poly_nums)
        info = old_info

    for i in range(len(info)):
        for j in range(len(info[0])):
            if(info[i][j] == '1'):
                # print('no')
                raise PolygonsError('Cannot get polygons as expected.')
    return result_list

class PolygonsError(Exception):
    pass
class Polygons:
    def __init__(self,filename):
        self.filename = filename
        self.info = []
        try:
            with open (filename,"r",encoding= 'utf-8') as f:
                height = 0
                width = 0
                data = f.readlines()
                for line in data:
                    line_info = []
                    line = line.replace(' ','')
                    if (line == '\n'):
                        continue
                    height = height + 1
                    for point in line:
                        if (point != '\n'):
                            width = width + 1
                            if(point != "1" and point != '0'):
                                raise PolygonsError('Incorrect input.')
                            line_info.append(point)

                    if(width <2 or width >50):
                        raise PolygonsError('Incorrect input.')
                    self.info.append(line_info)
                    width = 0
                if(height < 2 or height > 50):
                    raise PolygonsError('Incorrect input.')
            
                test_width = len(self.info[0])
                # If its lines of digits do not contain the same number of digits
                for line in self.info:
                    if(len(line) != test_width):
                        raise PolygonsError('Incorrect input.')


            info = copy.deepcopy(self.info)
            self.sum_poly = get_polygons(info)
        except PolygonsError:
            print(traceback.format_exc(),end = '')
        self.result_list = []
    def analyse(self):
        info = copy.deepcopy(self.info)
        self.result_list = get_polygons_analyse(info,self.sum_poly)

    def analyse_noOutput(self):
        info = copy.deepcopy(self.info)
        self.result_list = get_polygons_analyse_noOutput(info,self.sum_poly)


    def display(self):


        height = len(self.info)
        width = len(self.info[0])
        # print(len(self.result_list))
        # print(self.sum_poly)
        output_filename = self.filename[:-4] + '.tex'
        with open(output_filename,'w') as f:
            self.analyse_noOutput()
            # Fixed part
            f.write('\documentclass[10pt]{article}\n')
            f.write('\\usepackage{tikz}\n')
            f.write('\\usepackage[margin=0cm]{geometry}\n')
            f.write('\\pagestyle{empty}\n')
            f.write('\n')
            f.write('\\begin{document}\n')
            f.write('\n')
            f.write('\\vspace*{\\fill}\n')
            f.write('\\begin{center}\n')
            f.write('\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]\n')
            f.write('\\draw[ultra thick] (0, 0) -- ('+str(width-1)+', 0) -- ('+str(width-1)+', '+str(height-1)+') -- (0, '+str(height-1)+') -- cycle;\n')
            f.write('\n')

            # Find max area and min area
            max_area = 0
            min_area = len(self.info) * len(self.info[0])
            for i in range(len(self.result_list)):
                if(len(self.result_list[i]) != 0):
                    for j in self.result_list[i]:
                        if(float(j[-1]) > max_area):
                            max_area = float(j[-1])
                        if(float(j[-1]) < min_area):
                            min_area = float(j[-1])

            for i in range(len(self.result_list)):
                if(len(self.result_list[i]) != 0):
                    # print('Depth '+str(i)+'\n')
                    f.write('% Depth '+str(i)+'\n')
                    for j in range(len(self.result_list[i])):
                        path = self.result_list[i][j]
                        color_parameter_ = (max_area - float(path[-1])) / (max_area- min_area) * 100
                        # print(color_parameter_,end=' |')
                        color_parameter = Decimal(str(color_parameter_)).quantize(Decimal("0."), rounding = "ROUND_HALF_UP")
                        f.write('\\filldraw[fill=orange!'+str(color_parameter)+'!yellow]')

                        # Remove area 
                        path.pop(-1)
                        # Append start point to test last line
                        path.append(path[0])

                        # If direction was changed at some points, print those points
                        lenth = len(path)
                        k_old = 123456789.123445667
                        k = 123124213412.13414113451
                        for index in range(lenth):
                            
                            # print(index)
                            if(index + 1 == lenth):
                                break

                            if(path[index][1] - path[index+1][1] != 0):
                                k = (path[index][0] - path[index+1][0])/(path[index][1] - path[index+1][1])
                            else:
                                k = inf
                            if(k  != k_old):
                                # print(path[index],end = ' ')
                                f.write(' ('+str(path[index][1])+', '+str(path[index][0])+')'+ ' --')
                                k_old = k
                        f.write(' cycle;\n')

                        # print()
                        # x->y y->x

            f.write('\\end{tikzpicture}\n')
            f.write('\\end{center}\n')
            f.write('\\vspace*{\\fill}\n')
            f.write('\n')
            f.write('\\end{document}\n')

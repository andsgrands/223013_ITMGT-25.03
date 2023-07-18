#!/usr/bin/env python
# coding: utf-8

# In[1]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member in social_graph[to_member]["following"]:
        if to_member in social_graph[from_member]["following"]:
            relationship = "friends"
            
        else:
            relationship = "followed by"
            
    elif to_member in social_graph[from_member]["following"]:
        relationship = "follower"
        
    else:
        relationship = "no relationship"
        
    return relationship


# In[2]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    winner = ""
    
    #HORIZONTAL
    counter_h = 0
    
    for x in range(len(board)):
        h_list = []
        
        for y in range(len(board)):
            h_list.append(board[x][y])
        
        if (h_list.count("O") == len(board)) or (h_list.count("X") == len(board)):
            win_h = h_list.pop()
            counter_h = counter_h+1
            
        else:
            h_list = []
    
    if counter_h != 0:
        winner = win_h
        
    else:
        #VERTICAL
        counter_v = 0
        
        for y in range(len(board)):
            v_list = []
            
            for x in range(len(board)):
                v_list.append(board[x][y])
        
            if (v_list.count("O") == len(board)) or (v_list.count("X") == len(board)):
                win_v = v_list.pop()
                counter_v = counter_v+1
            
        if counter_v != 0:
            winner = win_v
        
        else:
            #DIAGONAL1
            d1_list = []
            
            for x in range(len(board)):
                y = x
                d1_list.append(board[x][y])
            
            if (d1_list.count("O") == len(board)) or (d1_list.count("X") == len(board)):
                winner = d1_list.pop()
                
            else:
                #DIAGONAL2
                counter_d2 = 0
                d2_list = []
                
                for x in range(len(board)):
                    for y in range(len(board)):
                        if x+y == (len(board) - 1):
                            d2_list.append(board[x][y])
                    
                    if (d2_list.count("O") == len(board)) or (d2_list.count("X") == len(board)):
                        win_d2 = d2_list.pop()
                        counter_d2 = counter_d2+1
                        
                    else:
                        continue
                        
                if counter_d2 != 0:
                    winner = win_d2
                    
                else:
                    winner = "NO WINNER"
    return winner


# In[39]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    time = 0
    start = False
    stop = False
    
    while stop == False:
        for key, value in route_map.items():
            if key[0] == first_stop or start == True:
                start = True
                
                if key[0] == second_stop:
                    stop = True
                    
            if start == True and stop == False:
                time = time + value['travel_time_mins']
                
                if key[1] == second_stop:
                    stop = True
        
    return time


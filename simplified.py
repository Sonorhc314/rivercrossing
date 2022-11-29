### Your code here!
# ...

game_list = []
class Node:
    def __init__(self, m_wrong_side, c_wrong_side, boat_wrong_side):
        self.state = [m_wrong_side, c_wrong_side, boat_wrong_side]
        self.is_state()
        game_list.append(self)
    
    def is_goal_state(self):
        if (self.state[0] == 0 and self.state[1] == 0):
            return 1
        return 0
    
    def is_state(self):
        print(f"<{self.state[0], self.state[1], self.state[2]}>")
        return f"<{self.state[0], self.state[1], self.state[2]}>"
    
    def get_child_node(self):
        Node(self.state[0]-1,self.state[1]-1,1)
        Node(self.state[0],self.state[1]-1,1)
        Node(self.state[0]-1,self.state[1],1)
    
    def is_valid_state(self):
        if self.state[0]<self.state[1]:
            return 0
        return 1
    

# first = Node(3,3,1)
# a = first.get_child_node([1,1])
# b = a.get_child_node([1,1])

# use queue of nodes to find solution


class Game:
    def __init__(self):
        self.initial_node = Node(m_wrong_side=3, c_wrong_side=3, boat_wrong_side=1)
        self.i=0
    def breadth_first_search(self):
        while True:
            if self.initial_node.is_goal_state():
                print(f"Solved with node {game_list[0].is_state()} on step {self.i}")
                break
            self.i+=1
            game_list.pop(0)
            self.initial_node.get_child_node()
            self.initial_node = game_list[0]
            
my_game = Game()
my_game.breadth_first_search()
            
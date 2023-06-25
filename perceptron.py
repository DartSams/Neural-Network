import random
import pygame

class Perceptron:
    def __init__(self):
        self.weights = []
        self.learning_rate = 0.1 #how much to correct when a error is made
        self.threshold = 0.2 #key to classification and activation function

        for i in range(2): #assign wieghts a random value between -1 and 1
            self.weights.append(random.uniform(-1,1))

    def sign(self,weighted_sum): #activation function
        if weighted_sum >= self.threshold:
            return 1
        else:
            return -1

    def guess(self,inputs:list):
        weighted_sum = 0
        for i in range(len(self.weights)): #adds together all the inputs multiplied by the weights
            weighted_sum += self.weights[i] * inputs[i]

        output = self.sign(weighted_sum)
        return output
    
    def train(self,inputs,target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)): #changes the weights if guess is wrong which is supervised learning
            self.weights[i] += error * inputs[i] *self.learning_rate 
    

# p = Perceptron()
# print(f"Inputs are {inputs}")
# print(f"Weights are {p.weights}")
# print(f"Output is {p.guess(inputs)}")
# print(p.guess(inputs))


class Point: #class for each dot
    def __init__(self,x,y,label,color):
        self.x = x
        self.y = y
        self.label = label
        self.color = color




pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
width,height = (500,500)
win = pygame.display.set_mode((width,height))
dots_limit = 17656 #number of dots allowed
border_thickness = 5 #thickness of border seperator
dots_lst = [] #list of dots

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

for i in range(dots_limit): #creates a limited amount of dots on the screen
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    if x >= width//2 + border_thickness: #on right side
        d = Point(x,y,1,RED)
    elif x < width//2: #on the left side
        d = Point(x,y,-1,BLUE)

    dots_lst.append(d)

p = Perceptron()
run = True
while run:
    # for i in dots_lst:
    #     inputs = [i.x / width, i.y / height]  # Normalize inputs
    #     p.train(inputs, i.label)

    #     guess = p.guess(inputs)
    #     # print(guess)
    #     if guess == i.label: #if neural network guesses correct changes color of dot to green
    #         i.color = GREEN
        
    #     else:
    #         i.color = RED
            

        # text_surface = my_font.render(str(guess), False, WHITE) #draws the label of the dot to the screen used for seeing what the current guess is
        # win.blit(text_surface,(i.x,i.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.key.get_pressed()[pygame.K_SPACE]: #trains when spacebar is pressed
            for i in dots_lst:
                inputs = [i.x / width, i.y / height]  # Normalize inputs
                p.train(inputs, i.label)

                guess = p.guess(inputs)
                # print(guess)
                if guess == i.label: #if neural network guesses correct changes color of dot to green
                    i.color = GREEN
                
                else:
                    i.color = RED
                    

                # text_surface = my_font.render(str(guess), False, WHITE) #draws the label of the dot to the screen used for seeing what the current guess is
                # win.blit(text_surface,(i.x,i.y))
    
    pygame.display.flip()
    pygame.draw.line(win,WHITE,(width//2,0),(width//2,height),border_thickness) #draw border line if dots on left the -1 if on right its 1

    for i in dots_lst:
        pygame.draw.circle(win,i.color,(i.x,i.y),10)  #draws all dots to screen


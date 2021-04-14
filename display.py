import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from constants import RGB,Faces,Direction



class Display:
    def __init__(self):
        self.gap = 0.09
        self.cube_size = 2
        self.xrot = self.yrot = 0
        pygame.init()
        self.w = 800
        self.h = 600
        pygame.display.set_mode((self.w, self.h), DOUBLEBUF | OPENGL)
        glutInitDisplayMode( GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        gluPerspective(45, (self.w / self.h), 0.1, 50.0)
        # glTranslatef(-1.5, -2.0, -10)
        glEnable(GL_DEPTH_TEST)


    def display(self,faces):
        """
                This method displays the cube and has to be called in a loop so it is always displaying
                :param   :
                :param   : cube -> the cube lol
                :return: void
                """
        self.faces = faces
        # n = len(self.faces[0][1])

        self.n = 3


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        #gluLookAt(10, 3, 0, 0, 0, 0, 0, 1, 0)
        # glTranslatef(0.0, 0.0, -25.0 )
        for i in range(self.n):
            for j in range(self.n):
                # for k in range(n):
                    self.set_for_display(i,j)

        glFlush()
        glutSwapBuffers()
        pass
    def set_for_display(self,i,j):
        #TODO rotations aren't good
        glPushMatrix()

        x = j
        y = i
        z = 2
        # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap)/////self.n-1+self.gap
        (-x + 1) * self.cube_size - x * self.gap + self.gap
        # front face : red
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot,1,0,0)
        glRotate(self.yrot,0,1,0)
        glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap - self.gap)
        color = RGB.rgb.get(self.faces[0][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size/2,self.cube_size/2,self.cube_size/2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)

        glEnd()

        # # back face : orange
        # glLoadIdentity()
        # glTranslatef(0, 0, -25.0)
        # glRotate(self.xrot,1,0,0)
        # glRotate(self.yrot,0,1,0)
        # glTranslatef((-x + 1) * self.cube_size - x * self.gap, (-y + 1) * self.cube_size - y * self.gap, z *self.n-1 )
        # # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, -z)
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, -((z - 1) * self.cube_size + z * self.gap - self.gap))
        # glTranslatef(0,0,-(self.n-1+self.gap*2) * 2) #x2 because i have to bring it to the center from the previous translate and then the same size
        color = RGB.rgb.get(self.faces[2][i][-j + self.n-1])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        # bottom face: green
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        #n-1 = has to start here the front/back face ends * la grandeur du cube
        #(self.n-1) * self.gap il faut ajuster le gap
        #enlever la taille du cube pour une raison mathematique que j'ignore.....
        x_to_translate = (self.n-1) * self.cube_size + (self.n-1) * self.gap - self.cube_size
        z_to_translate = (-x + 1) * self.cube_size - x * self.gap + self.gap
        glTranslatef( x_to_translate,(-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[1][i][j])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glEnd()

        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)

        #
        # top face: blue
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        x_to_translate = (self.n - 1) * self.cube_size +  - self.cube_size
        glTranslatef(-x_to_translate, (-y + 1) * self.cube_size - y * self.gap, z_to_translate)
        color = RGB.rgb.get(self.faces[3][i][-j + self.n-1])
        glColor(color)
        glBegin(GL_QUADS)

        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)


        # glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()
        #
        # # right face: yellow
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        y_to_translate = (self.n - 1) * self.cube_size - self.cube_size
        x_to_translate = (x - 1) * self.cube_size + x * self.gap - self.gap * 2
        z_to_translate = (y - 1) * self.cube_size + y * self.gap - self.gap

        glTranslatef(-x_to_translate, y_to_translate, -z_to_translate)
        color = RGB.rgb.get(self.faces[4][j][i])
        glColor(color)
        glBegin(GL_QUADS)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)



        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        glEnd()
        #

        #
        # left face: white
        glLoadIdentity()
        glTranslatef(0, 0, -25.0)
        glRotate(self.xrot, 1, 0, 0)
        glRotate(self.yrot, 0, 1, 0)
        # glTranslatef((-x + 1) * self.cube_size - x * self.gap, (y - 1) * self.cube_size + y * self.gap, 0)
        # glTranslatef((x - 1) * self.cube_size + x * self.gap, (-y + 1) * self.cube_size - y * self.gap, (z - 1) * self.cube_size + z * self.gap)
        y_to_translate =  (self.n - 1) * self.cube_size - self.cube_size + self.gap*2
        glTranslatef(-x_to_translate, -y_to_translate, -z_to_translate)
        color = RGB.rgb.get(self.faces[5][-j + self.n-1][i])
        glColor(color)
        glBegin(GL_QUADS)

        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        glVertex3f(self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)

        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, self.cube_size / 2, -self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, self.cube_size / 2)
        # glVertex3f(-self.cube_size / 2, -self.cube_size / 2, -self.cube_size / 2)
        glEnd()

        glPopMatrix()

    def rotate(self,rot,angle):
        if angle == 'x':
            self.yrot += rot
        else :
            self.xrot += rot

    # def special_keys(self,key,x,y):
    #     if key == GLUT_KEY_DOWN:
    #         self.xrot += 5
    #     elif key == GLUT_KEY_RIGHT:
    #         self.yrot += 5
    #     glutPostRedisplay()
    # def keys(self, key, x,y):
    #     if key == 27:
    #         print("baby break a sweat, dont get tired yet")
    #         pygame.quit()
    #         quit()

    def update_move(self, move):
        """
                This method is called after a move every time so it can update the displaying cube
                :param move: is a tuple variable, it contains the face to rotate and the direction to rotate
                :return: void
                """


        pass

    def update_hints(self,hints):
        """
                This method update the possible hints to a solution
                :param hints: a list of moves that can be made from a particular state
                :return: void
                """
        pass

    def redisplay(self):
        glViewport(0, 0, self.w, self.h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.w/self.h,1.0,1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def display_pygame(self):
        pass
    def move(self, face, direction):
        """
        This method causes a 90 degree rotation of a specific face
        of the cube (this is what we have defined as a "move")
        :param face: the face to be rotated
        :param direction: the direction in which to rotate the given face
        :return: void
        """

        # top: arr[x,0,:]
        # bottom: arr[x,2,:]
        # right side: arr[x,:,2]
        # left side: arr[x,:,0]

        # for CCW rotations, need to flip whenever moving the bottom
        # of one 3x3 array to the right side of another, or when moving
        # the top of one to the left side of another
        print(self.faces)
        if direction == Direction.CCW:
            # CCW 90 degree rotation

            if face == Faces.RED:
                # red face

                self.faces[0, :, :] = np.rot90(self.faces[0, :, :])
                temp1 = self.faces[1, :, 0].copy()
                temp2 = np.flip(self.faces[4, 2, :]).copy()
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[3, :, 2].copy()
                self.faces[3, :, 2] = temp2
                temp2 = np.flip(self.faces[5, 0, :]).copy()
                self.faces[5, 0, :] = temp1
                self.faces[1, :, 0] = temp2

            elif face == Faces.GREEN:
                # green face

                self.faces[1, :, :] = np.rot90(self.faces[1, :, :])
                temp1 = self.faces[2, :, 0].copy()
                temp2 = np.flip(self.faces[4, 2, :]).copy()
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[0, :, 2].copy()
                self.faces[0, :, 2] = temp2
                temp2 = np.flip(self.faces[5, 0, :]).copy()
                self.faces[5, 0, :] = temp1
                self.faces[2, :, 0] = temp2

            elif face == Faces.ORANGE:
                # orange face

                self.faces[2, :, :] = np.rot90(self.faces[2, :, :])
                temp1 = self.faces[3, :, 0].copy()
                temp2 = np.flip(self.faces[4, 2, :]).copy()
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[1, :, 2].copy()
                self.faces[1, :, 2] = temp2
                temp2 = np.flip(self.faces[5, 0, :]).copy()
                self.faces[5, 0, :] = temp1
                self.faces[3, :, 0] = temp2

            elif face == Faces.BLUE:
                # blue face

                self.faces[3, :, :] = np.rot90(self.faces[3, :, :])
                temp1 = self.faces[0, :, 0].copy()
                temp2 = np.flip(self.faces[4, 2, :]).copy()
                self.faces[4, 2, :] = temp1
                temp1 = self.faces[2, :, 2].copy()
                self.faces[2, :, 2] = temp2
                temp2 = np.flip(self.faces[5, 0, :]).copy()
                self.faces[5, 0, :] = temp1
                self.faces[0, :, 0] = temp2

            elif face == Faces.YELLOW:
                # yellow face

                self.faces[4, :, :] = np.rot90(self.faces[4, :, :])
                temp1 = self.faces[2, :, 0].copy()
                temp2 = np.flip(self.faces[3, 2, :]).copy()
                self.faces[3, 2, :] = temp1
                temp1 = self.faces[0, :, 2].copy()
                self.faces[0, :, 2] = temp2
                temp2 = np.flip(self.faces[1, 0, :]).copy()
                self.faces[1, 0, :] = temp1
                self.faces[2, :, 0] = temp2

            elif face == Faces.WHITE:
                # white face

                self.faces[5, :, :] = np.rot90(self.faces[5, :, :])
                temp1 = self.faces[2, :, 0].copy()
                temp2 = np.flip(self.faces[1, 2, :]).copy()
                self.faces[1, 2, :] = temp1
                temp1 = self.faces[0, :, 2].copy()
                self.faces[0, :, 2] = temp2
                temp2 = np.flip(self.faces[3, 0, :]).copy()
                self.faces[3, 0, :] = temp1
                self.faces[2, :, 0] = temp2

        # for CW rotations, need to flip whenever moving the left side
        # of one 3x3 array to the top of another, or when moving
        # the right side of one to the bottom of another

        elif direction == Direction.CW:
            # CW 90 degree rotation

            # top: arr[x,0,:]
            # bottom: arr[x,2,:]
            # right side: arr[x,:,2]
            # left side: arr[x,:,0]

            if face == Faces.RED:
                self.faces[0, :, :] = np.rot90(self.faces[0, :, :], 3)
                temp1 = np.flip(self.faces[3, :, 2]).copy()
                temp2 = self.faces[4, 2, :].copy()
                self.faces[4, 2, :] = temp1
                temp1 = np.flip(self.faces[1, :, 0]).copy()
                self.faces[1, :, 0] = temp2
                temp2 = self.faces[5, 0, :].copy()
                self.faces[5, 0, :] = temp1
                self.faces[3, :, 2] = temp2

            elif face == Faces.GREEN:
                self.faces[1, :, :] = np.rot90(self.faces[1, :, :], 3)
                temp1 = np.flip(self.faces[0, :, 2]).copy()
                temp2 = self.faces[4, 2, :].copy()
                self.faces[4, 2, :] = temp1
                temp1 = np.flip(self.faces[2, :, 0]).copy()
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[5, 0, :].copy()
                self.faces[5, 0, :] = temp1
                self.faces[0, :, 2] = temp2

            elif face == Faces.ORANGE:
                self.faces[2, :, :] = np.rot90(self.faces[2, :, :], 3)
                temp1 = np.flip(self.faces[1, :, 2]).copy()
                temp2 = self.faces[4, 2, :].copy()
                self.faces[4, 2, :] = temp1
                temp1 = np.flip(self.faces[3, :, 0]).copy()
                self.faces[3, :, 0] = temp2
                temp2 = self.faces[5, 0, :].copy()
                self.faces[5, 0, :] = temp1
                self.faces[1, :, 2] = temp2

            elif face == Faces.BLUE:
                self.faces[3, :, :] = np.rot90(self.faces[3, :, :], 3)
                temp1 = np.flip(self.faces[2, :, 2]).copy()
                temp2 = self.faces[4, 2, :].copy()
                self.faces[4, 2, :] = temp1
                temp1 = np.flip(self.faces[0, :, 0]).copy()
                self.faces[0, :, 0] = temp2
                temp2 = self.faces[5, 0, :].copy()
                self.faces[5, 0, :] = temp1
                self.faces[2, :, 2] = temp2

            elif face == Faces.YELLOW:
                self.faces[4, :, :] = np.rot90(self.faces[4, :, :], 3)
                temp1 = np.flip(self.faces[0, :, 2]).copy()
                temp2 = self.faces[3, 2, :].copy()
                self.faces[3, 2, :] = temp1
                temp1 = np.flip(self.faces[2, :, 0]).copy()
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[1, 0, :].copy()
                self.faces[1, 0, :] = temp1
                self.faces[0, :, 2] = temp2

            elif face == Faces.WHITE:
                self.faces[5, :, :] = np.rot90(self.faces[5, :, :], 3)
                temp1 = np.flip(self.faces[0, :, 2]).copy()
                temp2 = self.faces[1, 2, :].copy()
                self.faces[1, 2, :] = temp1
                temp1 = np.flip(self.faces[2, :, 0]).copy()
                self.faces[2, :, 0] = temp2
                temp2 = self.faces[3, 0, :].copy()
                self.faces[3, 0, :] = temp1
                self.faces[0, :, 2] = temp2
            print(self.faces)
disp = Display()
n=3
faces = np.zeros([6, n, n], dtype=int)
i = 0
for colors in range(6):
    for r in range(n):
        for c in range(n):
            faces[colors,r,c] = i
    i+=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_DOWN]:
            disp.rotate(5,'y')
            disp.move(3,0)

        if keypress[pygame.K_RIGHT]:
            disp.rotate(5, 'x')

        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glutReshapeFunc(disp.redisplay())
        glutDialsFunc(disp.display(faces))
        # glutKeyboardFunc(disp.keys)
        # glutSpecialFunc(disp.special_keys)
        pygame.display.flip()
        # pygame.time.wait(500)
# displaysmt = Display()
# displaysmt.display()

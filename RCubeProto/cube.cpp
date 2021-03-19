#include <stdio.h>
#include <stdarg.h>
#include <math.h>
#include <GL/freeglut.h> 
#include <GL/glu.h> 

#include <iostream> 
#include <vector>

using namespace std;

// Ncdt Aranda Luisa, s28419
//
//controls:    
// ~*~ in the whole state ~*~ :   
// 4 - Rorate Left
// 6 - Rotate Right
// 8 - Rotate Up
// 2 - Rotate Down
// ----------------------------------------------------------
// Global Variables
// ----------------------------------------------------------
//GLfloat xrot, yrot, zrot; 
double xrot = 0;
double yrot = 0;
bool flag = false;
bool k_down = false;

//double zrot = 0;
// for the mouse mouvement
//float angle;
bool rotation_started;
int start_x = 0;// the old x
int start_y = 0;// the old y
int valid = 0;

// ----------------------------------------------------------
//My cube's settings N x N x N (N = cube_dimension)
// ----------------------------------------------------------
float gap = 0.2; //Gap between the cubies.
int cube_size = 2;
int cube_dimension = 2;
int tot_faces = 7; // for the sake of the indices N-1;
// ----------------------------------------------------------
//To id the face I want to rotate and the axis
// RED = 0
// ORANGE = 1
// BLUE = 2
// GREEN = 3
// WHITE = 4
// YELLOW = 5
// ----------------------------------------------------------

// ----------------------------------------------------------
//To id the cubes that i need to rotate
// ----------------------------------------------------------
int cubes_to_rotate = cube_dimension * cube_dimension; // i know i want to rotate this number of faces.
int cube_id = 0;
int cubes_id[4];
bool cubies[8];
bool change_perspective = false; // as a whole cube or to change a side
bool up = true; // by default will go to the top left cube part of the pocket cube.

typedef struct Rotate {
    //int id;
    float angle;
    int x_axis;
    int y_axis;
    int z_axis;
}Rotate;

Rotate rotations[8];
// ----------------------------------------------------------
//To id the axis is rotating
// ----------------------------------------------------------
//int axis_x = 1;
//int axis_y = 0;
//int axis_z = 0;

//
//typedef enum Face {
//    red_face, orange_face, blue_face, green_face, white_face, yellow_face
//} Face;



void setCube(int x, int y, int z);

void set_rotation(int cubeID, char axis, float angle);

void set_rotation(int cubeID, char axis, float angle) {
    rotations[cubeID].angle += angle;
    if (axis == 'x') {
        rotations[cubeID].x_axis = 1;
        rotations[cubeID].y_axis = 0;
        rotations[cubeID].z_axis = 0;
    }
    else if (axis == 'y') {
        rotations[cubeID].x_axis = 0;
        rotations[cubeID].y_axis = 1;
        rotations[cubeID].z_axis = 0;
    }
    else {
        rotations[cubeID].x_axis = 0;
        rotations[cubeID].y_axis = 0;
        rotations[cubeID].z_axis = 1;
    }

}

void keys(unsigned char key, int x, int y) {
    switch (key) {

    case 27:
        exit(0);
        break;
        // to coming and going from the whole perspective by clicking s or 5.

        // TODO implpement the general rotation with the numbers.
        // TODO implement the setting for the keyboard to be more generalize no matter what size the cube is.
        // for now, its for always 2x2x2 cube.

        //this case is to change from a whole state to a specific state. 
        // setting to start will be bottom left side of the cube for this 2x2x2. 
    case 's':
    case 'S':
    case '5':
        if (change_perspective == true) {
            change_perspective = false;

        }
        else {
            change_perspective = true;
            // since we change the perspective we change to a top square.
        }
        break;

    case '1':
    case 'z':
    case 'Z':
        if (change_perspective) { // to change perspective to the lower right case
            if (up) {
                up = false;
            }
            else {
                up = true; // go back to the upper left body by clicking twice in the 1 button or z
            }
            cout << up;
        }
        break;
        // ----------------------------------------------------------
        //case 2 : rotate vertically clockwise 
        //          if in the up : 0,1,2,3
        //         if in down : 4,5,6,7
        // ----------------------------------------------------------

    case '2': // rotate down
    case 'x':
    case 'X':
        if (change_perspective) { // means we want to move the 4 top squares 
            if (up) { // change point in the left corner
                for (int i = 0; i < cubes_to_rotate; i++) {
                    set_rotation(i, 'x', 90);
                }

            }
            else if (!up) { // lower right corner
                for (int i = tot_faces; i > cubes_to_rotate; i--) {

                    set_rotation(i, 'x', 90);
                }

            }
        }
        else {
            xrot += 5;
        }

        // ----------------------------------------------------------
        //case 8 : rotate vertically counter-clockwise
        //          if in the up : 0,1,2,3
        //         if in down : 4,5,6,7
        // ----------------------------------------------------------
        break;
    case'8': // rotate up
    case 'w':
    case 'W':
        if (change_perspective) {
            if (up) { // change point in the left corner
                for (int i = 0; i < cubes_to_rotate; i++) {
                    set_rotation(i, 'x', -90);
                }

            }
            else if (!up) { // lower right corner
                for (int i = 0; i < cubes_to_rotate; i++) {

                    set_rotation(7 - i, 'x', -90);
                }

            }
        }
        else {
            xrot -= 5;
        }
        break;

        // ----------------------------------------------------------
        //case 4 : rotate horizontally counter-clockwise
        //          if in the up : 2,3,6,7
        //         if in down : 0,1,4,5
        // ----------------------------------------------------------
    case '4': //rotate left
    case 'a':
    case 'A':
        int r;
        if (change_perspective) {
            if (up) { // change point in the left corner
                for (int i = 0; i <= tot_faces; i++) {
                    if (i % 4 == 2 % 4 || i % 4 == 3 % 4) {
                        set_rotation(i, 'y', -90);
                    }

                }

            }

            else if (!up) { // lower right corner
                for (int i = 4; i <= tot_faces; i++) {
                    r = i % 6;
                    set_rotation(r, 'y', -90);
                }

            }
        }
        else {
            yrot -= 5;
        }
        break;
        // ----------------------------------------------------------
        //case 6 : rotate horizontally clockwise
        //          if in the up : 2,3,6,7
        //         if in down : 0,1,4,5
        // ----------------------------------------------------------
    case '6': // rotate right
    case 'd':
    case 'D':
        if (change_perspective) {
            if (up) { // change point in the left corner
                for (int i = 0; i <= tot_faces; i++) {
                    if (i % 4 == 2 % 4 || i % 4 == 3 % 4) {
                        set_rotation(i, 'y', 90);
                    }

                }

            }

            else if (!up) { // lower right corner
                for (int i = 4; i <= tot_faces; i++) {
                    r = i % 6;
                    set_rotation(r, 'y', 90);
                }

            }
        }
        else {
            yrot += 5;
        }
        break;
    }

    glutPostRedisplay();
}


void resize(int width, int height) {
    //angle =0;
    //rotation_started = false;
    start_x = 0;
    start_y = 0;


    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f/*angle on the Y axis*/, (GLfloat)width / (GLfloat)height /* the aspect ratio of x to y ( width to height)*/, 1.0f/*znear*/, 1000.0f /*zfar*/);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

}


void specialkeys(int key, int x, int y) {
    switch (key) {
    case(GLUT_KEY_DOWN):
        xrot += 5;
        break;
    case(GLUT_KEY_UP):
        xrot -= 5;
        break;
    case(GLUT_KEY_RIGHT):
        yrot += 5;
        break;
    case(GLUT_KEY_LEFT):
        yrot -= 5;
        break;
    }
    glutPostRedisplay();
}


void setCube(int x, int y, int z) {


    glPushMatrix();
    // now i need to set the transformation so the cube can be divided into cubies. glTranslatef takes care of this
    // note that this method creates individual cubes

    glTranslatef((x - 1) * cube_size + x * gap, (y - 1) * cube_size + y * gap, (z - 1) * cube_size + z * gap);


    glRotatef(rotations[cube_id].angle, rotations[cube_id].x_axis, rotations[cube_id].y_axis, rotations[cube_id].z_axis);

    // front face : red 
    glColor3f(1, 0, 0);
    glBegin(GL_QUADS);
    glVertex3f(cube_size / 2, cube_size / 2, cube_size / 2);
    glVertex3f(-cube_size / 2, cube_size / 2, cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, cube_size / 2);
    glVertex3f(cube_size / 2, -cube_size / 2, cube_size / 2);
    glEnd();

    // back face : orange
    glColor3f(1, 176.0 / 255.0, 5.0 / 255.0);
    glBegin(GL_QUADS);
    glVertex3f(cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, -cube_size / 2);
    glVertex3f(cube_size / 2, -cube_size / 2, -cube_size / 2);
    glEnd();

    // top face : blue
    glColor3f(0, 0, 1);
    glBegin(GL_QUADS);
    glVertex3f(cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, cube_size / 2, cube_size / 2);
    glVertex3f(cube_size / 2, cube_size / 2, cube_size / 2);
    glEnd();

    // bottom face : green
    glColor3f(0, 1, 0);
    glBegin(GL_QUADS);
    glVertex3f(cube_size / 2, -cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, cube_size / 2);
    glVertex3f(cube_size / 2, -cube_size / 2, cube_size / 2);
    glEnd();

    // left face : white
    glColor3f(1, 1, 1);
    glBegin(GL_QUADS);
    glVertex3f(-cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(-cube_size / 2, cube_size / 2, cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, cube_size / 2);
    glVertex3f(-cube_size / 2, -cube_size / 2, -cube_size / 2);
    glEnd();

    // right face : yellow
    glColor3f(1, 1, 0);
    glBegin(GL_QUADS);
    glVertex3f(cube_size / 2, cube_size / 2, -cube_size / 2);
    glVertex3f(cube_size / 2, cube_size / 2, cube_size / 2);
    glVertex3f(cube_size / 2, -cube_size / 2, cube_size / 2);
    glVertex3f(cube_size / 2, -cube_size / 2, -cube_size / 2);
    glEnd();

    glPopMatrix();

    cube_id++; // id the cube TODO not sure about this location
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    //gluLookAt(10,3,0,0,0,0,0,1,0);
    glTranslatef(0.0f, 0.0f, -25.0f);
    //Rotate when user changes the xrot,yrot,zrot
    glRotatef(xrot, 1.0f, 0.0f, 0.0f);
    glRotatef(yrot, 0.0f, 1.0f, 0.0f);

    for (int i = 0; i < cube_dimension; i++) {
        for (int j = 0; j < cube_dimension; j++) {
            for (int k = 0; k < cube_dimension; k++) {
                setCube(i, j, k);
            }
        }
    }
    cube_id = 0; // reset count here
    glFlush();
    glutSwapBuffers();
}


////the mouse movements
void mouse(int button, int state, int x, int y) {

    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        valid = 1;
        start_x = x - yrot;
        start_y = -y + xrot;

    }
    else {
        valid = 0;
    }

}

void motion(int x, int y) {
    if (valid == 1) {
        yrot = (-start_x + x);
        xrot = (start_y + y);
        glutPostRedisplay();
    }
}

//
//the key movements


bool init()
{
    glClearColor(0, 0, 0, 0.0f);
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LEQUAL);
    glClearDepth(1.0f);

    return true;
}



int main(int argc, char* argv[]) {

    glutInit(&argc, argv);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(10, 10);

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("A pocket cube");

    glEnable(GL_DEPTH_TEST);

    glutReshapeFunc(resize);
    glutDisplayFunc(display);
    glutKeyboardFunc(keys);
    glutSpecialFunc(specialkeys);
    glutMouseFunc(mouse);
    glutMotionFunc(motion);

    init();

    glutMainLoop();
    return 0;
}







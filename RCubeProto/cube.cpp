#include <GL/freeglut.h> #include <GL/glu.h> 

#include <iostream> 

GLfloat xrot, yrot, zrot;

void resize(int width, int height) {
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity();   
    gluPerspective(60.0f/*angle on the Y axis*/, (GLfloat)width / (GLfloat)height /* the aspect ratio of x to y ( width to height)*/ , 1.0f/*znear*/, 1000.0f /*zfar*/); 

    glMatrixMode(GL_MODELVIEW);  
    glLoadIdentity();

    glEnable(GL_DEPTH_TEST);

    glDepthFunc(GL_LEQUAL);

    glEnable(GL_CULL_FACE);
}
//TODO look for the edge of the cube

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
    glLoadIdentity(); 
    glTranslatef(0.0f, 0.0f, -5.0f); 
    glRotatef(xrot, 1.0f, 0.0f, 0.0f);
    glRotatef(yrot, 0.0f, 1.0f, 0.0f); 
    glRotatef(zrot, 0.0f, 0.0f, 1.0f); 
    glBegin(GL_QUAD_STRIP);
    GLfloat s = 1; // le sommet

    glBegin(GL_QUADS);
    glColor3f(1.0f, 0.0f, 0.0f);  //front ROUGE
    //from the front view, top left corner
    //R 1-3  
    glVertex3f(s, s, s);
    glVertex3f(.4, s, s);
    glVertex3f(.4, 0.4, s);
    glVertex3f(s, 0.4, s);
    //R 1-2
    glVertex3f(.3, s, s);
    glVertex3f(-.3, s, s);
    glVertex3f(-.3, 0.4, s);
    glVertex3f(.3, 0.4, s);
    //R 1-1
    glVertex3f(-.4, s, s);
    glVertex3f(-s, s, s);
    glVertex3f(-s, 0.4, s);
    glVertex3f(-.4, 0.4, s);
    //R 2-3
    glVertex3f(s, 0.3, s);
    glVertex3f(.4, 0.3, s);
    glVertex3f(.4, -0.3, s);
    glVertex3f(s, -0.3, s);
    //R 2-2
    glVertex3f(.3, 0.3, s);
    glVertex3f(-.3, 0.3, s);
    glVertex3f(-.3, -0.3, s);
    glVertex3f(.3, -0.3, s);
    //R 2-1
    glVertex3f(-.4, 0.3, s);
    glVertex3f(-s, 0.3, s);
    glVertex3f(-s, -0.3, s);
    glVertex3f(-.4, -0.3, s);
    //R 3-3
    glVertex3f(s, -.4, s);
    glVertex3f(.4, -.4, s);
    glVertex3f(.4, -s, s);
    glVertex3f(s, -s, s);
    //R 3-2
    glVertex3f(.3, -.4, s);
    glVertex3f(-.3, -.4, s);
    glVertex3f(-.3, -s, s);
    glVertex3f(.3, -s, s);
    //R 3-1
    glVertex3f(-.4, -.4, s);
    glVertex3f(-s, -.4, s);
    glVertex3f(-s, -s, s);
    glVertex3f(-.4, -s, s);


    glColor3f(0.0f, 0.0f, 1.0f);  //BLEU top
    /*from the top view, TOP right */
    //B 1-3
    glVertex3f(s, s, -s);
    glVertex3f(.4, s, -s);
    glVertex3f(.4, s, -0.4);
    glVertex3f(s, s, -0.4);
    //B 1-2
    glVertex3f(.3, s, -s);
    glVertex3f(-.3, s, -s);
    glVertex3f(-.3, s, -0.4);
    glVertex3f(.3, s, -0.4);
    //B 1-1
    glVertex3f(-.4, s, -s);
    glVertex3f(-s, s, -s);
    glVertex3f(-s, s, -0.4);
    glVertex3f(-.4, s, -0.4);
    //B 2-3
    glVertex3f(s, s, -.3);
    glVertex3f(.4, s, -0.3);
    glVertex3f(.4, s, 0.3);
    glVertex3f(s, s, 0.3);
    //B 2-2
    glVertex3f(.3, s, -.3);
    glVertex3f(-.3, s, -0.3);
    glVertex3f(-.3, s, 0.3);
    glVertex3f(.3, s, 0.3);
    //B 2-1
    glVertex3f(-.4, s, -.3);
    glVertex3f(-s, s, -0.3);
    glVertex3f(-s, s, 0.3);
    glVertex3f(-.4, s, 0.3);
    //B 3-3
    glVertex3f(s, s, .4);
    glVertex3f(.4, s, .4);
    glVertex3f(.4, s, s);
    glVertex3f(s, s, s);
    //B 3-2
    glVertex3f(.3, s, .4);
    glVertex3f(-.3, s, .4);
    glVertex3f(-.3, s, s);
    glVertex3f(.3, s, s);
    //B 3-1
    glVertex3f(-.4, s, .4);
    glVertex3f(-s, s, .4);
    glVertex3f(-s, s, s);
    glVertex3f(-.4, s, s);

    glColor3f(1.0f, 1.0f, 1.0f); // left BLANC
    /*from the right view, top right*/
    //W 1-3
    glVertex3f(-s, s, s);
    glVertex3f(-s, s, .4);
    glVertex3f(-s, .4, .4);
    glVertex3f(-s, .4, s);
    //W 1-2
    glVertex3f(-s, s,.3);
    glVertex3f(-s, s, -.3);
    glVertex3f(-s, .4, -.3);
    glVertex3f(-s, .4, .3);
    //W 1-1
    glVertex3f(-s, s, -.4);
    glVertex3f(-s, s, -s);
    glVertex3f(-s, .4, -s);
    glVertex3f(-s, .4, -.4);
    //W 2-3
    glVertex3f(-s, .3, s);
    glVertex3f(-s, .3, .4);
    glVertex3f(-s, -.3, .4);
    glVertex3f(-s, -.3, s);
    //W 2-2
    glVertex3f(-s, .3, .3);
    glVertex3f(-s, .3, -.3);
    glVertex3f(-s, -.3, -.3);
    glVertex3f(-s, -.3, .3);
    //W 2-1
    glVertex3f(-s, .3, -.4);
    glVertex3f(-s, .3, -s);
    glVertex3f(-s, -.3, -s);
    glVertex3f(-s, -.3, -.4);
    //W 3-3
    glVertex3f(-s, -.4, s);
    glVertex3f(-s, -.4, .4);
    glVertex3f(-s, -s, .4);
    glVertex3f(-s, -s, s);
    //W 3-2
    glVertex3f(-s, -.4, .3);
    glVertex3f(-s, -.4, -.3);
    glVertex3f(-s, -s, -.3);
    glVertex3f(-s, -s, .3);
    //W 3-1
    glVertex3f(-s, -.4, -.4);
    glVertex3f(-s, -.4, -s);
    glVertex3f(-s, -s, -s);
    glVertex3f(-s, -s, -.4);


    glColor3f(0.0f, 1.0f, 0.0f); // bottom green
    /*from the bottom view, top right*/
    //G 1-3
    glVertex3f(s, -s, s);
    glVertex3f(.4, -s, s);
    glVertex3f(.4, -s, 0.4);
    glVertex3f(s, -s, .4);
    //G 1-2
    glVertex3f(.3, -s, s);
    glVertex3f(-.3, -s, s);
    glVertex3f(-.3, -s, 0.4);
    glVertex3f(.3, -s, .4);
    //G 1-1
    glVertex3f(-.4, -s, s);
    glVertex3f(-s, -s, s);
    glVertex3f(-s, -s, 0.4);
    glVertex3f(-.4, -s, .4);
    //G 2-3
    glVertex3f(s, -s, 0.3);
    glVertex3f(.4, -s, 0.3);
    glVertex3f(.4, -s,-0.3);
    glVertex3f(s, -s, -.3);
    //G 2-2
    glVertex3f(.3, -s, 0.3);
    glVertex3f(-.3, -s, 0.3);
    glVertex3f(-.3, -s, -0.3);
    glVertex3f(.3, -s, -.3);
    //G 2-1
    glVertex3f(-.4, -s, 0.3);
    glVertex3f(-s, -s, 0.3);
    glVertex3f(-s, -s, -0.3);
    glVertex3f(-.4, -s, -.3);
    //G 3-3
    glVertex3f(s, -s, -0.4);
    glVertex3f(.4, -s, -0.4);
    glVertex3f(.4, -s, -s);
    glVertex3f(s, -s, -s);
    //G 3-2
    glVertex3f(.3, -s, -0.4);
    glVertex3f(-.3, -s, -0.4);
    glVertex3f(-.3, -s, -s);
    glVertex3f(.3, -s, -s);
    //G 3-1
    glVertex3f(-.4, -s, -0.4);
    glVertex3f(-s, -s, -0.4);
    glVertex3f(-s, -s, -s);
    glVertex3f(-.4, -s, -s);

    glColor3f(1.0f, (129.0 / 255.0), 0.0f); //back ORANGE
    /*from the back view top right*/
    //O 1-1
    glVertex3f(s, .4, -s);
    glVertex3f(.4, .4, -s);
    glVertex3f(.4, s, -s);
    glVertex3f(s, s, -s);
    //O 1-2
    glVertex3f(.3, .4, -s);
    glVertex3f(-.3, .4, -s);
    glVertex3f(-.3, s, -s);
    glVertex3f(.3, s, -s);
    //O 1-3
    glVertex3f(-.4, .4, -s);
    glVertex3f(-s, .4, -s);
    glVertex3f(-s, s, -s);
    glVertex3f(-.4, s, -s);
    //O 2-1
    glVertex3f(s, -.3, -s);
    glVertex3f(.4, -.3, -s);
    glVertex3f(.4, .3, -s);
    glVertex3f(s, .3, -s);
    //O 2-2
    glVertex3f(.3, -.3, -s);
    glVertex3f(-.3, -.3, -s);
    glVertex3f(-.3, .3, -s);
    glVertex3f(.3, .3, -s);
    //O 2-3
    glVertex3f(-.4, -.3, -s);
    glVertex3f(-s, -.3, -s);
    glVertex3f(-s, .3, -s);
    glVertex3f(-.4, .3, -s);
    //O 3-3
    glVertex3f(-.4, -s, -s);
    glVertex3f(-s, -s, -s);
    glVertex3f(-s, -.4, -s);
    glVertex3f(-.4, -.4, -s);
    //O 3-2
    glVertex3f(.3, -s, -s);
    glVertex3f(-.3, -s, -s);
    glVertex3f(-.3, -.4, -s);
    glVertex3f(.3, -.4, -s);
    //O 3-1
    glVertex3f(s, -s, -s);
    glVertex3f(.4, -s, -s);
    glVertex3f(.4, -.4, -s);
    glVertex3f(s, -.4, -s);

    glColor3f(1.0f, 1.0f, 0.0f); //Right yellow
    /*from the right view, top right*/
    //Y 1-3
    glVertex3f(s, s, -s);
    glVertex3f(s, s, -.4);
    glVertex3f(s, .4, -.4);
    glVertex3f(s, .4, -s);
    //Y 1-2
    glVertex3f(s, s, -.3);
    glVertex3f(s, s, .3);
    glVertex3f(s, .4, .3);
    glVertex3f(s, .4, -.3);
    //Y 1-2
    glVertex3f(s, s, .4);
    glVertex3f(s, s, s);
    glVertex3f(s, .4, s);
    glVertex3f(s, .4, .4);
    //Y- 2-3
    glVertex3f(s, .3, -s);
    glVertex3f(s, .3, -.4);
    glVertex3f(s, -.3, -.4);
    glVertex3f(s, -.3, -s);
    //Y- 2-2
    glVertex3f(s, .3, -.3);
    glVertex3f(s, .3, .3);
    glVertex3f(s, -.3, .3);
    glVertex3f(s, -.3, -.3);
    //Y- 2-1
    glVertex3f(s, .3, .4);
    glVertex3f(s, .3, s);
    glVertex3f(s, -.3, s);
    glVertex3f(s, -.3, .4);
    //Y 3-3
    glVertex3f(s, -.4, -s);
    glVertex3f(s, -.4, -.4);
    glVertex3f(s, -s, -.4);
    glVertex3f(s, -s, -s);
    //Y 3-2
    glVertex3f(s, -.4, -.3);
    glVertex3f(s, -.4, .3);
    glVertex3f(s, -s, .3);
    glVertex3f(s, -s, -.3);
    //Y 3-1
    glVertex3f(s, -.4, .4);
    glVertex3f(s, -.4, s);
    glVertex3f(s, -s, s);
    glVertex3f(s, -s, .4);


    glEnd();

    xrot += 30.0f;
    yrot +=10.0f; 
    zrot += 10.0f;

    glutSwapBuffers();
}

void key(unsigned char key, int x, int y) {
     switch (key) { 
     case 27:       
     exit(0);       
     break;        
     default:       
         break; 
     }
                 
     glutPostRedisplay();
}
//
//void idle() { /* c'est lui qui fait tourner non stop*/
//    glutPostRedisplay(); 
//}

int main(int argc, char* argv[]) {
    glutInit(&argc, argv);   
    glutInitWindowSize(640, 480); 
    glutInitWindowPosition(10, 10); 
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("Rubik's cube to be");    
    glutReshapeFunc(resize);  
    glutDisplayFunc(display);   
    glutKeyboardFunc(key);   
    //glutIdleFunc(idle);

    glutMainLoop();
}



 /*plain cube ROUGE*/
    //glVertex3f(1.0f, 1.0f, 1.0f);
    //glVertex3f(-1.0f, 1.0f, 1.0f);
    //glVertex3f(-1.0f, -1.0f, 1.0f);
    //glVertex3f(1.0f, -1.0f, 1.0f);

    /*face divided in 3*/
    //glVertex3f(s, s, s);
    //glVertex3f(-s, s, s);
    //glVertex3f(-s,0.4, s);
    //glVertex3f(s, 0.4, s);

    //glVertex3f(s, 0.3, s);
    //glVertex3f(-s, 0.3, s);
    //glVertex3f(-s, -0.3, s);
    //glVertex3f(s, -0.3,s);

    //glVertex3f(s, -.4, s);
    //glVertex3f(-s, -.4, s);
    //glVertex3f(-s, -s, s);
    //glVertex3f(s, -s, s);

    /*plain cube BLEU*/
    //glVertex3f(1.0f, 1.0f, -1.0f);
    //glVertex3f(-1.0f, 1.0f, -1.0f);
    //glVertex3f(-1.0f, 1.0f, 1.0f);
    //glVertex3f(1.0f, 1.0f, 1.0f);

    // face divided in 3
    /*glVertex3f(s, s, -s);
    glVertex3f(-s, s, -s);
    glVertex3f(-s, s, -0.4);
    glVertex3f(s, s, -0.4);

    glVertex3f(s, s, -.3);
    glVertex3f(-s, s, -0.3);
    glVertex3f(-s, s, 0.3);
    glVertex3f(s, s, 0.3);

    glVertex3f(s, s, .4);
    glVertex3f(-s, s, .4);
    glVertex3f(-s,s,s);
    glVertex3f(s,s,s);*/

    //
    //    glColor3f(1.0f, 1.0f, 1.0f); // back white
    ////glVertex3f(-1.0f, 1.0f, 1.0f);
    ////glVertex3f(-1.0f, 1.0f, -1.0f);
    ////glVertex3f(-1.0f, -1.0f, -1.0f);
    ////glVertex3f(-1.0f, -1.0f, 1.0f);
        // face divided in 3
    //    glVertex3f(-s, s, s);
    //    glVertex3f(-s, s, -s);
    //    glVertex3f(-s, .4, -s);
    //    glVertex3f(-s, .4, s);
    //
    //    glVertex3f(-s, .3, s);
    //    glVertex3f(-s, .3, -s);
    //    glVertex3f(-s, -.3, -s);
    //    glVertex3f(-s, -.3, s);
    //
    //    glVertex3f(-s, -.4, s);
    //    glVertex3f(-s, -.4, -s);
    //    glVertex3f(-s, -s, -s);
    //    glVertex3f(-s, -s, s);
    

//    glColor3f(0.0f, 1.0f, 0.0f); // bottom green
    //plain face
//    //glVertex3f(1.0f, -1.0f, 1.0f);
//    //glVertex3f(-1.0f, -1.0f, 1.0f);
//    //glVertex3f(-1.0f, -1.0f, -1.0f);
//    //glVertex3f(1.0f, -1.0f, -1.0f);
    //face divided in 3
//    glVertex3f(s, -s, s);
//    glVertex3f(-s, -s, s);
//    glVertex3f(-s, -s, 0.4);
//    glVertex3f(s, -s, .4);
//
//    glVertex3f(s, -s, 0.3);
//    glVertex3f(-s, -s, 0.3);
//    glVertex3f(-s, -s,-0.3);
//    glVertex3f(s, -s, -.3);
//
//    glVertex3f(s, -s, -0.4);
//    glVertex3f(-s, -s, -0.4);
//    glVertex3f(-s, -s, -s);
//    glVertex3f(s, -s, -s);

//    glColor3f(1.0f, (129.0 / 255.0), 0.0f); //right orange
    // plain face
////glVertex3f(1.0f, -1.0f, -1.0f);
////glVertex3f(-1.0f, -1.0f, -1.0f);
////glVertex3f(-1.0f, 1.0f, -1.0f);
////glVertex3f(1.0f, 1.0f, -1.0f);
//    face divided by 3
//    glVertex3f(s, -s, -s);
//    glVertex3f(-s, -s, -s);
//    glVertex3f(-s, -.4, -s);
//    glVertex3f(s, -.4, -s);
//
//    glVertex3f(s, -.3, -s);
//    glVertex3f(-s, -.3, -s);
//    glVertex3f(-s, .3, -s);
//    glVertex3f(s, .3, -s);
//
//    glVertex3f(s, .4, -s);
//    glVertex3f(-s, .4, -s);
//    glVertex3f(-s, s, -s);
//    glVertex3f(s, s, -s);
//

//    glColor3f(1.0f, 1.0f, 0.0f); //front yellow
    //plain face
////glVertex3f(1.0f, 1.0f, -1.0f);
////glVertex3f(1.0f, 1.0f, 1.0f);
////glVertex3f(1.0f, -1.0f, 1.0f);
////glVertex3f(1.0f, -1.0f, -1.0f);
    // face divided by 3
//    glVertex3f(s, s, -s);
//    glVertex3f(s, s, s);
//    glVertex3f(s, .4, s);
//    glVertex3f(s, .4, -s);
//
//    glVertex3f(s, .3, -s);
//    glVertex3f(s, .3, s);
//    glVertex3f(s, -.3, s);
//    glVertex3f(s, -.3, -s);
//
//    glVertex3f(s, -.4, -s);
//    glVertex3f(s, -.4, s);
//    glVertex3f(s, -s, s);
//    glVertex3f(s, -s, -s);

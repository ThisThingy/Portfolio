from cmu_graphics import *
import random
# FNAF GO BRRRRRRRRR HURR HURR HURR HURR HURR HURR HUr HUr Hur HURRR


def onAppStart(app):
    restart(app)
    app.night = 1
    

def restart(app):
    app.width = 800
    app.height = 500

    # Screen Calls
    app.title = True
    app.helpWanted = False
    app.nightTransition = False
    app.office = False
    
    app.imageSpeed = 1
    app.imageMoveSwitch = False
    app.imageCenterX = 400
    app.imageMoving = True
    
    # Death Screens
    app.dead = False
    app.freddyKillin = False
    app.bonGonKill = False
    app.chiKill = False
    app.hooked = False
    app.CYA = False
    
    # Office Calls
    app.rightDoor = False
    app.rDoor = 10
    app.rightLight = False
    app.leftDoor = False
    app.lDoor = 10
    app.leftLight = False
    
    app.withinNew = False
    app.withinCon = False
    
    
    app.steps = 0
    app.adjust = 0
    
    #Time Progression
    app.seconds = 0
    app.hour = 12
    
    app.helpOpacity = 10
    app.transition = 100
    app.offTrans = 0
    
    app.nightEnd = False
    
    # Camera Calls
    
    app.switch = True
    app.camUp = False
    app.cam1A = True
    app.cam1B = False
    app.cam1C = False
    app.cam2A = False
    app.cam2B = False
    app.cam3 = False
    app.cam4A = False
    app.cam4B = False
    app.cam5 = False
    app.cam6 = False
    app.cam7 = False
    
    ### AMINATRONICS
    
    #Freddy
    app.freddyMS = True
    app.freddyMainStage = False
    app.freddyParty = False
    app.freddyPoopy = False
    app.freddyCookin = False
    app.freddyLookin = False
    app.freddySniffing = False
    
    app.freddyDif = 20
    
    #Bonnie
    app.bonnieMainStage = True
    app.bonnieStupidFace = False
    app.bonnieComing = False
    app.bonnieRizz = False
    app.bonnieInTheCloset = False
    app.bonnieBackstage = False
    app.bonnieBsMencaing = False
    
    app.bonnieDif = 20
    
    #Chica
    app.chicaMainStage = True
    app.chicaPIZZA = False
    app.chicaOnHerWay = False
    app.chicaOnHerWayButCloser = False
    app.chicaGivingThatStare = False
    app.chicaKitchen = False
    app.chicaBathroom = False
    
    app.chicaDif = 20
    
    #Foxy
    app.foxyCloseted = True
    app.foxyPeeking = False
    app.foxyLeaving = False
    app.foxyGone = False
    app.foxyComing = False
    
    app.foxyDif = 20
    
    #Golden Freddy
    app.itsMe = False
    

#####--------------------------------------------------------------------------------------------------#

def movementCheck(app, difLevel):
    
    L = 0
    ran = random.randrange(1, 21)
    L = ran
    
    if L < difLevel:
        return True
        
    else:
        return False
    print(L)
        
#####--------------------------------------------------------------------------------------------------#

def drawTitle(app):
    
    drawRect(0, 0, app.width, app.height)
    drawLabel('Five', 150, 50, size = 30, fill = 'white')
    drawLabel('Nights', 165, 85, size = 30, fill = 'white')
    drawLabel('At', 135, 120, size = 30, fill = 'white')
    drawLabel("Freddy's :", 185, 155, size = 30, fill = 'white')
    drawLabel("Mistakes", 180, 190, size = 30, fill ='white')

    if app.withinNew == True:
        drawLabel('New Game', 200, 260, size = 40, fill = 'white', bold = True)
        
    else:
        drawLabel('New Game', 195, 260, size = 30, fill = 'white')
        
    if app.withinCon == True:
        drawLabel('Continue', 190, 295, size = 40, fill = 'white', bold = True)
    
    else:
        drawLabel('Continue', 180, 295, size =30, fill = 'white')
        
    if app.night == 1:        
        drawLabel('1st Night', 180, 330, size = 30, fill = 'white')
    
    elif app.night == 2:
        drawLabel('2nd Night', 185, 330, size = 30, fill = 'white')
        
    elif app.night == 3:
        drawLabel('3rd Night', 180, 330, size = 30, fill = 'white')
        
    else:
        drawLabel(f'{app.night}th Night', 180, 330, size = 30, fill = 'white')
        
    
    
    
    ####### Title Freddy
    
    ### body
    
    fredbed = 'cmu://629187/26641418/fredbed.gif'
    
    freddy = 'cmu://629187/40586625/Ff.jpg'
    drawImage(freddy, 550, 250, width = 500, height = 500, align = 'center')

    # drawOval(465, 360, 70, 150, fill = 'saddleBrown', rotateAngle = 30)
    # drawOval(485, 360, 40, 150, opacity = 70, rotateAngle = 30)
    
    # drawCircle(505, 315, 35, fill = 'saddleBrown', border = 'black')
    # drawCircle(520, 320, 25)
    
    # drawOval(440, 410, 60, 80, rotateAngle = -20)
    # drawOval(440, 415, 60, 80, fill = 'saddleBrown', rotateAngle = -20)
    # drawCircle(450, 435, 25)
    
    # drawLine(445, 430, 460, 450, fill = 'silver', lineWidth = 15)
    
    # drawRect(460, 430, 40, 70, fill = 'saddleBrown', rotateAngle = 50)
    # drawLine(460, 475, 500, 445, dashes = (1, 15), lineWidth = 45)
    
    
    # drawCircle(695, 315, 30, fill = 'saddleBrown')
    # drawCircle( 680, 320, 25)
    
    
    # drawOval(600, 470, 200, 500, fill = 'saddleBrown')
    # drawOval(600, 470, 175, 450, fill = 'peru')
    # drawCircle(600, 350, 30)
    # drawRegularPolygon(560, 350, 35, 3, rotateAngle = 90)
    # drawRegularPolygon(640, 350, 35, 3, rotateAngle = -90)        
    
    
    # ### head
    # drawOval(600, 170, 200, 195, fill = 'saddleBrown')
    # drawOval(600, 220, 250, 120, fill = 'saddleBrown')
    # drawOval(600, 280, 180, 120, fill ='saddleBrown', border = 'black')
    # drawOval(600, 270, 170, 90, fill = 'black')
    
    # #eyebrows
    # drawOval(555, 135, 50, 15, rotateAngle = 10)
    # drawOval(645, 135, 50, 15, rotateAngle = -10)
    
    # # tophat        
    # drawOval(600, 40, 90, 20, fill ='dimGrey')
    # drawOval(600, 90, 150, 50, fill = 'black')
    # drawRect(555, 40, 90, 40, fill = 'dimGrey')
    # drawOval(600, 85, 150, 50, fill = 'dimGrey')
    # drawLine(545, 65, 655, 65, fill = 'black', lineWidth = 5)
    
    # # ears
    # drawCircle(480, 110, 30, fill = 'saddleBrown')
    # drawOval(480, 110, 70, 30, fill = 'saddleBrown', rotateAngle = 20)
    # drawLine(495, 150, 520, 100, lineWidth = 15)
    # drawLine(505, 120, 515, 125, fill = 'grey', lineWidth = 15)
    # size = 20
    # for c in range(5):
    #     drawCircle(480, 110, size, opacity = 50)
    #     size -= 4
    
    
    # drawCircle(720, 110, 30, fill = 'saddleBrown')
    # drawOval(720, 110, 70, 30, fill = 'saddleBrown', rotateAngle = -20)
    # drawLine(705, 150, 680, 100, lineWidth = 15)
    # drawLine(695, 120, 685, 125, fill = 'grey', lineWidth = 15)
    
    # # eyes
    # drawCircle(555, 175, 27)
    # drawOval(555, 175, 45, 30, fill = 'white')
    # drawCircle(555, 175, 12, border = 'lightBlue', borderWidth = 7)
    
    # drawCircle(645, 175, 27)
    # drawOval(645, 175, 45, 30, fill = 'white')
    # drawCircle(645, 175, 12, fill = 'black', border = 'lightBlue', borderWidth = 7)
    
    
    
    # # draws jaw area
    # drawOval(600, 235, 175, 100, fill = 'saddleBrown', border = 'black')
    # drawOval(600, 280, 120, 35, fill = 'white')
    # drawLine(500, 270, 800, 270, lineWidth = 15)
    
    # drawPolygon(512, 280, 518, 280, 515, 260, fill = 'saddleBrown')
    # drawPolygon(688, 280, 682, 280, 685, 260, fill = 'saddleBrown')
    
    # # draws nose and center line
    # drawOval(600, 193, 60, 30, fill = 'black')
    # drawLine(600, 195, 600, 370, fill = 'black', lineWidth = 3)
    
    # drawCircle(540, 220, 3)
    # drawCircle(530, 240, 3)
    # drawCircle(550, 240, 3)
    
    # drawCircle(660, 220, 3)
    # drawCircle(670, 240, 3)
    # drawCircle(650, 240, 3)
    
    # # draws his goofy teeth
    # drawLine(560, 275, 560, 300, lineWidth = 1.5)
    # drawLine(640, 275, 640, 300, lineWidth = 1.5)
    # drawLine(580, 275, 580, 300, lineWidth = 2.5)
    # drawLine(620, 275, 620, 300, lineWidth = 2.5)
    # drawLine(604, 275, 604, 300, lineWidth = 5.7)
    # drawOval(600, 275, 115, 10)


    # gradient effect
    size = 300
    for i in range(50):
        drawRect(app.width - size, 0, size, 500, opacity = 10)
        size -= 6
    
    newSize = 100
    for i in range(20):
        drawRect(0, app.height - newSize, 800, newSize, opacity = 15)
        newSize -= 5

#####--------------------------------------------------------------------------------------------------#

def drawHelpWanted(app):
    helpWanted = 'cmu://629187/27640789/Screenshot+2024-01-10+13.18.53.png'
    drawRect(0, 0, 800, 500)
    drawImage(helpWanted, 400, 250, align = 'center', width = 800, height = 500, opacity = app.helpOpacity)

#####--------------------------------------------------------------------------------------------------#

def drawNightTransition(app):
    drawRect(0, 0, 800, 500, opacity = app.transition)
    drawLabel(f'Night {app.night}', 400, 250, fill = 'white', size = 50, opacity = app.transition)

#####--------------------------------------------------------------------------------------------------#

def drawOffice(app):
    if app.office == True and app.dead != True and app.camUp != True:
        drawRect(0, 0, 800, 500, opacity = app.offTrans)
        table = 'cmu://629187/26450908/office.jpg'
        drawImage(table, 400, 250, align = 'center', width = 500, height = 500, opacity = app.offTrans)
        drawRect(0, 0, 200, 500, fill = rgb(0, 0, 10), opacity = app.offTrans)
        drawRect(600, 0, 200, 500, fill = rgb(0, 0, 10), opacity = app.offTrans)
        
        #####--------------------------------------------------------------------------------------------------#
        
        if app.leftLight == True:
            drawRect(50, 0, 100, 500, fill = rgb(120, 120, 150), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
        else:
            drawRect(50, 0, 100, 500, fill = rgb(20, 20, 50), border = rgb(100, 100, 100), borderWidth = 5, opacity = app.offTrans)
            
        if app.lDoor <= 530:
            drawRect(50, 0, 100, app.lDoor, fill = 'grey', opacity = app.offTrans)
        
        if app.leftDoor == True:
            drawRect(0, 250, 50, 50, fill = 'green', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
        else:
            drawRect(0, 250, 50, 50, fill = 'red', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
    
        if app.leftLight == True:
            drawRect(0, 300, 50, 50, fill = 'lightBlue', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
        else:
            drawRect(0, 300, 50, 50, fill = 'silver', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
            
        #####--------------------------------------------------------------------------------------------------#
        
        if app.rightLight == True:
            drawRect(650, 0, 100, 500, fill = rgb(120, 120, 150), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
        else:
            drawRect(650, 0, 100, 500, fill = rgb(20, 20, 50), border = rgb(100, 100, 100), borderWidth = 5, opacity = app.offTrans)
            
        if app.rDoor <= 530:
            drawRect(650, 0, 100, app.rDoor, fill = 'grey', opacity = app.offTrans)
        
        if app.rightDoor == True:
            drawRect(750, 250, 50, 50, fill = 'green', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
        else:
            drawRect(750, 250, 50, 50, fill = 'red', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
    
        if app.rightLight == True:
            drawRect(750, 300, 50, 50, fill = 'lightBlue', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
        else:
            drawRect(750, 300, 50, 50, fill = 'silver', border = rgb(0, 0, 10), opacity = app.offTrans, borderWidth = 10)
        
        #####--------------------------------------------------------------------------------------------------#
        if app.leftLight == True:
            drawPolygon(215, 100, 215, 265, 155, 275, 155, 60, fill = rgb(120, 120, 150), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
            
        else:
            drawPolygon(215, 100, 215, 265, 155, 275, 155, 60, fill = rgb(20, 20, 50), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
    
        
        if app.rightLight == True:
            drawPolygon(585, 100, 585, 265, 645, 275, 645, 60, fill = rgb(120, 120, 150), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
            
        else:
            drawPolygon(585, 100, 585, 265, 645, 275, 645, 60, fill = rgb(20, 20, 50), opacity = app.offTrans, border = rgb(100, 100, 100), borderWidth = 5)
        
    #####--------------------------------------------------------------------------------------------------#

    
    ############ keep at back
    
    drawLabel(f'{app.hour} AM', 725, 35, fill = 'white', size = 30, opacity = app.offTrans)
    drawLabel(f'Night {app.night}', 725, 65, size = 20, fill = 'white', opacity = app.offTrans)
    
#####--------------------------------------------------------------------------------------------------#    

def drawNightEnd(app):
    drawRect(0, 0, 800, 500)
    drawLabel('6 AM', 400, 250, fill = 'white', size = 40)

#####--------------------Jumpscares------------------------------------------------------------------------------#

def fredbedScare(app):
    
    frame1 = 'cmu://629187/26654334/Screenshot+2023-11-22+09.23.02.png'
    frame2 = 'cmu://629187/26654367/Screenshot+2023-11-22+09.23.06.png'
    frame3 = 'cmu://629187/26654376/Screenshot+2023-11-22+09.23.08.png'
    frame4 = 'cmu://629187/26654381/Screenshot+2023-11-22+09.23.10.png'
    frame5 = 'cmu://629187/26654435/Screenshot+2023-11-22+09.23.12.png'
    frame6 = 'cmu://629187/26654457/Screenshot+2023-11-22+09.23.14.png'
    drawRect(0, 0, 800, 500, fill = 'black')
    if app.freddyKillin == True:    
        if (app.steps % 1 == 0 and 
            app.steps % 2 != 0 and 
            app.steps % 3 != 0 and 
            app.seconds % 4 != 0 and 
            app.seconds % 5 != 0 and 
            app.seconds % 6 != 0):
            drawFrame1 = drawImage(frame1, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 2 == 0 and app.seconds % 4 != 0 and app.seconds % 6 != 0:
            drawFrame2 = drawImage(frame2, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.seconds % 3 == 0 and app.steps % 6 != 0:
            drawFrame3 = drawImage(frame3, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.steps % 4 == 0:
            drawFrame4 = drawImage(frame4, 400, 250, width = 800, height = 500, align = 'center')
            
        if app.seconds % 5 == 0:
            drawFrame5 = drawImage(frame5, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.seconds % 6 == 0:
            drawFrame6 = drawImage(frame6, 400, 250, width = 800, height = 500, align = 'center')

        drawRect(0, 0, 800, 500, opacity = 50)
        
def bongonKill(app):
    frame1 = 'cmu://629187/27160600/bongon1.gif'
    frame2 = 'cmu://629187/27160660/bongon2.gif'
    frame3 = 'cmu://629187/27160686/bongon3.gif'
    frame4 = 'cmu://629187/27160713/bongon4.gif'
    frame5 = 'cmu://629187/27160748/bongon5.gif'
    frame6 = 'cmu://629187/27160787/bongon6.gif'
    
    if app.bonGonKill == True:
        if (app.steps % 1 == 0 and
            app.steps % 2 != 0 and 
            app.steps % 3 != 0 and 
            app.steps % 4 != 0 and 
            app.steps % 5 != 0 and 
            app.steps % 6 != 0):
            drawFrame1 = drawImage(frame1, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 2 == 0 and app.steps % 4 != 0 and app.steps % 6 != 0:
            drawFrame2 = drawImage(frame2, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.steps % 3 == 0 and app.steps % 6 != 0:
            drawFrame3 = drawImage(frame3, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.steps % 4 == 0:
            drawFrame4 = drawImage(frame4, 400, 250, width = 800, height = 500, align = 'center')
            
        if app.steps % 5 == 0:
            drawFrame5 = drawImage(frame5, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 6 == 0:
            drawFrame6 = drawImage(frame6, 400, 250, width = 800, height = 500, align = 'center')

def chickKicken(app):
    drawRect(0, 0, 800, 500)
    frame1 = "cmu://629187/39436822/frame_00_delay-0.04s.png"
    frame2 = "cmu://629187/39436830/frame_01_delay-0.04s.png"
    frame3 = "cmu://629187/39436835/frame_02_delay-0.04s.png"
    frame4 = "cmu://629187/39436836/frame_03_delay-0.04s.png"
    frame5 = "cmu://629187/39436839/frame_04_delay-0.04s.png"
    frame6 = "cmu://629187/39436843/frame_05_delay-0.04s.png"
    frame7 = "cmu://629187/39436844/frame_06_delay-0.04s.png"
    frame8 = "cmu://629187/39436847/frame_07_delay-0.04s.png"
    frame9 = "cmu://629187/39436848/frame_08_delay-0.04s.png"
    frame10 = "cmu://629187/39436850/frame_09_delay-0.04s.png"
    frame11 = "cmu://629187/39436852/frame_10_delay-0.04s.png"
    frame12 = "cmu://629187/39436854/frame_11_delay-0.04s.png"
    frame13 = "cmu://629187/39436856/frame_12_delay-0.04s.png"
    frame14 = "cmu://629187/39436857/frame_13_delay-0.04s.png"
    frame15 = "cmu://629187/39436858/frame_14_delay-0.04s.png"
    frame16 = "cmu://629187/39436859/frame_15_delay-0.04s.png"
    
    
    if app.chiKill == True:
        if (app.steps % 1 == 0 and
            app.steps % 2 != 0 and 
            app.steps % 3 != 0 and 
            app.steps % 4 != 0 and 
            app.steps % 5 != 0 and 
            app.steps % 6 != 0 and 
            app.steps % 7 != 0 and 
            app.steps % 8 != 0 and 
            app.steps % 9 != 0 and 
            app.steps % 10 != 0 and 
            app.steps % 11 != 0 and 
            app.steps % 12 != 0 and 
            app.steps % 13 != 0 and 
            app.steps % 14 != 0 and 
            app.steps % 15 != 0 and 
            app.steps % 16 != 0):
            drawFrame1 = drawImage(frame1, 400, 250, width = 800, height = 500, align = 'center')
        
        if (app.steps % 2 == 0 and app.steps % 4 != 0 and app.steps % 6 != 0 and 
            app.steps % 8 != 0 and app.steps % 10 != 0 and app.steps % 12 != 0 and
            app.steps % 14 != 0 and app.steps % 16 != 0):
            drawFrame2 = drawImage(frame2, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.steps % 3 == 0 and app.steps % 6 != 0 and app.steps % 9 != 0 and app.steps % 12 != 0 and app.steps % 15 != 0:
            drawFrame3 = drawImage(frame3, 400, 250, width = 800, height = 500, align = 'center') 
            
        if app.steps % 4 == 0 and app.steps % 8 == 0 and app.steps % 12 == 0 and app.steps % 16 == 0:
            drawFrame4 = drawImage(frame4, 400, 250, width = 800, height = 500, align = 'center')
            
        if app.steps % 5 == 0 and app.steps % 10 == 0 and app.steps % 15 == 0:
            drawFrame5 = drawImage(frame5, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 6 == 0 and app.steps % 12 == 0:
            drawFrame6 = drawImage(frame6, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 7 == 0 and app.steps % 14 == 0:
            drawFrame7 = drawImage(frame7, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 8 == 0 and app.steps % 16 == 0:
            drawFrame8 = drawImage(frame8, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 9 == 0:
            drawFrame9 = drawImage(frame9, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 10 == 0:
            drawFrame10 = drawImage(frame10, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 11 == 0:
            drawFrame11 = drawImage(frame11, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 12 == 0:
            drawFrame12 = drawImage(frame12, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 13 == 0:
            drawFrame13 = drawImage(frame13, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 14 == 0:
            drawFrame14 = drawImage(frame14, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 15 == 0:
            drawFrame15 = drawImage(frame15, 400, 250, width = 800, height = 500, align = 'center')
        
        if app.steps % 16 == 0:
            drawFrame16 = drawImage(frame16, 400, 250, width = 800, height = 500, align = 'center')
        


#####--------------------------------------------------------------------------------------------------#    

def camFlick(app):
    if ((app.office == True or app.camUp == True) and app.dead != True):
        if app.switch == True:
            drawPolygon(10, 490, 160, 450, 440, 450, 590, 490, fill = 'silver', border = 'white', borderWidth = 20, opacity = 30)
        
            drawLine(145, 460, 455, 460, fill = 'darkSlateGray', opacity = 50, lineWidth = 7, arrowEnd = True, arrowStart = True)
            drawLine(105, 480, 495, 480, fill = 'darkSlateGray', opacity = 50, lineWidth = 7, arrowEnd = True, arrowStart = True)
        
#####--------------------------------------------------------------------------------------------------#    

def camPanel(app):
    # Draws camera layout
    
    if app.camUp == True and app.dead != True:
        drawRect(530, 300, 150, 110, fill = None, border = 'grey')
        drawRect(560, 270, 80, 30, fill = None, border = 'grey')
        drawRect(490, 300, 25, 60, fill = None, border = 'grey')
        drawRect(515, 315, 15, 10, fill = None, border = 'grey')
        drawRect(505, 365, 25, 35, fill = None, border = 'grey')
        drawRect(680, 320, 15, 10, fill = None, border = 'grey')
        drawRect(695, 310, 25, 95, fill = None, border = 'grey')
        drawRect(720, 340, 15, 10, fill = None, border = 'grey')
        drawRect(720, 380, 15, 10, fill = None, border = 'grey')
        drawRect(735, 335, 20, 20, fill = None, border = 'grey')
        drawRect(735, 375, 20, 20, fill = None, border = 'grey')
        drawRect(660, 410, 10, 10, fill = None, border = 'grey')
        drawRect(657, 420, 55, 40, fill = None, border = 'grey')
        drawRect(640, 410, 10, 10, fill = None, border = 'grey')
        drawRect(635, 420, 20, 70, fill = None, border = 'grey')
        drawRect(565, 410, 10, 10, fill = None, border = 'grey')
        drawRect(560, 420, 20, 70, fill = None, border = 'grey')
        drawRect(550, 445, 10, 10, fill = None, border = 'grey')
        drawRect(530, 435, 20, 40, fill = None, border = 'grey')
        drawRect(589, 435, 37, 60, fill = None, border = 'grey')
        
        drawRect(600, 463, 15, 15, fill = 'white', border = 'green')
        
        # Draws camera buttons
        if app.cam1A == True:
            drawRect(550, 250, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(550, 250, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #
        if app.cam1B == True:
            drawRect(550, 300, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(550, 300, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #
        if app.cam1C == True:
            drawRect(525, 362, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(525, 362, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #   
        if app.cam2A == True:
            drawRect(560, 440, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(560, 440, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #    
        if app.cam2B == True:
            drawRect(560, 460, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(560, 460, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #    
        if app.cam3 == True:
            drawRect(515, 445, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(515, 445, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #    
        if app.cam4A == True:
            drawRect(635, 440, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(635, 440, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #    
        if app.cam4B == True:
            drawRect(635, 460, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(635, 460, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #
        if app.cam5 == True:
            drawRect(465, 335, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(465, 335, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #
        if app.cam6 == True:
            drawRect(695, 430, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(695, 430, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        #    
        if app.cam7 == True:
            drawRect(697, 315, 35, 20, fill = 'green', border = 'white', borderWidth = 2)
        else:
            drawRect(697, 315, 35, 20, fill = 'dimGrey', border = 'white', borderWidth = 2)
        
#####--------------------Camera Images------------------------------------------------------------------------------#    

def mainStage(app):
    if app.camUp == True:
        if app.cam1A == True:
            drawRect(0, 0, 800, 500)
            if app.freddyMS == True and app.bonnieMainStage == True and app.chicaMainStage == True:
                image = 'cmu://629187/39772854/Show_stage_nocamera.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            elif app.freddyMS == True and app.bonnieMainStage == False and app.chicaMainStage == True:
                image = 'cmu://629187/39772858/68.jpg'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            elif app.freddyMS == True and app.chicaMainStage == False and app.bonnieMainStage == True:
                image = 'cmu://629187/39772861/223.jpg'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            elif app.freddyMS == True and app.chicaMainStage == False and app.bonnieMainStage == False:
                image = 'cmu://629187/39772863/224.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            elif app.chicaMainStage == False and app.bonnieMainStage == False and app.freddyMainStage == True:
                image = 'cmu://629187/39772864/355.jpg'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
            
            elif app.freddyMS == False and app.chicaMainStage == False and app.bonnieMainStage == False and app.freddyMainStage == False:
                image = 'cmu://629187/39772865/Nothing_is_scarier.jpg'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
    
    
    drawLabel(f'{app.hour} AM', 725, 35, fill = 'white', size = 30, opacity = app.offTrans)
    drawLabel(f'Night {app.night}', 725, 65, size = 20, fill = 'white', opacity = app.offTrans)
    camPanel(app)
    camFlick(app)
            
def dining(app):
    if app.camUp == True:
        if app.cam1B == True:
            drawRect(0, 0, 800, 500)
            if app.freddyParty == True:
                image = 'cmu://629187/39773597/Cam1B_freddy.png' # Freddy 1B
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
            
            if app.chicaPIZZA == True :
                image = 'cmu://629187/39773602/215.png'  # Chica 1B
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
            
            if app.bonnieStupidFace == True:
                image = 'cmu://629187/39773601/90.png' # Bonnie 1B
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                    
            if app.chicaPIZZA == True and app.bonnieStupidFace == True:
                image = 'cmu://629187/39773964/Mergedboth.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            else:        
                image = 'cmu://629187/39773595/DiningAreaNoCamera.png' # No One 1B
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
    
    drawLabel(f'{app.hour} AM', 725, 35, fill = 'white', size = 30, opacity = app.offTrans)
    drawLabel(f'Night {app.night}', 725, 65, size = 20, fill = 'white', opacity = app.offTrans)
    camPanel(app)
    camFlick(app)
    
def pirateCove(app):
    if app.camUp == True:
        if app.cam1C == True:
            drawRect(0, 0, 800, 500)
            if app.foxyCloseted == True:
                image = 'cmu://629187/39796123/foxyCloset.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            if app.foxyPeeking == True:
                image = 'cmu://629187/39796124/foxPeek.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            if app.foxyLeaving == True:
                image = 'cmu://629187/39796126/foxLeave.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
            if app.foxyGone == True:
                image = 'cmu://629187/39796127/foxGone.png'
                drawImage(image, app.imageCenterX, 250, align = 'center', width = 1100, height = 450)
                
    drawLabel(f'{app.hour} AM', 725, 35, fill = 'white', size = 30, opacity = app.offTrans)
    drawLabel(f'Night {app.night}', 725, 65, size = 20, fill = 'white', opacity = app.offTrans)
    camPanel(app)
    camFlick(app)
    
    
#####--------------------------------------------------------------------------------------------------#    

# Pathing for animatronics #
def fredbedPath(app):
    if app.bonnieMainStage == False and app.chicaMainStage == False:    
        if movementCheck(app, app.freddyDif) == True:
            if app.freddyMS == True:
                app.freddyMainStage = True
                app.freddyMS = False
            
            elif app.freddyMainStage == True:
                app.freddyParty = True
                app.freddyMainStage = False
            
            elif app.freddyParty == True:
                app.freddyPoopy = True
                app.freddyParty = False
                
            elif app.freddyPoopy == True:
                app.freddyCookin = True
                app.freddyPoopy = False
                
            elif app.freddyCookin == True:
                app.freddyLookin = True
                app.freddyCookin = False
                
            elif app.freddyLookin == True:
                app.freddySniffing = True
                app.freddyLookin = False
            
            elif app.freddySniffing == True and app.rightDoor == False:
                app.dead = True
                app.freddyKillin = True
            else:
                app.freddySniffing = False
                app.freddyMainStage = True
                
def chickenPath(app):
    if movementCheck(app, app.chicaDif) == True:
        if app.chicaMainStage == True:
            app.chicaPIZZA = True
            app.chicaMainStage = False
        
        elif app.chicaPIZZA == True:
            app.chicaBathroom = True
            app.chicaPIZZA = False
        
        elif app.chicaBathroom == True:
            app.chicaKitchen = True
            app.chicaBathroom = False
            
        elif app.chicaKitchen == True:
            app.chicaOnHerWay = True
            app.chicaKitchen = False
            
        elif app.chicaOnHerWay == True:
            app.chicaOnHerWayButCloser = True
            app.chicaOnHerWay = False
            
        elif app.chicaOnHerWayButCloser == True:
            app.chicaGivingThatStare = True
            app.chicaOnHerWayButCloser = False
            
        elif app.chicaGivingThatStare == True and app.rightDoor == False:
            app.dead = True
            app.chiKill = True
        else:
            app.chicaPIZZA = True
            app.chicaGivingThatStare = False
        
def bongonPath(app):
    if movementCheck(app, app.bonnieDif) == True:
        if app.bonnieMainStage == True:
            app.bonnieStupidFace = True
            app.bonnieMainStage = False
            
        
        elif app.bonnieStupidFace == True:
            app.bonnieBackstage = True
            app.bonnieStupidFace = False
        
        elif app.bonnieBackstage == True and app.bonnieDif >= 15:
            app.bonnieBsMenacing = True
            app.bonnieBackstage = False
        
        elif app.bonnieBackstage == True or app.bonnieBsMenacing == True:
            app.bonnieComing = True
            app.bonnieBackstage = False
            app.bonnieBsMenacing = False
            
        elif app.bonnieComing == True:
            app.bonnieInTheCloset = True
            app.bonnieComing = False
            
        elif app.bonnieInTheCloset == True:
            app.bonnieRizz = True
            app.bonnieInTheCloset = False
            
        elif app.bonnieRizz == True and app.leftDoor == False:
            app.dead = True
            app.bonGonKill = True
        else:
            app.bonnieStupidFace = True
            app.bonnieRizz = False

def hooksPath(app):
    if movementCheck(app, app.foxyDif) == True:
        if app.foxyCloseted == True:
            app.foxyPeeking = True
            app.foxyCloseted = False
        
        elif app.foxyPeeking == True:
            app.foxyLeaving = True
            app.foxyPeeking = False
        
        elif app.foxyLeaving == True:
            app.foxyGone = True
            app.foxyLeaving = False
            
        if app.foxyGone == True:
            app.foxyComing = not app.foxyComing
            
            
        if app.foxyComing == True and app.leftDoor == True:
            app.foxyCloseted = True
            app.foxyGone = False

            
#####--------------------------------------------------------------------------------------------------#    

def onStep(app):
    app.steps += app.adjust
    if app.title == False:
        app.adjust = 1
        if app.helpOpacity < 100:
            app.helpOpacity += 1
    
    if app.nightTransition == True:
        app.adjust = 1
        if app.transition > 0:
            app.transition -= .5
            
        app.office = True
        if 0 <= app.offTrans <= 98 :
            if app.transition <= 50:
                app.offTrans += 1
            
            app.offTrans += 1
            
            if app.offTrans == 99:
                app.offTrans = 100
                app.steps = 0           
                
    if app.transition == 0 and app.offTrans == 100 and app.hour != 6:
        
        app.nightTransition = False
        app.adjust = 1
    
        if app.steps % 20 == 0:
    
            app.seconds += 1
            if app.seconds % 60 == 0:
                app.hour += 1
                if app.hour > 12:
                    app.hour = 1
        
        if app.steps % 60 == 0:
            if app.freddyDif > 0:            
                movementCheck(app, app.freddyDif)
                fredbedPath(app)
                
        if app.steps % 97 == 0:    
            if app.bonnieDif > 0:
                movementCheck(app, app.bonnieDif)
                bongonPath(app)
            
        if app.steps % 99 == 0:
            if app.chicaDif > 0:
                movementCheck(app, app.chicaDif)
                chickenPath(app)
            
        if app.steps % 175 == 0:
            if app.foxyDif > 0:
                movementCheck(app, app.foxyDif)
                hooksPath(app)
            
    if app.hour == 6:
        app.adjust = 0
        app.steps = 0
        app.nightEnd = True
        app.office = False
        
    if app.leftDoor == True:
        if app.lDoor < 520:
            app.lDoor += 30
    
    if app.leftDoor == False:
        if app.lDoor > 30:
            app.lDoor -= 30
            
    if app.rightDoor == True:
        if app.rDoor < 520:
            app.rDoor += 30
        
    if app.rightDoor == False:
        if app.rDoor > 30:
            app.rDoor -= 30
            
    if app.chiKill == True:
        app.stepsPerSecond = 16
    else:
        app.stepsPerSecond = 20
'''    
    app.imageCenterX += app.imageSpeed
    if app.imageCenterX >= 550 or app.imageCenterX <= 250:
        app.imageSpeed *= -1
'''   
    
    
#####--------------------------------------------------------------------------------------------------#    

def redrawAll(app):
    if app.title == True:
        drawTitle(app)

    if app.helpWanted == True:
        drawHelpWanted(app)

    if app.nightTransition == True:
        drawNightTransition(app)

    if app.office == True:
        drawOffice(app)
        camFlick(app)

#####  Camera Calls
    if app.camUp == True and app.cam1A == True:
        mainStage(app)
    
    if app.camUp == True and app.cam1B == True:
        dining(app)
        
    if app.camUp == True and app.cam1C == True:
        pirateCove(app)
    
#####--------------------------------------------------------------------------------------------------#
    if app.nightEnd == True:
        drawNightEnd(app)
    
    if app.dead == True:
        if app.freddyKillin == True:
            fredbedScare(app)
        
        if app.bonGonKill == True:
            bongonKill(app)
            
        if app.chiKill == True:
            chickKicken(app)

#####--------------------------------------------------------------------------------------------------#        
        
def onMousePress(app, mouseX, mouseY):
    if app.withinNew == True:
        app.title = False
        app.helpWanted = True
        
    if app.helpOpacity == 100:
        app.helpWanted = False
        app.nightTransition = True
        app.steps = 0

    if 0 <= mouseX <= 50 and 250 <= mouseY <= 300:
        app.leftDoor = not app.leftDoor
        
    if 0 <= mouseX <= 50 and 300 <= mouseY <= 350:
        app.leftLight = not app.leftLight
        
    if 750 <= mouseX <= 800 and 250 <= mouseY <= 300:
        app.rightDoor = not app.rightDoor
        
    if 750 <= mouseX <= 800 and 300 <= mouseY <= 350:
        app.rightLight = not app.rightLight
    

    if app.withinCon == True:
        app.title = False
        app.nightTransition = True
    
    # Camera Calls
    if app.camUp == True: 
        if 550 < mouseX < 585 and 250 < mouseY < 270:
            app.cam1A = True
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False    
            
        if 550 < mouseX < 585 and 300 < mouseY < 320:
            app.cam1A = False
            app.cam1B = True
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False
            
        if 525 < mouseX < 560 and 362 < mouseY < 382:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = True
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False
                
        if 560 < mouseX < 595 and 440 < mouseY < 460:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = True
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False        
            
        if 560 < mouseX < 595 and 460 < mouseY < 480:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = True
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False        
            
        if 515 < mouseX < 550 and 445 < mouseY < 465:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = True
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False    
            
        if 635 < mouseX < 670 and 440 < mouseY < 460:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = True
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False    
            
        if 635 < mouseX < 670 and 460 < mouseY < 480: 
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = True
            app.cam5 = False
            app.cam6 = False
            app.cam7 = False        
            
        if 465 < mouseX < 500 and 335 < mouseY < 355:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = True
            app.cam6 = False
            app.cam7 = False
            
        if 695 < mouseX < 730 and 430 < mouseY < 450:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = True
            app.cam7 = False
            
        if 697 < mouseX < 732 and 315 < mouseY < 335:
            app.cam1A = False
            app.cam1B = False
            app.cam1C = False
            app.cam2A = False
            app.cam2B = False
            app.cam3 = False
            app.cam4A = False
            app.cam4B = False
            app.cam5 = False
            app.cam6 = False
            app.cam7 = True
            
    if app.office == True or app.camUp == True:
        if mouseY >= 450 and mouseX < 500:
            app.camUp = not app.camUp
            
            app.office = not app.office
    
    if app.dead == True:
        restart(app)
            
#####--------------------------------------------------------------------------------------------------#

def onMouseMove(app, mouseX, mouseY):
    if 120 <= mouseX <= 280 and 245 <= mouseY <= 275:
        app.withinNew = True
    else:
        app.withinNew = False
        
        
    if 120 <= mouseX <= 240 and 275 <= mouseY <= 310:
        app.withinCon = True
    else:
        app.withinCon = False
        
#####--------------------------------------------------------------------------------------------------#

def onKeyPress(app, key):
    if key == 'f':
        app.dead = True
        app.freddyKillin = True
    
    if key == 'b':
        app.dead = True
        app.bonGonKill = True
        
    if key == 'c':
        app.dead = True
        app.chiKill = True
        
def main():
    runApp()

main()
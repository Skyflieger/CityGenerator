import sys
from PyQt5.QtCore import Qt, QT_VERSION_STR
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QFileDialog
from QtImageViewer import QtImageViewer
from map import map
from roads import roads
from PIL.ImageQt import ImageQt


# Custom slot for handling mouse clicks in our viewer.
# Just prints the (row, column) matrix index of the 
# image pixel that was clicked on.
def handleLeftClick(x, y):
    row = int(y)
    column = int(x)
    print("Pixel (row="+str(row)+", column="+str(column)+")")
    

if __name__ == '__main__':
    # Create the QApplication.
    app = QApplication(sys.argv)
        
    # Create an image viewer widget.
    viewer = QtImageViewer()
        
    # Set viewer's aspect ratio mode.
    # !!! ONLY applies to full image view.
    # !!! Aspect ratio always ignored when zoomed.
    #   Qt.IgnoreAspectRatio: Fit to viewport.
    #   Qt.KeepAspectRatio: Fit in viewport using aspect ratio.
    #   Qt.KeepAspectRatioByExpanding: Fill viewport using aspect ratio.
    viewer.aspectRatioMode = Qt.KeepAspectRatio
    
    # Set the viewer's scroll bar behaviour.
    #   Qt.ScrollBarAlwaysOff: Never show scroll bar.
    #   Qt.ScrollBarAlwaysOn: Always show scroll bar.
    #   Qt.ScrollBarAsNeeded: Show scroll bar only when zoomed.
    viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    
    # Allow zooming with right mouse button.
    # Drag for zoom box, doubleclick to view full image.
    viewer.canZoom = True
    
    # Allow panning with left mouse button.
    viewer.canPan = True
    
    # Display the image in the viewer.
    
    viewer.setImage(map.generate(map))
    
    # Handle left mouse clicks with your own custom slot
    # handleLeftClick(x, y). (x, y) are image coordinates.
    # For (row, col) matrix indexing, row=y and col=x.
    # ImageViewerQt also provides similar signals for
    # left/right mouse button press, release and doubleclick.
    viewer.leftMouseButtonPressed.connect(handleLeftClick)
        
    # Show the viewer and run the application.
    viewer.show()
    sys.exit(app.exec_())
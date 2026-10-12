import QtQuick
import QtQuick.Controls.Basic

Button {
    id: root

    width: 50
    height: 50
    
    property color bgColor: "#8744a1"
    property color bgHoverColor: "#804fdb"
    property color bgPressedColor: "#b199dd"

    property string imagePath: ""
    property int imageSize: 15

    background: Rectangle {
        color: root.down ? root.bgPressedColor : root.hovered ? root.bgHoverColor : root.bgColor

        anchors.fill: parent
        radius: root.width / 2

        Behavior on color {
            ColorAnimation {
                duration: 100
            }
        }
    }

    contentItem: Item {
        Image {
            source: root.imagePath
            
            width: root.imageSize
            height: root.imageSize


            fillMode: Image.PreserveAspectFit

            anchors.centerIn: parent
        
        }   
    }
}
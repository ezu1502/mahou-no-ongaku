import QtQuick
import QtQuick.Controls.Basic
import ".."
Button {
    id: root

    width: 50
    height: 50
    
    property color bgColor: ThemeVision.mahouHighlight
    property color bgHoverColor: ThemeVision.navHover
    property color bgPressedColor: "#b199dd" // todo implementar cor nova aqui

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
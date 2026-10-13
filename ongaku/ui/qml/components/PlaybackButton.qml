import QtQuick
import QtQuick.Controls.Basic
import Qt5Compat.GraphicalEffects

import ".."
Button {
    id: root

    width: 50
    height: 50
    
    property color bgColor: ThemeVision.mahouHighlight
    property color bgHoverColor: ThemeVision.navHover
    property color bgPressedColor: ThemeVision.surfacePressed // todo implementar cor nova aqui

    property color iconColor: "#FF0000"

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
            id: icon
            source: root.imagePath
            
            width: root.imageSize
            height: root.imageSize


            fillMode: Image.PreserveAspectFit

            anchors.centerIn: parent          
        }  

        ColorOverlay {
            anchors.fill: icon
            source: icon
            color: root.iconColor

            Behavior on color {
                ColorAnimation {
                    duration: 100
                }
            }
        }
    }
}
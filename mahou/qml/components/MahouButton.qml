import QtQuick
import QtQuick.Controls.Basic

Button {
    id: root

    property int defaultWidth: 180
    property int defaultHeight: 55

    width: defaultWidth
    height: defaultHeight

    font.family: "Bahnschrift"
    font.pixelSize: 18

    property color baseColor: "#222222"
    property color hoverColor: "#353535"
    property color pressColor: '#777777'

    property color baseBorder: "#4C4C4C"
    property color hoverBorder: "#4C4C4C"
    property color pressBorder: "#020202"

    property color baseText: "#EEEEEE"
    property color pressText: "#020202"






    background: Rectangle {
        color: "#222222"
        radius: 12

        border.width: 1
        border.color: "#4c4c4c"
    }

    contentItem: Text {
        id: buttonText

        text: root.text
        font: root.font
        color: root.baseText
        anchors.fill: parent

        horizontalAlignment: Qt.AlignHCenter
        verticalAlignment: Qt.AlignVCenter
    }

    onHoveredChanged: {
        if (hovered && !pressed){
            exitedAnimation.stop()
            hoverAnimation.restart()
        }
        else if (!hovered && !pressed){
            hoverAnimation.stop()
            exitedAnimation.restart()
        }  
        else if (!hovered && pressed){
            hoverAnimation.stop()
            pressAnimation.stop()


            releaseAnimation.restart()
        }
    }

    onPressed: {
        releaseAnimation.stop()
        pressAnimation.restart()
    }

    onReleased: {
        pressAnimation.stop()
        releaseAnimation.restart()
    }

    onClicked: {
        
    }

// press
    ParallelAnimation{
        id: releaseAnimation
            ColorAnimation {
                target: root.background
                property: "color"

                to: root.baseColor
                duration: 200
            }

            ColorAnimation {
                target: buttonText
                property: "color"

                to: root.baseText
                duration: 200
            }
    }
// release
    ParallelAnimation{
        id: pressAnimation
        ColorAnimation {
            target: root.background
            property: "color"

            to: root.pressColor
            duration: 50
        }

        ColorAnimation {
            target: buttonText
            property: "color"

            to: root.pressText
            duration: 50
        }
    }
//  hover
    ColorAnimation {
        id: hoverAnimation

        target: root.background
            property: "color"

            to: root.hoverColor
            duration: 100
    }
// exited
    ColorAnimation {
        id: exitedAnimation

        target: root.background
            property: "color"

            to: root.baseColor
            duration: 150

            easing.type: Easing.InQuad
    }
      
}
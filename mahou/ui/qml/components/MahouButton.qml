import QtQuick
import QtQuick.Controls.Basic

Button {
    id: root

    property int defaultWidth: 230
    property int defaultHeight: 65

    width: defaultWidth
    height: defaultHeight

    font.family: "Bahnschrift"
    font.pixelSize: 16

    property color baseColor: "#222222"
    property color hoverColor: "#2b2b2b"
    property color pressColor: "#4A4A4A"

    property color borderBase: "#555555"
    property color borderHover: "#555555"
    property color borderPress: "#020202"



    background: Rectangle {
        color: root.pressed ? root.pressColor : root.hovered ? root.hoverColor : root.baseColor

        border.width: 1
        radius: 10
        border.color: root.pressed ? root.borderPress : root.hovered ? root.borderHover : root.borderBase

        Behavior on color {
            ColorAnimation {
                duration: 100
            }
        }

        Behavior on border.color {
            ColorAnimation {
                duration: 100
            }
        }
    }

    contentItem: Text {
        text: root.text
        font: root.font
        color: root.pressed ? "#020202" : "#EEEEEE"

        horizontalAlignment: Qt.AlignHCenter
        verticalAlignment: Qt.AlignVCenter

        Behavior on color {
            ColorAnimation {
                duration: 100
            }
        }
    }
}
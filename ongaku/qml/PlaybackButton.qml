import QtQuick
import QtQuick.Controls.Basic

Button {
    id: root

    width: 40
    height: 40
    
    property color font_color: "#EEEEEE"
    
    property bool transparent_bg: false

    background: Rectangle {
        color: root.transparent_bg ? "transparent" : root.down ? '#b199dd' : root.hovered ? '#804fdb' : "#6f33df"

        anchors.fill: parent
        radius: root.width / 2

        Behavior on color {
            ColorAnimation {
                duration: 100
            }
        }
    }

    contentItem: Text {

        color: root.font_color

        anchors.fill: parent

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        text: root.text

        font: root.font
    }
}
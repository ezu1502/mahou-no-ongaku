import QtQuick
import QtQuick.Controls.Basic

Button {
    id: root

    implicitWidth: 180
    implicitHeight: 60

    

    background: Rectangle {
        anchors.fill: parent
        color: root.hovered ? "#444444" : "#333333"
        radius: 10
    }

    contentItem: Text {
        anchors.fill: parent

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        font.pixelSize: 20
        font.family: "Noto Sans"

        text: root.text
        color: "#EEEEEE"
    }
}
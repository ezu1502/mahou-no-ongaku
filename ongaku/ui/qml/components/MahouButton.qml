import QtQuick
import QtQuick.Controls.Basic
import ".."

Button {
    id: root

    implicitWidth: 180
    implicitHeight: 60

    background: Rectangle {
        anchors.fill: parent
        color: root.hovered ? ThemeVision.navHover : ThemeVision.surface
        radius: 10
    }

    contentItem: Text {
        anchors.fill: parent

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        font.pixelSize: 20
        font.family: "Noto Sans"

        text: root.text
        color: ThemeVision.foreground
    }
}
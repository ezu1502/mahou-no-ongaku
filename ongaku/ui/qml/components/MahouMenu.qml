import QtQuick
import QtQuick.Controls.Basic
import ".."
Menu {
    id: root
    implicitWidth: 200
    padding: 1
    
    background: Rectangle {
        color: ThemeVision.surface
        radius: 5

        border.color: "#666666"
        border.width: 1
    }

    delegate: MenuItem {
        id: menuItem
        implicitWidth: 200
        implicitHeight: 36


        background: Rectangle {
            color: menuItem.highlighted ? ThemeVision.progressBackground: "transparent"
            radius: 5

            anchors.rightMargin: 4
        }

        contentItem: Text {
            anchors.fill: parent

            text: menuItem.text
            verticalAlignment: Text.AlignVCenter

            color: ThemeVision.foreground
            font.pixelSize: 14

            leftPadding: 12
        }
    }

}
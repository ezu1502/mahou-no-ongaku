import QtQuick
import QtQuick.Controls.Basic

Menu {
    id: root
    implicitWidth: 200
    padding: 1
    
    background: Rectangle {
        color: "#222222"
        radius: 5

        border.color: "#666666"
        border.width: 1
    }
    clip: true

    delegate: MenuItem {
        id: menuItem
        implicitWidth: 200
        implicitHeight: 36


        background: Rectangle {
            color: menuItem.highlighted ? "#333333" : "transparent"
            radius: 5

            anchors.rightMargin: 4
        }

        contentItem: Text {
            anchors.fill: parent

            text: menuItem.text
            verticalAlignment: Text.AlignVCenter

            color: "#EEEEEE"
            font.pixelSize: 14

            leftPadding: 12
        }
    }

}
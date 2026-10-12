import QtQuick
import QtQuick.Controls.Basic

MenuBar {
    id: mahouNav

    background: Rectangle {
        color: '#8744a1'
    }

    delegate: MenuBarItem {
        id: menuItem

        background: Rectangle {
            color: menuItem.highlighted ? '#916e9e' : "#8744a1"
            radius: 5

            Behavior on color {
                ColorAnimation {
                    duration: 100
                }
            }
        }

        contentItem: Text {
            text: menuItem.text
            anchors.fill: parent
            
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            font.family: "Noto Sans"
            font.pixelSize: 14

            color: "#111111"
        }
    }
}
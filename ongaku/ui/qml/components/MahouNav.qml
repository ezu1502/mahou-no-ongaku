import QtQuick
import QtQuick.Controls.Basic
import ".."
MenuBar {
    id: mahouNav

    background: Rectangle {
        color: ThemeVision.navBackground
    }

    delegate: MenuBarItem {
        id: menuItem

        background: Rectangle {
            color: menuItem.highlighted ? ThemeVision.navHover: ThemeVision.navBackground
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

            color: ThemeVision.navText
        }
    }
}
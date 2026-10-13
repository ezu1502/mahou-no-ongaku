import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
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

        property string shortcutName: ""



        background: Rectangle {
            color: menuItem.highlighted ? ThemeVision.progressBackground: "transparent"
            radius: 5

    
            anchors.rightMargin: 4
        }

        contentItem: Item {
            anchors.fill: parent

            


            RowLayout {
                anchors.fill: parent
            
                anchors.leftMargin: 12
                anchors.rightMargin: 12
                spacing: 8

                Text {
                    text: menuItem.text
                    verticalAlignment: Text.AlignVCenter

                    color: ThemeVision.foreground
                    font.pixelSize: 14

                    Layout.alignment: Qt.AlignVCenter
                }

                Item {
                    Layout.fillWidth: true
                }

                Text {
                    text: menuItem.action ? menuItem.action.shortcut.toString() : ""
                    verticalAlignment: Text.AlignVCenter

                    color: ThemeVision.secondaryText
                    font.pixelSize: 14

                    Layout.alignment: Qt.AlignVCenter

                }
            }   
            
        }

    }

}
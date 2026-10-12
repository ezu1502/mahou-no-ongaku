pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls.Basic

ListView {
    signal songSelected(string path)

    required property var proxyModel

    id: root

    currentIndex: -1

    model: root.proxyModel

    clip: true


    delegate: Rectangle {
        required property string title
        required property int index
        required property string path
        required property string artists

        id: delegateRect

        width: root.width
        height: 50

        color: index === root.currentIndex ? "#333333" : "#222222"

        Behavior on color {
            ColorAnimation {
                duration: 80
            }
        }

        Column {
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 20


            MahouLabel {    
                text: delegateRect.title
                font.pixelSize: 18    
                verticalAlignment: Text.AlignVCenter
            }

            MahouLabel {    
                text: delegateRect.artists
                font.pixelSize: 15
                color: "#AAAAAA"    
                verticalAlignment: Text.AlignVCenter

            }

            
        }
        

        MouseArea {
            anchors.fill: parent

            onClicked: {
                root.currentIndex = delegateRect.index

                root.songSelected(delegateRect.path)
            }


        }
    }

}
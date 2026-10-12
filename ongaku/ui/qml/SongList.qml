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

        id: delegateRect

        width: root.width
        height: 40

        color: index === root.currentIndex ? "#333333" : "#222222"

        MahouLabel {
            text: parent.title
            font.pixelSize: 18

            anchors.fill: parent
            
            anchors.leftMargin: 20
            verticalAlignment: Text.AlignVCenter
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
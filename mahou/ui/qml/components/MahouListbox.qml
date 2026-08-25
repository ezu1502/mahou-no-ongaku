import QtQuick
import QtQuick.Controls.Basic

Rectangle {
    id: rect

    implicitWidth: 400
    implicitHeight: 450
    
    color: "#0D0D0D"

    border.width: 3
    border.color: "#202020"

    ListView {
        id: root

        anchors.fill: parent
        anchors.margins: 3

        model: song_proxy

        currentIndex: -1

        clip: true

        onCurrentIndexChanged: {
            if (currentIndex >= 0){
                const index = song_proxy.index(currentIndex, 0)
                const song = song_proxy.data(index, Qt.UserRole + 2)

                backend.select_song(song)
            }
        }
        
        ScrollBar.vertical: ScrollBar {
            id: scroll
            policy: ScrollBar.AsNeeded

            visible: root.contentHeight > root.height

            background: Rectangle {
                implicitWidth: 8
                color: "transparent"
            }

            contentItem: Rectangle {
                implicitWidth: 6

                implicitHeight: 50



                radius: width / 2
                

                color: scroll.pressed ? "#4422DD" : scroll.hovered ? "#454545" : "#333333"

                Behavior on color {
                    ColorAnimation {
                        duration: 80
                    }
                }
            }
        }

        delegate: ListItemDelegate {
            listView: root
            itemIndex: index

            width: root.width
        }

            
    }


    
}

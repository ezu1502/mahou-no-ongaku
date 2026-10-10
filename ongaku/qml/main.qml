import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Dialogs

ApplicationWindow {
    visible: true

    width: 1280
    height: 720

    title: "Mahou no Ongaku"

    Component.onCompleted: showMaximized()

    FolderDialog {
        id: folderDialog
        title: "Choose folder to scan"

        onAccepted: {
            backend.receive_folder(folderDialog.selectedFolder)
        }
    }

    menuBar: MenuBar {
        Menu {
            title: "File"

            Action {
                text: "Scan Folder..."
                onTriggered: {
                    folderDialog.open()
                }
            }
        }

        Menu {
            title: "Controls"
        }

        Menu {
            title: "Help"
        }
    }

    Rectangle {
        anchors.fill: parent

        color: "#111111"

    }

    MahouTitle {
        text: "Mahou no Ongaku"
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
    }

    Row {
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        anchors.margins: 20

        Button {
            id: backButton
            text: "◂"

            width: 40
            height: 40
            
            background: Rectangle {
                color: "transparent"
            }
            contentItem: Text {

                color: "#EEEEEE"

                anchors.fill: parent

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                text: backButton.text

                font.pixelSize: 25
            }
        }

        


        Button {
            id: playButton

            text: "▶"

            width: 40
            height: 40

            background: Rectangle {
                anchors.fill: parent
                radius: parent.width / 2

                color: '#6f33df'
            }

            contentItem: Text {
                anchors.fill: parent

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                text: playButton.text

                font.pixelSize: 25
            }
        }

        Button {
            id: forwardButton

            text: "▸"

            width: 40
            height: 40

            background: Rectangle {
                color: "transparent"
            }
            
            contentItem: Text {
                color: "#EEEEEE"
                anchors.fill: parent

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                text: forwardButton.text

                font.pixelSize: 25
            }
        }
    }

}
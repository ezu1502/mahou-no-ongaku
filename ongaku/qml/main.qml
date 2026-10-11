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

        PlaybackButton {
            transparent_bg: true
            text: "◁"
            font.pixelSize: 20

        }


        PlaybackButton {
            text: "▶"

            font.pixelSize: 25
            font_color: "#111111"
        }

        PlaybackButton {
            transparent_bg: true
            text: "▷"
            font.pixelSize: 20

        }
    }

}
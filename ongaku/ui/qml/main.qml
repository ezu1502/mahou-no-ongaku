import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Dialogs

ApplicationWindow {
    visible: true

    width: 1280
    height: 720

    title: "Mahou no Ongaku"
    color: "#111111"


    Component.onCompleted: showMaximized()


    FolderDialog {
        id: folderDialog
        title: "Choose folder to scan"

        onAccepted: {
            backend.receive_folder(folderDialog.selectedFolder)
        }
    }

    menuBar: MahouNav {
        id: mahouNav

        MahouMenu {
            title: "File"

            Action {
                text: "Scan Folder..."
                onTriggered: {
                    folderDialog.open()
                }
            }
        }

        MahouMenu {
            title: "Controls"
        }

        MahouMenu {
            title: "Theme"
        }

        MahouMenu {
            title: "Help"
        }
    }


    MahouTitle {
        id: mahouTitle
        text: "Mahou no Ongaku"
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
    }

    Item {
        anchors.top: mahouTitle.bottom
        anchors.right: parent.right

        anchors.left: parent.left
        anchors.bottom: buttonsPanel.top

        anchors.topMargin: 20
        
        SongList {
            anchors.fill: parent

            proxyModel: proxy

            onSongSelected: (path) => {
                backend.on_song_selected(path)
            }
        }
    }
    

    Row {
        id: buttonsPanel
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        anchors.margins: 20
        spacing: 5

        PlaybackButton {

            imagePath: "../assets/previous_icon.png"
            imageSize: 15

            bgColor: "transparent"
            bgHoverColor: "#222222"
            bgPressedColor: "#222222"
        }

        PlaybackButton {
            imagePath: backend.app_state !== "playing" ? "../assets/play_icon.png" : "../assets/pause_icon.png"
            imageSize: 20
    
            onClicked: {
                backend.toggle()
            }
        }

        PlaybackButton {
            imagePath: "../assets/next_icon.png"
            imageSize: 15

            bgColor: "transparent"
            bgHoverColor: "#222222"
            bgPressedColor: "#222222"
        }

        PlaybackButton {
            imagePath: "../assets/stop_icon.png"
            imageSize: 13

            bgColor: "transparent"
            bgHoverColor: "#222222"
            bgPressedColor: "#222222"
        }
    }

}
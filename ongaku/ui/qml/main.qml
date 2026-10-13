import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Dialogs

import "./components"
import "."


ApplicationWindow {
    id: window
    visible: true

    width: 1280
    height: 720

    title: "Mahou no Ongaku"
    color: ThemeVision.background

    Behavior on color {
        ColorAnimation {
            duration: 100
        }
    }
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

                shortcut: "Ctrl+O"
                
            }
        }

        MahouMenu {
            title: "Controls"

            Action {
                text: "Play/Pause"

                shortcut: "Space"

                onTriggered: {
                    backend.toggle();
                }
            }

            Action {
                text: "Stop"

                shortcut: "S"

                onTriggered: {
                    backend.stop_player();
                }
            }

            Action {
                text: "Previous Song"

                shortcut: "Left"

                onTriggered: {
                    backend.change_song(-1);
                }
            }

            Action {
                text: "Next Song"

                shortcut: "Right"

                onTriggered: {
                    backend.change_song(1);
                }
            }

            Action {
                text: "Restart Song"

                shortcut: "R"


                onTriggered: {
                    backend.restart_song();
                }
            }

        }

        MahouMenu {
            title: "Options"

            Action {
                text: "Folder Scan Mode"
                // TODO colocar os modos: recursivo, ignorar subpastas etc.
            }
        }

        MahouMenu {
            title: "Theme"

            Action {
                text: "Dark"

                onTriggered: {
                    ThemeManager.setTheme("Dark");
                }
            }

            Action {
                text: "Light"
                onTriggered: {
                    ThemeManager.setTheme("Light");
                }
            }

            Action {
                text: "Habanero"

                onTriggered: {
                    ThemeManager.setTheme("Habanero");
                }
            }

            Action {
                text: "Monochrome"

                onTriggered: {
                    ThemeManager.setTheme("Monochrome");
                }
            }

            Action {
                text: "Cheesecake"

                onTriggered: {
                    ThemeManager.setTheme("Cheesecake");
                }
            }

            Action {
                text: "Future"

                onTriggered: {
                    ThemeManager.setTheme("Future");
                }
            }
        }

        MahouMenu {
            title: "Help"

            Action {
                text: "About Mahou..."
            }

            Action {
                text: "GitHub"
            }

            Action {
                text: "Go to website"
            }
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

    MahouProgressBar {
        id: progressBar
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40

        anchors.horizontalCenter: parent.horizontalCenter
    }
    

    Row {
        id: buttonsPanel
        anchors.bottom: parent.bottom
        anchors.right: parent.right

        anchors.margins: 20
        spacing: 5
        
        PlaybackButton {

            imagePath: "../../assets/previous_icon.png"
            imageSize: 15

            bgColor: "transparent"
            bgHoverColor: ThemeVision.surface
            bgPressedColor: ThemeVision.surface

            iconColor: ThemeVision.foreground

            onClicked: {
                if (progressBar.progressPercent * progressBar.durationSeconds > 5){
                    backend.restart_song();
                }
                else {  
                    backend.change_song(-1);
                }

            }
        }

        PlaybackButton {
            imagePath: backend.app_state !== "playing" ? "../../assets/play_icon.png" : "../../assets/pause_icon.png"
            imageSize: 20

            bgColor: ThemeVision.mahouHighlight
            bgHoverColor: ThemeVision.navHover
            bgPressedColor: ThemeVision.navPressed

            iconColor: ThemeVision.background
            onClicked: {
                backend.toggle()
            }
        }

        PlaybackButton {
            imagePath: "../../assets/next_icon.png"
            imageSize: 15

            bgColor: "transparent"
            bgHoverColor: ThemeVision.surface
            bgPressedColor: ThemeVision.surface

            iconColor: ThemeVision.foreground

            onClicked: {
                backend.change_song(1);
            }
        }

        PlaybackButton {
            imagePath: "../../assets/stop_icon.png"
            imageSize: 13

            bgColor: "transparent"
            bgHoverColor: ThemeVision.surface
            bgPressedColor: ThemeVision.surface
            iconColor: ThemeVision.foreground


            onClicked: {
                backend.stop_player();
            }
        }
    }



    Shortcut {
        sequence: "Esc"
        onActivated: {
            if (window.visibility === Window.FullScreen)
                window.visibility = Window.Windowed;
        }
    }

    Shortcut {
        sequence: "F11"
        onActivated: {
            window.visibility = window.visibility === Window.FullScreen ? Window.Windowed : Window.FullScreen;
        }
    }

    
}
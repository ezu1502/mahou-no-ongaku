import QtQuick
import QtQuick.Controls.Basic

import ".."


Item {
    id: buttonArea

    signal requestFolderChooser()

    Column {
        id: buttonPanel
        spacing: 15

        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        
        
        MahouButton {
            property string playerState: backend ? backend.state : "playing"

            text: (playerState === "playing") ? "PAUSE" : "PLAY"

            onClicked: {
                backend.toggle()
            }
        }
        // TODO TERMINAR DE LINKAR O STATE DO PLAYER COM O DA WINDOW


        MahouButton {
            text: "Scan Folder"

            onClicked: {
                buttonArea.requestFolderChooser()
            }
        }

        Row {
            spacing: 8
            MahouButton {
                id: previousButton
                text: "Previous"

                width: previousButton.defaultWidth / 2 - 4

            }
            MahouButton{
                id: nextButton
                text: "Next"

                
                width: nextButton.defaultWidth / 2 - 4

            }
        }

        Column {
            spacing: 2

            id: nowPlayingLabel

            visible: backend.now_playing != "None"
        
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter

            
            

            MahouLabel {
                text: "Now Playing:\n"
                font.pixelSize: 20
                font.weight: 500

                horizontalAlignment: Text.AlignHCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }

            MahouLabel {
                text: backend.now_playing
                font.pixelSize: 20
                font.weight: 500
                color: "#FFFF00"

                horizontalAlignment: Text.AlignHCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
        

    
    }
}
    
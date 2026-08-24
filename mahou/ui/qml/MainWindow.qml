import QtQuick
import QtQuick.Controls.Basic

import "./components"

ApplicationWindow {
    width: 950
    height: 600

    title: "Mahou no Ongaku"

    MahouFonts {}

    background: Rectangle {
        color: "#111111"
    }

    visible: true

    MahouLabel {
        text: "Mahou no Ongaku"

        font.family: "Zen Kaku Gothic New"
        font.weight: Font.Bold
        font.pixelSize: 42

        anchors.margins: 18
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top

    }
    Column {
        anchors.centerIn: parent
        spacing: 15

        

        MahouButton {
            text: "PLAY"
        }

        MahouButton {
            text: "Scan Folder"

            onClicked: {
                folderChooser.open()
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
        
    }
    
    FolderChooser {
        id: folderChooser
    }
}
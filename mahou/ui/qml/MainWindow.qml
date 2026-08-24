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
        id: mahouTitle
        text: "Mahou no Ongaku"

        font.family: "Zen Kaku Gothic New"
        font.weight: Font.Bold
        font.pixelSize: 42

        anchors.margins: 18
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top

    }

    Item {
        anchors.top: mahouTitle.bottom
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.left: parent.left

        anchors.margins: 25
        anchors.topMargin: 20

    Row {
        anchors.centerIn: parent

        spacing: 15
        
        MahouListbox {
            id: mahouListbox
        }

        Column {
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

        
    }
    }

/*
   

*/
    
    FolderChooser {
        id: folderChooser
    }
}
import QtQuick
import QtQuick.Controls.Basic

import "./components"

ApplicationWindow {
    id: window
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

        anchors.margins: 10
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

        
        MahouListbox {
            id: mahouListbox

            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            width: parent.width * 0.55
        }

        Item {
            id: buttonArea
            anchors.left: mahouListbox.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            Column {
                id: buttonPanel
                spacing: 15

                anchors.horizontalCenter: parent.horizontalCenter
                anchors.top: parent.top
                
                
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
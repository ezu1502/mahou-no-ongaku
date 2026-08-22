import QtQuick
import QtQuick.Controls.Basic
import "./components"

ApplicationWindow {
    id: mainWindow

    title: "Mahou no Ongaku"

    width: 900
    height: 600

    visible: true

    background: Rectangle {
        color: "#111111"
    }

    MahouLabel {
        text: "Mahou no Ongaku"

        font.pixelSize: 35
        font.weight: 650

        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 25
    }

    Column {
        spacing: 15
        anchors.centerIn: parent



        MahouButton {
            text: "Play"
            anchors.horizontalCenter: parent.horizontalCenter
        }

        MahouButton {
            text: "Scan Folder"
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Row {
            anchors.horizontalCenter: parent.horizontalCenter

            spacing: 6

            MahouButton {
                id: previousButton
                text: "Previous"

                width: (previousButton.defaultWidth / 2) - 3

                
            }
            MahouButton {
                id: nextButton
                text: "Next"

                width: (previousButton.defaultWidth / 2) - 3
            }
        }


    }
    


}


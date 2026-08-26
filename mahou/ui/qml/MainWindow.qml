import QtQuick
import QtQuick.Controls.Basic

import "./components"
import "./components/specific"

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

    Shortcut {
        sequence: "Space"

        onActivated: backend.toggle()
    }

    Shortcut {
        sequence: "S"

        onActivated: {
            backend.stop_song()
            contentArea.clearListboxSelection()
        }
    }




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

    ContentArea {
        id: contentArea
        anchors.top: mahouTitle.bottom
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.left: parent.left
    }

}
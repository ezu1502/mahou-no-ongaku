import QtQuick
import QtQuick.Controls.Basic

Rectangle {
    id: rect

    width: 400
    height: 450
    
    color: "#010101"

    ListView {
        id: root

        anchors.fill: parent


        model: song_proxy

        delegate: Text {
            text: model.title
            color: "#EEEEEE"
            font.pixelSize: 20
        }
    }
}

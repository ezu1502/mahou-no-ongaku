import QtQuick
import QtQuick.Controls.Basic

import ".."

Item {
    id: root
  
    anchors.margins: 25
    anchors.topMargin: 20

    function clearListboxSelection() {
        // callback

        mahouListbox.clearSelection()
    }
    MahouListbox {
        id: mahouListbox

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        width: parent.width * 0.55
    }

    ButtonArea {
        id: buttonArea
        anchors.left: mahouListbox.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        onRequestFolderChooser: folderChooser.open()
    }

    FolderChooser {
        id: folderChooser
    }
}

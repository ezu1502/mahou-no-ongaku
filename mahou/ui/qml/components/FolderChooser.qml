import QtQuick
import QtQuick.Dialogs

FolderDialog {
    id: folderChooser

    title: "Choose folder to scan"

    onAccepted: {
        backend.receive_folder(folderChooser.selectedFolder)
    }

    acceptLabel: "Scan Folder"
    rejectLabel: "Cancel"
}